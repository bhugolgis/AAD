from django.shortcuts import render
from rest_framework import generics
from database.models import *
from .serializers import * 
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser



# Create your views here.
class GetPhleboFamilyMembersDetails(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = familyMembers.objects.filter( bloodCollectionLocation = "Center")
    serializer_class = GetPhleboFamilyMemberDetailSerializer  
    filter_backends = (filters.SearchFilter,)
    search_fields = ['familyHead__familyId' , 'familyHead__mobileNo' , 'familyHead__name'  ]


class PostBloodTestReport(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PostBloodTestReportSerialzier
    parser_classes = [MultiPartParser]

    def post(self , request):
        serializer = self.get_serializer(data = request.data)
        if serializer.is_valid():
            serializer.save(user = request.user)
            return Response({'status' : 'success' , 
                             'message' : 'data saved successfully'} , status= 200)
        else:
            return Response(serializer.errors , status= 400)