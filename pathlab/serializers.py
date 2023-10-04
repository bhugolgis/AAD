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
        TestTubes = list(data.pop('barcodeNumber'))
        object = phlebotomist.objects.create(**data)
        for barcode in TestTubes:
            print(barcode)
            testtube_object = TestTube.objects.create( phlebo = object , barcodeNumber = barcode)

        return data

