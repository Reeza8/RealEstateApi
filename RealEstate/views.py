from rest_framework.generics import ListAPIView, RetrieveDestroyAPIView, RetrieveUpdateAPIView
from .serializer import *
from .models import *


class EstateList(ListAPIView):
	queryset = Estate.objects.all()
	serializer_class = EstateSerializer


class FileList(ListAPIView):
	queryset = File.objects.all()
	serializer_class = FileSerializer


class ConsultantList(ListAPIView):
	queryset = Consultant.objects.all()
	serializer_class = ConsultantSerializer


class ConsultantUpdateList(RetrieveUpdateAPIView):
	queryset = Consultant.objects.all()
	serializer_class = ConsultantSerializer


