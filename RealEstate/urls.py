from django.urls import path
from .views import *

urlpatterns = [
	path("", EstateList.as_view()),
	path("files/", FileList.as_view()),
	path("upload/files/<int:pk>/", UploadImageFile.as_view()),

	path("estate/consulant/", ConsultantList.as_view()),
	path("consultant/update/<int:pk>/", ConsultantUpdateList.as_view())

]

def update_filename(instance, filename):
    path = "upload/path/"
    format = instance.userid + instance.transaction_uuid + instance.file_extension
    return os.path.join(path, format)
