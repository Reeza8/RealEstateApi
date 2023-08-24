from rest_framework import serializers
from .models import *


class FileSerializer(serializers.ModelSerializer):

    class Meta:
        model = File
        fields = "__all__"


class ConsultantSerializer(serializers.ModelSerializer):

    class Meta:
        model = Consultant
        fields = "__all__"

    def validate_files(self, value):

        string=''
        if len(value) > 1:
            consultants = Consultant.objects.all().order_by('-created_date')
            string = []
            for c in consultants:
                files = File.objects.filter(consultant=c)
                if not files:
                    string.append(c.name)

            raise serializers.ValidationError("suggested consultants are {}".format(string))
        return value


class EstateSerializer(serializers.ModelSerializer):
    def get_Consultants(self, obj):
        consultants = Consultant.objects.filter(estate=obj.id)
        filename = []
        cons_name = []
        final = []
        for consultant in consultants:
            files = File.objects.filter(consultant=consultant.id)
            cons_name.append(consultant.name)
            for file in files:
                filename.append(file.name)
            dd = {"name": cons_name, "file name": filename}
            final.append(dd)
            dd = []
            filename = []
            cons_name = []
        return final

    Consultants = serializers.SerializerMethodField("get_Consultants")

    class Meta:
        model = Estate
        fields = "__all__"


