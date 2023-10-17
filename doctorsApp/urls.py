from django.urls import path
from doctorsApp.views import *
from . import views
urlpatterns = [
    path('labtestsuggested/', LabTestSuggestedCreateView.as_view(), name='lab-test-suggested-create'),
    path('listpatientspathlab/', ListPatientsPathlabView.as_view(), name='list-patients-pathlab'),
    path('FamilyHeadList/', views.FamilyHeadList),
    path('ViewFamilyDetails/<str:pk>', views.ViewFamilyDetails),



    # Add other URLs as needed
]