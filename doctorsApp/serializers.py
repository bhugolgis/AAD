from rest_framework import serializers
from database.models import *

class PatientsPathlabSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientPathlab
        fields = ['patientFamilyMember','LabTestSuggested']
        

class ViewPatientsPathlabSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientPathlab  
        fields = "__all__"      
        

class ViewAmoConsultancySerializer(serializers.ModelSerializer):
    class Meta:
        model = AmoConsultancy  
        fields = "__all__" 


class ViewPrimaryConsultancySerializer(serializers.ModelSerializer):
    class Meta:
        model = PrimaryConsultancy  
        fields = "__all__"  
        
class ViewSecondaryConsultancySerializer(serializers.ModelSerializer):
    class Meta:
        model = SecondaryConsultancy  
        fields = "__all__"  
        
class ViewTertiaryConsultancySerializer(serializers.ModelSerializer):
    class Meta:
        model = TertiaryConsultancy  
        fields = "__all__"  

# class ListPatientsPathlabSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = PatientsPathlab
#         fields = ['patientFamilyMember_id','LabTestSuggested','suggested_by_doctor_id','patientFamilyMember__familyHead__area','patientFamilyMember__familyHead__pincode','patientFamilyMember__familyHead__address','patientFamilyMember__familyHead__plotNo']


class ListPatientsPathlabSerializer(serializers.ModelSerializer):
    patientFamilyMember_area = serializers.CharField(source='patientFamilyMember.family_head_member.area', read_only=True)
    patientFamilyMember_pincode = serializers.IntegerField(source='patientFamilyMember.family_head_member.pincode', read_only=True)
    patientFamilyMember_address = serializers.CharField(source='patientFamilyMember.family_head_member.address', read_only=True)
    patientFamilyMember_plotNo = serializers.CharField(source='patientFamilyMember.family_head_member.plotNo', read_only=True)

    class Meta:
        model = PatientPathlab
        fields = [
            'patientFamilyMember_id',
            'LabTestSuggested',
            'suggested_by_doctor_id',
            'patientFamilyMember_area',
            'patientFamilyMember_pincode',
            'patientFamilyMember_address',
            'patientFamilyMember_plotNo',
        ]


class PatientPathlabSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientPathlab
        fields = '__all__'

class AmoConsultancySerializer(serializers.ModelSerializer):
    class Meta:
        model = AmoConsultancy
        fields = '__all__'

class PrimaryConsultancySerializer(serializers.ModelSerializer):
    class Meta:
        model = PrimaryConsultancy
        fields = '__all__'

class SecondaryConsultancySerializer(serializers.ModelSerializer):
    class Meta:
        model = SecondaryConsultancy
        fields = '__all__'

class TertiaryConsultancySerializer(serializers.ModelSerializer):
    class Meta:
        model = TertiaryConsultancy
        fields = '__all__'

class FamilyMemberDetailsSerializer(serializers.ModelSerializer):
    pathlab_reports = PatientPathlabSerializer(many=True, read_only=True)
    amo_consultancy = AmoConsultancySerializer(many=True, read_only=True)
    primary_consultancy = PrimaryConsultancySerializer(many=True, read_only=True)
    secondary_consultancy = SecondaryConsultancySerializer(many=True, read_only=True)
    tertiary_consultancy = TertiaryConsultancySerializer(many=True, read_only=True)

    class Meta:
        model = familyMembers
        fields = '__all__'

class FamilyHeadDetailsSerializer(serializers.ModelSerializer):
    family_head_member = FamilyMemberDetailsSerializer(many=True, read_only=True)


    class Meta:
        model = familyHeadDetails
        fields = '__all__'
        


class ListFamilyHeadDetailsSerializer(serializers.ModelSerializer):
    # family_head_member = FamilyMemberDetailsSerializer(many=True, read_only=True)


    class Meta:
        model = familyHeadDetails
        fields = '__all__'