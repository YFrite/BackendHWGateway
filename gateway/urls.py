from django.urls import path
from . import views


urlpatterns = [
	path("/", views.gateway_view),
	path("/<path:path>", views.gateway_view),
]