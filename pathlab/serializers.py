from rest_framework import serializers
from database.models import *

class GetPhleboFamilyMemberDetailSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = familyMembers
        fields = '__all__'


class PostBloodTestReportSerialzier(serializers.ModelSerializer):
    # barcodeNumber = serializers.CharField(max_length = 50 , required = False) 
    barcodeNumber =  serializers.ListField(child=serializers.CharField(max_length = 50 , required = False) , required = False )
    class Meta:
        model = phlebotomist
        fields = ('member','testReport', 'barcodeNumber', 'date')


    def create(self , data):
        TestTubes = data.pop('barcodeNumber')
        list = TestTubes[0].split(',')
        object = phlebotomist.objects.create(**data)
        for barcode in list:
            testtube_object = TestTube.objects.create( phlebo = object , barcodeNumber = barcode)
        return data

