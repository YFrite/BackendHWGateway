import requests
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods


@csrf_exempt
@require_http_methods(["GET", "POST", "PUT", "PATCH", "DELETE"])
def gateway_view(request, path=''):
    target_url = f'http://192.168.0.105:8001/{path}'

    headers = {
        key: value for key, value in request.headers.items()
        if key.lower() not in ['host', 'content-length', 'connection']
    }

    try:
        response = requests.request(
            method=request.method,
            url=target_url,
            headers=headers,
            params=request.GET,
            data=request.body,
            stream=True
        )

        proxy_response = HttpResponse(
            response.content,
            status=response.status_code,
            content_type=response.headers.get('Content-Type')
        )

        excluded_headers = ['connection', 'content-encoding', 'content-length', 'transfer-encoding']
        for key, value in response.headers.items():
            if key.lower() not in excluded_headers:
                proxy_response[key] = value

        return proxy_response

    except requests.exceptions.RequestException:
        return HttpResponse(status=502)