from django.urls import path
from .views import *

urlpatterns = [
        path('GetPhleboFamilyMembersDetails' , GetPhleboFamilyMembersDetails.as_view() , name = 'GetPhleboFamilyMembersDetails'),
        path('PostBloodTestReport' , PostBloodTestReport.as_view() , name = 'PostBloodTestReport'),
]