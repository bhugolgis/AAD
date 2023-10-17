from email.policy import default
from django.db import models
from django.contrib.gis.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager,PermissionsMixin ,AbstractBaseUser
from .managers import CustomUserManager
from django.utils.translation import gettext_lazy as _
from django.contrib.postgres.fields import ArrayField


class ward(models.Model):
    wardName = models.CharField(max_length=255 ,unique= True , blank = True , null = True)

    def __str__(self) -> str:
         return self.wardName

class healthPost(models.Model):
    ward = models.ForeignKey(ward , related_name="ward_name" , on_delete=models.SET_NULL , blank = True , null = True )
    healthPostName = models.CharField(max_length= 1000, unique= True ,  blank = True , null = True )

    def __str__(self) -> str:
         return self.healthPostName
    
class area(models.Model):
    healthPost = models.ForeignKey(healthPost , related_name="area_healthpost_name" , on_delete=models.SET_NULL , blank= True , null = True )
    areas = ArrayField(models.TextField(max_length=1000) , blank = True , null = True )


class section(models.Model):
    healthPost = models.ForeignKey(healthPost , related_name="healthPost_name" , on_delete=models.SET_NULL , blank = True , null = True )
    sectionName = models.CharField(max_length=255 , blank = True , null = True )

    def __str__(self) -> str:
         return self.sectionName
     
class Dispensary(models.Model):
    dispensaryname = models.CharField(max_length=255,blank=True,null=True,default="")
    location = models.CharField(max_length=255,blank=True,null=True,default="")
    contact_number = models.CharField(max_length=15,blank=True,null=True,default="")


    health_posts = models.ManyToManyField(healthPost, through='DispensaryHealthPostAssociation')

    def __str__(self):
        return self.name

