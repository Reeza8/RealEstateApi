from django.urls import path
from .views import *

urlpatterns = [
	path("", EstateList.as_view()),
	path("files/", FileList.as_view()),
	path("estate/consulant/", ConsultantList.as_view()),
	path("consultant/update/<int:pk>/", ConsultantUpdateList.as_view())

]


