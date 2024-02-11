from django import forms
from .models import StudentMembership,GeneralMembership,InstitutionalMembership,EducationalDocuments, Payment,FAQ
from django.contrib.auth.hashers import make_password
from . import choices
from datetime import date, timedelta


class PersonalInfoForm(forms.Form):
    salutation = forms.ChoiceField(choices=choices.SALUTATION_CHOICES)
    name_of_applicant = forms.CharField(
        max_length=200,
        error_messages={
            'required': 'Please enter name of applicant.',
        })
   
    gender = forms.ChoiceField( choices=choices.GENDER_CHOICES)

    affiliation = forms.CharField(max_length=200,required=False)
    phone_number = forms.CharField(max_length=15)
   
    pp_photo = forms.ImageField(error_messages={
        'required':'Please upload Passport size photo'
    })
    def clean_pp_photo(self):
        pp_photo = self.cleaned_data.get('pp_photo')
        max_size = 1*1024*1024
        if pp_photo and (pp_photo.size>max_size):
            raise forms.ValidationError("Please upload photo less than 1 MB.")

        return pp_photo

class EditPersonalInfoForm(forms.Form):
    salutation = forms.ChoiceField(choices=choices.SALUTATION_CHOICES)
    name_of_applicant = forms.CharField(
        max_length=200,
        error_messages={
            'required': 'Please enter name of applicant.',
        })
   
    gender = forms.ChoiceField( choices=choices.GENDER_CHOICES)

    affiliation = forms.CharField(max_length=200,required=False)
    phone_number = forms.CharField(max_length=15)
   
    pp_photo = forms.ImageField(required=False)
    def clean_pp_photo(self):
        pp_photo = self.cleaned_data.get('pp_photo')
        max_size = 1*1024*1024
        if pp_photo and (pp_photo.size>max_size):
            raise forms.ValidationError("Please upload photo less than 1 MB.")

        return pp_photo
class NationalDocumentForm(forms.Form):
    nationality = forms.ChoiceField(choices=choices.COUNTRY_CHOICES)
    identity_card_no = forms.CharField(max_length=80)
    identity_issued_from = forms.CharField(max_length=150)
    permanent_address = forms.CharField(max_length=200)
    dob = forms.DateField(error_messages={
                           'required': 'Date of Birth is required.'
                         })
    identity_card_image = forms.FileField(error_messages={
        'required':'Please upload valid identity card'
    })
    
    def clean_dob(self):
        dob = self.cleaned_data.get('dob')
        if dob:
            # Calculate the date 10 years ago
            ten_years_ago = date.today() - timedelta(days=365 * 10)
            # Compare the date of birth with 10 years ago
            if dob > ten_years_ago:
                raise forms.ValidationError('You must be at least 10 years old to apply for membership')
        return dob.strftime('%Y-%m-%d') if dob else None

class EditNationalDocumentForm(forms.Form):
    nationality = forms.ChoiceField(choices=choices.COUNTRY_CHOICES)
    identity_card_no = forms.CharField(max_length=80)
    identity_issued_from = forms.CharField(max_length=150)
    permanent_address = forms.CharField(max_length=200)
    dob = forms.DateField(error_messages={
                           'required': 'Date of Birth is required.'
                         })
    identity_card_image = forms.FileField(required=False)
    def clean_dob(self):
        dob = self.cleaned_data.get('dob')
        if dob:
            # Calculate the date 10 years ago
            ten_years_ago = date.today() - timedelta(days=365 * 10)
            # Compare the date of birth with 10 years ago
            if dob > ten_years_ago:
                raise forms.ValidationError('You must be at least 10 years old to apply for membership')
        return dob.strftime('%Y-%m-%d') if dob else None
class EducationalForm(forms.Form):
    degree_type = forms.ChoiceField(choices=choices.DEGREE_TYPES)
    course = forms.CharField(max_length=200,
                            error_messages={
                               'required': 'Please enter name of applicant.',
                            })
    institution = forms.CharField(max_length=200,required=False)
    university = forms.CharField(max_length=200,
                                            error_messages={
                                                    'required': 'Bachelor University is mandatory.',
                                                })
    country = forms.ChoiceField(choices=choices.COUNTRY_CHOICES)
    passed_year = forms.CharField(max_length=4)
    educational_document = forms.FileField(error_messages={
        'required':'Please upload latest educational document'
    })

    work_experience = forms.CharField(widget=forms.Textarea,required=False)

class EditEducationalForm(forms.Form):
    degree_type = forms.ChoiceField(choices=choices.DEGREE_TYPES)
    course = forms.CharField(max_length=200,
                            error_messages={
                               'required': 'Please enter name of applicant.',
                            })
    institution = forms.CharField(max_length=200,required=False)
    university = forms.CharField(max_length=200,
                                            error_messages={
                                                    'required': 'Bachelor University is mandatory.',
                                                })
    country = forms.ChoiceField(choices=choices.COUNTRY_CHOICES)
    passed_year = forms.CharField(max_length=4)
    educational_document = forms.FileField(required=False)
    work_experience = forms.CharField(widget=forms.Textarea,required=False)

class InstitutionalForm(forms.Form):
    company_name = forms.CharField(max_length=200)
    company_address = forms.CharField(max_length=200)
    registration_no = forms.CharField(max_length=200)
    contact_person = forms.CharField(max_length=200)
    contact_number = forms.CharField(max_length=10)
    website = forms.CharField(max_length=250,required=False)
class EditInstitutionalForm(forms.Form):
    company_name = forms.CharField(max_length=200)
    company_address = forms.CharField(max_length=200)
    registration_no = forms.CharField(max_length=200)
    contact_person = forms.CharField(max_length=200)
    contact_number = forms.CharField(max_length=10)
    website = forms.CharField(max_length=250,required=False)
    working_field = forms.CharField(max_length=200)

class InstitutionalDocuments(forms.Form):
    logo = forms.ImageField(error_messages={
        'required':'Please upload logo of your company photo(Image)'
    })
    pan_document = forms.FileField(error_messages={
        'required':'Please upload PAN Document photo'
    })
    registration_document = forms.FileField(error_messages={
        'required':'Please upload  comapany registration Document'
    })
  
    working_field = forms.CharField(max_length=200)

class EditInstitutionalDocuments(forms.Form):
    logo = forms.ImageField(required=False)
    pan_document = forms.FileField(required=False)
    registration_document = forms.FileField(required=False)
class VerificationForm(forms.Form):
    membership_no = forms.CharField()
    membership_since = forms.CharField(max_length=4)
class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ["payment_ss"]


class FAQForm(forms.ModelForm):
    class Meta:
        model=FAQ
        fields='__all__'