from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView
from .serializer import *
from .models import *
import jwt
from RealEstateApi.settings import SECRET_KEY


class EstateList(ListAPIView):
	queryset = Estate.objects.all()
	serializer_class = EstateSerializer

	def get(self, request, *args, **kwargs):
		aa = str(request.auth)
		arr = bytes(aa, 'utf-8')
		dic = jwt.decode(arr, SECRET_KEY, algorithms=["HS256"])
		if not dic['type'] == 'EstateOwner':
			raise Exception("Estate owners have access to this data")
		return self.list(request, *args, **kwargs)


class FileList(ListAPIView):
	queryset = File.objects.all()
	serializer_class = FileSerializer

	def get(self, request, *args, **kwargs):
		aa = str(request.auth)
		arr = bytes(aa, 'utf-8')
		dic = jwt.decode(arr, SECRET_KEY, algorithms=["HS256"])
		if not (dic['type'] == 'EstateOwner' or dic['type'] == 'Consultant'):
			raise Exception("Estate owners have access to this data")
		return self.list(request, *args, **kwargs)


class ConsultantList(ListAPIView):
	queryset = Consultant.objects.all()
	serializer_class = ConsultantSerializer

	def get(self, request, *args, **kwargs):
		aa = str(request.auth)
		arr = bytes(aa, 'utf-8')
		dic = jwt.decode(arr, SECRET_KEY, algorithms=["HS256"])
		if not dic['type'] == 'Consultant':
			raise Exception("Consultant have access to this data")
		return self.list(request, *args, **kwargs)


class ConsultantUpdateList(RetrieveUpdateAPIView):
	queryset = Consultant.objects.all()
	serializer_class = ConsultantSerializer

	def get(self, request, *args, **kwargs):
		aa = str(request.auth)
		arr = bytes(aa, 'utf-8')
		dic = jwt.decode(arr, SECRET_KEY, algorithms=["HS256"])
		if not dic['type'] == 'Consultant':
			raise Exception("Consultant have access to this data")
		return self.retrieve(request, *args, **kwargs)






