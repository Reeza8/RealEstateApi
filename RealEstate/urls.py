from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.SimpleRouter()
router.register('files', FileView, basename='files')
router.register('estates', EstateView, basename='estates')
router.register('consultant', ConsultantView, basename='consultant')

urlpatterns = [
	path("", include(router.urls)),
]

def update_filename(instance, filename):
	path = "upload/path/"
	format = instance.userid + instance.transaction_uuid + instance.file_extension
	return os.path.join(path, format)
