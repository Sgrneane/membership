from django.db import models
from account.models import CustomUser
from django.utils import timezone
from datetime import timedelta
from model_utils.managers import InheritanceManager
from .import choices
from django.core.exceptions import ValidationError


# Create your models here.

class ActionLog(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    action = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.email} - {self.action} - {self.timestamp}"

class PersonalInfo(models.Model):
    name_of_applicant = models.CharField(max_length=200)
    gender = models.CharField(max_length=1, choices=choices.GENDER_CHOICES)
    affiliation = models.CharField(max_length=200)
    pp_photo = models.ImageField(upload_to="personal_photo")
    salutation = models.CharField(max_length=20, blank=True, null=True)
    phone_number = models.CharField(max_length=20,null=True)
    class Meta:
        abstract = True

class NationalDocumment(models.Model):
    identity_card_no = models.CharField(max_length=80)
    dob = models.DateField()
    nationality = models.CharField(max_length=2, choices=choices.COUNTRY_CHOICES)
    identity_issued_from = models.CharField(max_length=150)
    permanent_address = models.CharField(max_length=200)
    identity_card_image = models.FileField(upload_to="identity_card_documents")

class EducationalDocuments(models.Model):
    degree_type =models.CharField(max_length=3,choices=choices.DEGREE_TYPES)
    course = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    university =models.CharField(max_length=200,null=True)
    country = models.CharField(max_length=2, choices=choices.COUNTRY_CHOICES)
    passed_year = models.CharField(max_length=4)
    work_experience = models.TextField()
    educational_document = models.FileField(upload_to="educational_document",null=True)

class Membership(models.Model):
    membership_number=models.CharField(max_length=10,unique=True,null=True)
    associated_user = models.OneToOneField(CustomUser,related_name='membership',on_delete=models.CASCADE,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    verification = models.BooleanField(default=False)
    expiry_date = models.DateField(null=True,blank=True)
    membership_since = models.CharField(max_length=4, blank=True, null=True)
    verified_date = models.DateTimeField(blank=True, null=True)
    rejected = models.BooleanField(default=False)
    expiry_status=models.BooleanField(default=False)
    membership_type=models.PositiveIntegerField(choices=choices.MEMBERSHIP_TYPES,default=1)
    remarks = models.TextField(null=True)
    objects = InheritanceManager()
    # To save Expiry Date 
    
    def save(self, *args, **kwargs):
        if self.created_at is None:
            self.created_at = timezone.now()

        if self.membership_type == 3:
            self.expiry_date = None
        elif not self.expiry_date:
            self.expiry_date = self.created_at + timedelta(days=365)

        # if not self.membership_number:
        #     membership_count = Membership.objects.count() + 1
        #     self.membership_number = f'NGS{membership_count:03}'

        super(Membership, self).save(*args, **kwargs)
    
    class Meta:
        ordering = ['-created_at']
        
    def __str__(self):
        return self.get_membership_type_display()

#Gemeral Memberships
class GeneralMembership(Membership,PersonalInfo):
    #Educational Information
    nationaldocument =models.OneToOneField(NationalDocumment,on_delete=models.CASCADE, related_name="associated_membership",related_query_name="associated_membership",null=True)
    educational_information = models.OneToOneField(EducationalDocuments,on_delete=models.CASCADE,related_name="edu_members",null=True)
    upgrade_request = models.BooleanField(null=True)
    upgrade_membership_type = models.PositiveIntegerField(choices=choices.MEMBERSHIP_TYPES,null=True)
    upgrade_payment = models.BooleanField(default=False)
    renew_request =models.BooleanField(null=True, default=False)
    renew_payment = models.BooleanField(default=False)

    def __str__(self):
        return self.associated_user.first_name
    @property
    def email(self):
        return self.associated_user.email
    
class InstitutionalMembership(Membership):
    company_name = models.CharField(max_length=200)
    company_address = models.CharField(max_length=200)
    registration_no = models.CharField(max_length=200)
    pan_document = models.FileField(upload_to="institutional_documents",null=True)
    registration_document = models.FileField(upload_to="institutional_documents",null=True)
    working_field = models.CharField(max_length=200,null=True)
    contact_person = models.CharField(max_length=200,null=True)
    contact_number = models.CharField(max_length=10,null=True)
    website = models.CharField(max_length=250,null=True)
    logo = models.ImageField(upload_to="institutional_documents",null=True)
    def __str__(self):
        return self.company_name
  
    
class Payment(models.Model):
    """To hold payment record of users."""
    created_at = models.DateTimeField()
    created_by = models.ForeignKey(CustomUser,on_delete=models.SET_NULL,related_name="paid_payment",null=True)
    member = models.ForeignKey(
        Membership, on_delete=models.CASCADE, related_name="payment",)
    paid = models.BooleanField(default=True)
    payment_ss = models.FileField(upload_to="payment",null=True)
    paid_amount_in_paisa = models.CharField(max_length=15, blank=True, null=True)
    pidx = models.CharField(max_length=250, blank=True, null=True)
    txn_id = models.CharField(max_length=250, blank=True, null=True)
    paypal_payer_id = models.CharField(max_length=250, blank=True, null=True)

    # def __str__(self):
    #     return self.paid_payment.first_name

    @property
    def amount_in_rs(self):
        """Converts amount which is in paisa to rs in npr."""
        if self.paid_amount_in_paisa is not None and self.paid_amount_in_paisa != "":
            amount_int = int(self.paid_amount_in_paisa)
            rs = amount_int / 100
            return str(int(rs))
        
class FAQ(models.Model):
    question=models.TextField()
    answer=models.TextField()

