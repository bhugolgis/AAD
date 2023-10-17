from django.urls import path , re_path
from .views import *
from . import views
from knox.views import LogoutView


urlpatterns = [
        path('CustomLoginAPI' , CustomLoginAPI.as_view() , name = 'CustomLoginAPI'),
        path('AddWardAPI', AddWardAPI.as_view(), name='AddWardAPI'),
        path('AddHealthPostAPI', AddHealthPostAPI.as_view(), name='AddHealthPostAPI'),
        path('AddsectionAPI', AddsectionAPI.as_view(), name='AddsectionAPI'),
        path('AddAreaAPI', AddAreaAPI.as_view(), name='AddAreaAPI'),
        path('login', LoginView.as_view(), name='login'),
        path('GetHealthPostAreas/<str:id>' , GetHealthPostAreasAPI.as_view() , name = 'GetHealthPostAreas'),
        re_path(r'^GetWardListAPI', GetWardListAPI.as_view(), name='GetWardListAPI'),
        re_path(r'^GethealthPostNameList', GethealthPostNameListAPI.as_view(), name='GethealthPostNameList'),
        re_path(r'^GetSectionListAPI', GetSectionListAPI.as_view(), name='GetSectionListAPI'),
        # path('InsertAmoAPI' , InsertAmoAPI.as_view() , name = 'InsertAmoAPI'),
        # path('InsertMoAPI' , InsertMoAPI.as_view() , name = 'InsertMoAPI'),

        path('InsertHealthWorkerAPI' , InsertHealthWorkerAPI.as_view() , name = 'InsertHealthWorkerAPI'),
        path('InsertPhlebotomistAPI' , InsertPhlebotomistAPI.as_view() , name = 'InsertPhlebotomistAPI'),
        path('usersList', UserGroupFilterView.as_view(), name='user-list'),
        path('SendOtp',views.SendOtp),
        path('CheckOtp',CheckOtp.as_view(),name="CheckOtp"),
        path('LoginWithOtp',LoginWithOtp.as_view(),name="LoginWithOtp"),
        path('changePassword', ChangePasswordView.as_view(), name='change-password'),
        path('logout', LogoutView.as_view(), name='knox_logout'),
       

        # path('dispensaries/', DispensaryListCreateView.as_view(), name='dispensary-list-create'),
        # path('dispensaries/<int:pk>/', DispensaryRetrieveUpdateDestroyView.as_view(), name='dispensary-retrieve-update-destroy'),
        # path('api/ward/', WardListCreateAPIView.as_view(), name='ward-list-create'),
        # path('api/ward/<int:pk>/', WardRetrieveUpdateDestroyAPIView.as_view(), name='ward-retrieve-update-destroy'),
        # path('api/healthpost/', HealthPostListCreateAPIView.as_view(), name='healthpost-list-create'),
        # path('api/healthpost/<int:pk>/', HealthPostRetrieveUpdateDestroyAPIView.as_view(), name='healthpost-retrieve-update-destroy'),
        # path('api/area/', AreaListCreateAPIView.as_view(), name='area-list-create'),
        # path('api/area/<int:pk>/', AreaRetrieveUpdateDestroyAPIView.as_view(), name='area-retrieve-update-destroy'),
        # path('api/section/', SectionListCreateAPIView.as_view(), name='section-list-create'),
        # path('api/section/<int:pk>/', SectionRetrieveUpdateDestroyAPIView.as_view(), name='section-retrieve-update-destroy'),





]