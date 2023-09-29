from rest_framework import serializers
from database.models import *

class GetPhleboFamilyMemberDetailSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = familyMembers
        fields = '__all__'


class PostBloodTestReportSerialzier(serializers.ModelSerializer):
    class Meta:
        model = phlebotomist
        fields = ('member','testReport', 'barcodeNumber', 'date')