class DispensaryHealthPostAssociation(models.Model):
    dispensary = models.ForeignKey(Dispensary, on_delete=models.CASCADE)
    health_post = models.ForeignKey(healthPost, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('dispensary', 'health_post')

    def __str__(self):
        return f"{self.dispensary} - {self.health_post}"

# class dispensary(models.Model):
#     disphealthPost = models.ForeignKey(healthPost , related_name="disp_healthpost_name" , on_delete=models.SET_NULL , blank= True , null = True )
#     dispensaryName = models.CharField(max_length=255 , blank = True , null = True )


    


    
class CustomUser(AbstractUser, PermissionsMixin):
    name=models.CharField(max_length=300,blank=True,null=True)
    username=models.CharField(max_length=255,unique=True)
    emailId=models.EmailField(max_length=255,blank=True,null=True)
    phoneNumber=models.CharField(max_length=20,blank=True,null=True , unique = True )
    otpChecked = models.BooleanField(default=False)
    supervisor = models.ForeignKey('CustomUser',related_name="supervisorId",on_delete=models.CASCADE,null=True,blank=True)
    section = models.ForeignKey(section , related_name="section_name" , on_delete=models.SET_NULL , blank = True , null = True )
    ward = models.ForeignKey(ward , related_name="wardAmo_mo_name" , on_delete=models.SET_NULL , blank = True , null = True )
    health_Post = models.ForeignKey(healthPost , related_name="healthpostAmo_mo_name" , on_delete=models.SET_NULL , blank = True , null = True )
    area = models.ForeignKey(area , related_name="areaAmo_mo_name" , on_delete=models.SET_NULL , blank = True , null = True )
    dispensary = models.ForeignKey(Dispensary , related_name="dispensary_name" , on_delete=models.SET_NULL , blank = True , null = True )

    USERNAME_FIELD = 'phoneNumber'
    REQUIRED_FIELDS = []
 
        
    objects = CustomUserManager()

    def __str__(self) -> str:
         return self.username



class sendOtp(models.Model):
    registerUser = models.ForeignKey(CustomUser,related_name="Registeruser",on_delete=models.CASCADE,null=True,blank=True)
    otp = models.CharField(max_length=6,blank=True,null=True)
    otpVerified = models.BooleanField(default=False)
    createdDate = models.DateTimeField(auto_now_add=True)
    expireyDate = models.DateTimeField(blank=True,null=True)



class familyHeadDetails(models.Model):

    familyId = models.CharField(max_length=150,blank=True,null=True , unique= True)
    name = models.CharField(max_length=255 , blank= True , null = True)
    mobileNo = models.BigIntegerField(unique= True , blank=True,null=True)
    plotNo = models.CharField(max_length=50 , blank= True , null= True)
    address = models.CharField(max_length=500,blank=True,null=True)
    # addressLine2 = models.CharField(max_length=500,blank=True,null=True)
    pincode = models.IntegerField(blank=True,null=True)
    area = models.CharField(max_length=255 ,blank= True , null= True )
    totalFamilyMembers = models.IntegerField(default=0)
    location = models.PointField(blank= True , null= True )
    created_datetime = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(CustomUser,related_name="surveyDoneBy", on_delete=models.CASCADE,null=True,blank=True)
    partialSubmit = models.BooleanField(default= False)
    created_date= models.DateTimeField(auto_now_add= True )
    isLabTestAdded = models.BooleanField(default=False)
    isSampleCollected = models.BooleanField(default=False)
    isLabTestReportGenerated = models.BooleanField(default=False)

   
    


class familyMembers(models.Model):
    bloodCollectionLocation_choices = [
         ("Home" , "Home"),
         ("Center" , "Center") ,
         ("Denied" , "Denied"),
    ]
    # user = models.ForeignKey(CustomUser , related_name="updatefamilysurveyor",on_delete=models.CASCADE,null=True,blank=True )
    memberId = models.CharField(max_length=255 , blank = True , null = True )
    name = models.CharField(max_length=900,blank=True,null=True)
    gender = models.CharField(max_length=15,blank=True,null=True)
    age  = models.IntegerField(blank = True , null = True)
    mobileNo  = models.BigIntegerField(blank = True , null = True)
    familyHead = models.ForeignKey(familyHeadDetails,related_name="family_head_member",on_delete=models.CASCADE,null=True,blank=True)
    familySurveyor = models.ForeignKey(CustomUser,related_name="familysurveyor",on_delete=models.CASCADE,null=True,blank=True)
    aadharCard = models.BigIntegerField(blank = True , null = True)
    abhaId = models.CharField(max_length=100 , blank= True , null = True )
    pulse = models.CharField(max_length=50 , blank = True , null = True)
    bloodPressure = models.CharField(max_length=50 , blank = True , null = True)
    weight = models.CharField(max_length=50 , blank = True , null = True)
    height = models.CharField(max_length=50 , blank = True , null = True)
    BMI = models.CharField(max_length=50 , blank = True , null = True)
    Questionnaire = models.JSONField(blank= True , null = True)
    bloodCollectionLocation = models.CharField(max_length= 20 , choices= bloodCollectionLocation_choices , blank= True , null = True  )
    questionsConsent = models.BooleanField(default= False)
    aadharAndAbhaConsent = models.BooleanField(default= False)
    demandLetter = models.ImageField(upload_to='demand letter' , blank = True , null = True )
    bloodConsent = models.BooleanField(default= False)
    cbacScore = models.IntegerField(default=0)
    created_date= models.DateTimeField(auto_now= True)
    isLabTestAdded = models.BooleanField(default=False)
    isSampleCollected = models.BooleanField(default=False)
    isLabTestReportGenerated = models.BooleanField(default=False)


class phlebotomist(models.Model):
    testChoices = [
         ('HB' , 'HB') , 
         ('CBC' , 'CBC') , 
         ('Platelet Count' , 'Platelet Count') , 
         ('PT/INR' , 'PT/INR') , 
         ('RBS' , 'RBS') , 
         ('S. Total Bilirubin' , 'S. Total BilirubinB') , 
         ('S. Direct Bilirubin' , 'S. Direct Bilirubin') , 
         ('SGPT/ALT' , 'SGPT/ALT') , 
         ('SGOT/AST' , 'SGOT/AST') , 
         ('Urea / BUN' , 'Urea / BUN') , 
         ('S. Creatinine' , 'S. Creatinine') , 
         ('ALP' , 'ALP') , 
         ('S. Total Proteins' , 'S. Total Proteins') , 
         ('S. Albumin' , 'S. Albumin') , 
         ('S. Total Calcium' , 'S. Total Calcium') , 
         ('S. Uric Acid' , 'S. Uric Acid') , 
         ('S. Cholesterol' , 'S. Cholesterol') , 
         ('S. Triglycerides ' , 'S. Triglycerides ') , 
         ('S. HDL (Direct)' , 'S. HDL (Direct)') , 
         ('LDL' , 'LDL') , 
         ('VLDL' , 'VLDL') , 
         ('Amylase' , 'Amylase') , 
         ('T3' , 'T3') , 
         ('T4' , 'T4') , 
         ('HbA1C' , 'HbA1C') , 
         ('S. Electrolytes' , 'S. Electrolytes') , 
         ('S. TIBC' , 'S. TIBC') , 
         ('LDH' , 'LDH') , 
         ('Vit. D' , 'Vit. D') , 
         ('Vit. B12' , 'Vit. B12') , 
         ('Immunoassays' , 'Immunoassays') ,]
    user = models.ForeignKey(CustomUser , related_name='phlebotomist_user' , on_delete=models.SET_NULL ,  blank = True , null = True  )
    member = models.ForeignKey(familyMembers , related_name='family_Member' ,on_delete=models.SET_NULL , blank = True , null = True )
    testReport = ArrayField(models.CharField(max_length=255 , choices=testChoices , blank = True , null = True ))
    # barcodeNumber =ArrayField( models.CharField(max_length=100 , blank = True , null = True ))
    date = models.DateField(blank = True , null = True )


class TestTube(models.Model):
    phlebo = models.ForeignKey(phlebotomist , related_name='phlebo_details' , on_delete=models.SET_NULL , blank = True , null = True)
    barcodeNumber = models.CharField(max_length=50 , blank = True , null = True)
   

    
# class PatientsPathlab(models.Model):  
class PatientPathlab(models.Model): 
    testChoices = [
         ('HB' , 'HB') , 
         ('CBC' , 'CBC') , 
         ('Platelet Count' , 'Platelet Count') , 
         ('PT/INR' , 'PT/INR') , 
         ('RBS' , 'RBS') , 
         ('S. Total Bilirubin' , 'S. Total BilirubinB') , 
         ('S. Direct Bilirubin' , 'S. Direct Bilirubin') , 
         ('SGPT/ALT' , 'SGPT/ALT') , 
         ('SGOT/AST' , 'SGOT/AST') , 
         ('Urea / BUN' , 'Urea / BUN') , 
         ('S. Creatinine' , 'S. Creatinine') , 
         ('ALP' , 'ALP') , 
         ('S. Total Proteins' , 'S. Total Proteins') , 
         ('S. Albumin' , 'S. Albumin') , 
         ('S. Total Calcium' , 'S. Total Calcium') , 
         ('S. Uric Acid' , 'S. Uric Acid') , 
         ('S. Cholesterol' , 'S. Cholesterol') , 
         ('S. Triglycerides ' , 'S. Triglycerides ') , 
         ('S. HDL (Direct)' , 'S. HDL (Direct)') , 
         ('LDL' , 'LDL') , 
         ('VLDL' , 'VLDL') , 
         ('Amylase' , 'Amylase') , 
         ('T3' , 'T3') , 
         ('T4' , 'T4') , 
         ('HbA1C' , 'HbA1C') , 
         ('S. Electrolytes' , 'S. Electrolytes') , 
         ('S. TIBC' , 'S. TIBC') , 
         ('LDH' , 'LDH') , 
         ('Vit. D' , 'Vit. D') , 
         ('Vit. B12' , 'Vit. B12') , 
         ('Immunoassays' , 'Immunoassays') ,]
    
    patientFamilyMember = models.ForeignKey(familyMembers , related_name='patientFamilyMember' ,on_delete=models.SET_NULL , blank = True , null = True )
    suggested_by_doctor = models.ForeignKey(CustomUser , related_name='suggested_by_doctor' , on_delete=models.SET_NULL ,  blank = True , null = True  )
    suggested_date = models.DateTimeField(auto_now=True)
    LabTestSuggested = ArrayField(models.CharField(max_length=255 , choices=testChoices ,default=list ) , blank = True , null = True )
    PatientSampleTaken = models.BooleanField(default=False)

    # pathLabPatient = models.ForeignKey(CustomUser,related_name="phlebotomist_user",on_delete=models.CASCADE,null=True,blank=True)
    PathLab = models.ForeignKey(CustomUser,related_name="PathLab",on_delete=models.CASCADE,null=True,blank=True)
    ReportCheckByDoctor = models.ForeignKey(CustomUser,related_name="ReportCheckByDoctor",on_delete=models.CASCADE,null=True,blank=True)
    LabTestReport = models.JSONField(default = dict,null=True,blank=True)
    doctorRemarks = models.CharField(max_length=500,blank=True,null=True)
    PathLabRemarks = models.CharField(max_length=500,blank=True,null=True)
    response_date = models.DateTimeField(blank=True,null=True)
    created_date = models.DateTimeField(auto_now=True)
    isCompleted = models.BooleanField(default=False)
    CentreID = models.CharField(max_length=255 , blank = True, null=True )
    bookingVisitID = models.CharField(max_length=255 , blank = True, null=True )
    puid =models.CharField(max_length=255 , blank = True, null=True )
    patientID =models.CharField(max_length=255 , blank = True, null=True )
    citizenRejectedLabTest = models.BooleanField(default=False)



class AmoConsultancy(models.Model):
    #patientLabTest to patientTest
    AmoPatientsPathReport = models.ForeignKey(PatientPathlab,related_name="AmoPatientsPathReport",on_delete=models.CASCADE,null=True,blank=True)
    AmoPatientsConsultancy = models.ForeignKey(familyMembers,related_name="AmoPatientsConsultancy",on_delete=models.CASCADE,null=True,blank=True)
    AmoassignedDoctor = models.ForeignKey(CustomUser,related_name="AmoassignedDoctor",on_delete=models.CASCADE,null=True,blank=True)
    Amodoctor_name = models.CharField(max_length=500,blank=True,null=True) 
    Amospecialization = models.CharField(max_length=500,blank=True,null=True)
    AmodoctorRemarks = models.CharField(max_length=500,blank=True,null=True)
    AmofileUpload = models.FileField(upload_to='doctorFolder',blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    isCompleted = models.BooleanField(default=False)


class PrimaryConsultancy(models.Model):
    #patientLabTest to patientTest
    PriPatientsPathReport = models.ForeignKey(PatientPathlab,related_name="PriPatientsPathReport",on_delete=models.CASCADE,null=True,blank=True)
    PriPatientsConsultancy = models.ForeignKey(familyMembers,related_name="PriPatientsConsultancy",on_delete=models.CASCADE,null=True,blank=True)
    PriassignedDoctor = models.ForeignKey(CustomUser,related_name="PriassignedDoctor",on_delete=models.CASCADE,null=True,blank=True)
    PriDoctor_name = models.CharField(max_length=500,blank=True,null=True) 
    Prispecialization = models.CharField(max_length=500,blank=True,null=True)
    PridoctorRemarks = models.CharField(max_length=500,blank=True,null=True)
    fileUpload = models.FileField(upload_to='doctorFolder',blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    isCompleted = models.BooleanField(default=False)

class SecondaryConsultancy(models.Model):
    #patientLabTest to patientTest
    SecPatientsPathReport = models.ForeignKey(PatientPathlab,related_name="SecPatientsPathReport",on_delete=models.CASCADE,null=True,blank=True)
    SecPatientsConsultancy = models.ForeignKey(familyMembers,related_name="SecPatientsConsultancy",on_delete=models.CASCADE,null=True,blank=True)
    SecSecassignedDoctor = models.ForeignKey(CustomUser,related_name="SecassignedDoctor",on_delete=models.CASCADE,null=True,blank=True)
    Secdoctor_name = models.CharField(max_length=500,blank=True,null=True) 
    Secspecialization = models.CharField(max_length=500,blank=True,null=True)
    SecdoctorRemarks = models.CharField(max_length=500,blank=True,null=True)
    SecfileUpload = models.FileField(upload_to='doctorFolder',blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    isCompleted = models.BooleanField(default=False)

class TertiaryConsultancy(models.Model):
    #patientLabTest to patientTest
    TerPatientsPathReport = models.ForeignKey(PatientPathlab,related_name="TerPatientsPathReport",on_delete=models.CASCADE,null=True,blank=True)
    TerPatientsConsultancy = models.ForeignKey(familyMembers,related_name="TerPatientsConsultancy",on_delete=models.CASCADE,null=True,blank=True)
    TerassignedDoctor = models.ForeignKey(CustomUser,related_name="TerassignedDoctor",on_delete=models.CASCADE,null=True,blank=True)
    Terdoctor_name = models.CharField(max_length=500,blank=True,null=True) 
    Terspecialization = models.CharField(max_length=500,blank=True,null=True)
    TerdoctorRemarks = models.CharField(max_length=500,blank=True,null=True)
    fileUpload = models.FileField(upload_to='doctorFolder',blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    isCompleted = models.BooleanField(default=False)




