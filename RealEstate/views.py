from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView
from .serializer import *
from .models import *
import jwt
from RealEstateApi.settings import SECRET_KEY
from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


# Check the access of user from token claims
def permissions(request, UserWithAccess):
	token_str = str(request.auth)
	token_byte = bytes(token_str, 'utf-8')
	dic = jwt.decode(token_byte, SECRET_KEY, algorithms=["HS256"])

	if dic['type'] is not UserWithAccess or dic['type'] is not 'admin':
		raise Exception(f"{UserWithAccess} have access to this data")



class EstateView(viewsets.ViewSet):
	def list(self, request):
		permissions(request, 'Estate owners')
		queryset = Estate.objects.all()
		serializer = EstateSerializer(queryset, many=True)
		return Response(serializer.data)


class FileView(viewsets.ViewSet):
	queryset = File.objects.all()
	serializer_class = FileSerializer

	def list(self, request):
		queryset = File.objects.all()
		serializer = FileSerializer(queryset, many=True)
		return Response(serializer.data)

	def retrieve(self, request, pk=None):
		queryset = File.objects.all()
		file = get_object_or_404(queryset, pk=pk)
		serializer = FileSerializer(file)
		return Response(serializer.data)

	def update(self, request, pk=None):
		queryset = File.objects.all()
		serializer = FileSerializer(queryset)
		return Response(serializer.data)


class ConsultantView(viewsets.ViewSet):

	def list(self, request):
		permissions(request, 'Consultants')
		queryset = Consultant.objects.all()
		serializer = ConsultantSerializer(queryset, many=True)
		return Response(serializer.data)

	def retrieve(self, request, pk=None):
		permissions(request, 'Consultants')
		queryset = Consultant.objects.all()
		consultant = get_object_or_404(queryset, pk=pk)
		serializer = ConsultantSerializer(consultant)
		return Response(serializer.data)

	def update(self, request, pk=None):
		permissions(request, "Estate owners")
		queryset = Consultant.objects.all()
		serializer = ConsultantSerializer(queryset)
		return Response(serializer.data)



