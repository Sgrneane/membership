from django.shortcuts import render,redirect,HttpResponse,get_object_or_404
import requests
import json
import uuid
from django.db.models import Q
from datetime import datetime
from django.conf import settings
from django.contrib import messages
from . import forms
from .models import (Membership,GeneralMembership,InstitutionalMembership,EducationalDocuments,Payment,NationalDocumment,FAQ)
from .import choices
from .currency_converter import currency_rates
from membership.tasks import send_token_mail
from django.contrib.auth.decorators import login_required
from account.decorators import is_user,is_admin
from events.models import Event
import pandas as pd

# Create your views here.
def index(request):
    events=Event.objects.all()
    faqs=FAQ.objects.all()
    context={
        'events':events,
        'faqs':faqs
    }
    return render(request,'management/index.html',context)



def membership_guidelines(request):
    return render(request,'management/membership_guidelines.html')


def general_members(request):
    general_membership = GeneralMembership.objects.filter(Q(membership_type=1),Q(verification=True))
    context ={
        'members': general_membership
    }
    return render(request,'management/listview/homepage_lists/general_membership_list.html',context)

def lifetime_members(request):
    general_membership = GeneralMembership.objects.filter(Q(membership_type=3),Q(verification=True))
    context ={
        'members': general_membership
    }
    return render(request,'management/listview/homepage_lists/general_membership_list.html',context)


def institutional_members(request):
    student_membership = InstitutionalMembership.objects.filter(verification=True)
    context ={
        'members': student_membership
    }
    return render(request,'management/listview/homepage_lists/institutional_membership_list.html',context)


def student_members(request):
    student_membership = GeneralMembership.objects.filter(Q(membership_type=4),Q(verification=True))
    context ={
        'members': student_membership
    }
    return render(request,'management/listview/homepage_lists/student_membership_list.html',context)


@login_required
def user_dashboard(request):
    user= request.user
    if user.role == 2: 
        general_membership_count=GeneralMembership.objects.filter(Q(membership_type=1),Q(verification=True)).count()
        student_membership_count=GeneralMembership.objects.filter(Q(membership_type=1),Q(verification=True)).count()
        lifetime_membership_count=GeneralMembership.objects.filter(Q(membership_type=3),Q(verification=True)).count()
        institutional_membership_count=InstitutionalMembership.objects.filter(verification=True).count()
        events = Event.objects.all()
        membership=None
        try:
            membership=user.membership
            membership=Membership.objects.select_subclasses().filter(associated_user=user).first()
            print(membership.verification)
        except:
            membership=None
        context={
            'general_membership_count':general_membership_count,
            'student_membership_count':student_membership_count,
            'institutional_membership_count':institutional_membership_count,
            'lifetime_membership_count' :lifetime_membership_count,
            'membership' : membership,
            'events':events
        }
        return render(request,'management/user_dashboard.html',context)
    if user.role == 1:
        general_membership_count=GeneralMembership.objects.filter(Q(membership_type=1),Q(verification=False)).count()
        student_membership_count=GeneralMembership.objects.filter(Q(membership_type=4),Q(verification=False)).count()
        lifetime_membership_count=GeneralMembership.objects.filter(Q(membership_type=3),Q(verification=False)).count()
        institutional_membership_count=InstitutionalMembership.objects.filter(verification=False).count()
        context={
            'general_membership_count':general_membership_count,
            'student_membership_count':student_membership_count,
            'institutional_membership_count':institutional_membership_count,
            'lifetime_membership_count' :lifetime_membership_count,
        }
        return render(request,'management/admin_dashboard.html',context)

#New membership form
@is_user
def new_membership(request):
    return render(request,'management/forms/new_membership.html')
#General lifetime form
@is_user
def general_membership_personal(request, id=None):
    gender = choices.GENDER_CHOICES
    countries = choices.COUNTRY_CHOICES
    salutation = choices.SALUTATION_CHOICES
    form = forms.PersonalInfoForm(request.POST or None,request.FILES or None)
    if request.method == 'POST':
        membership_type = int(request.POST.get('membership_type',1))
        if form.is_valid():
            GeneralMembership.objects.create(associated_user = request.user,
                                             membership_type= membership_type,
                                             **form.cleaned_data)
            return redirect("management:payment")
        else:
            print(form.errors)
    else:    
        pass
    context={
        'form':form,
        'gender':gender,
        'salutation':salutation,
        'countries':countries,
    }
    return render(request,'management/forms/general_membership/membership_info.html',context)
@is_user
def complete_registration_national_document(request,id):
    member = Membership.objects.select_subclasses().get(id=id)
    form =forms.NationalDocumentForm(request.POST or None, request.FILES or None)
    countries = choices.COUNTRY_CHOICES
    if request.method == 'POST':
        if form.is_valid():
            national_document = NationalDocumment.objects.create(**form.cleaned_data)
            member.nationaldocument=national_document
            member.save()
            return redirect('management:complete_registration_educational_document',id=member.id)
        else:
            print(form.errors)
    else:
        pass
    context={
        'form':form,
        'countries': countries,
        'membership': member
    }
    return render(request,'management/forms/general_membership/national_document.html',context)


@is_user       
def complete_registration_educational_document(request,id):
    countries = choices.COUNTRY_CHOICES
    degrees = choices.DEGREE_TYPES
    member = Membership.objects.select_subclasses().get(id=id)
    print(member)
    form =forms.EducationalForm(request.POST or None, request.FILES or None)
    countries = choices.COUNTRY_CHOICES
    if request.method == 'POST':
        if form.is_valid():
            educational_document = EducationalDocuments.objects.create(**form.cleaned_data)
            member.educational_information=educational_document
            member.save()
            messages.success(request,'Congratulations!! Your registration is complete.')
            return redirect('management:user_dashboard')
        else:
            print(form.errors)
    else:
        pass
    context={
        'form':form,
        'countries': countries,
        'degrees':degrees,
        'member': member,
    }
    return render(request,'management/forms/general_membership/educational_info.html',context)


#Student Membership form
@is_user
def student_membership_personal(request):
    gender = choices.GENDER_CHOICES
    countries = choices.COUNTRY_CHOICES
    salutation = choices.SALUTATION_CHOICES
    form = forms.PersonalInfoForm(request.POST or None,request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            GeneralMembership.objects.create(associated_user = request.user,
                                             membership_type= 4,
                                             **form.cleaned_data)
            return redirect("management:payment")
        else:
            print(form.errors)
    else:   
        pass
    context={
        'form':form,
        'gender':gender,
        'salutation':salutation,
        'countries':countries,
    }
    return render(request,'management/forms/student_membership/membership_info.html',context)


#institutional Membership form
@is_user
def institutional_membership_details(request):
    form = forms.InstitutionalForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            InstitutionalMembership.objects.create(associated_user=request.user,
                                                   membership_type=2,
                                                   **form.cleaned_data)
            return redirect("management:payment")
        else:
            print(form.errors)
    else:   
        pass
    context={
        'form':form
    }
    return render(request,'management/forms/institutional/institutional_detail.html',context)


@is_user
def complete_institutional_membership(request,id):
    institutional_membership_instance = Membership.objects.select_subclasses().get(id=id)
    form= forms.InstitutionalDocuments(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            institutional_membership_instance.logo = form.cleaned_data['logo']
            institutional_membership_instance.pan_document = form.cleaned_data['pan_document']
            institutional_membership_instance.registration_document = form.cleaned_data['registration_document']
            institutional_membership_instance.working_field = form.cleaned_data['working_field']
            institutional_membership_instance.save()
            messages.success(request,'Congratulations!! Your registration is complete.')
            return redirect('management:user_dashboard')
        else:
            print(form.errors)
    else:
        pass
    context={
        'form':form
    }
    return render(request,'management/forms/institutional/documents.html',context)

#view membership list
@is_admin
def view_general_membership_list(request):
    general_membership = GeneralMembership.objects.filter(Q(membership_type=1),Q(verification=False))
    context ={
        'members': general_membership
    }
    return render(request,'management/listview/general_membership_list.html',context)

@is_admin
def view_student_membership_list(request):
    student_membership = GeneralMembership.objects.filter(Q(membership_type=4),Q(verification=False))
    context ={
        'members': student_membership
    }
    return render(request,'management/listview/student_membership_list.html',context)

@is_admin
def view_lifetime_membership_list(request):
    general_membership = GeneralMembership.objects.filter(Q(membership_type=3),Q(verification=False))
    context ={
        'members': general_membership
    }
    return render(request,'management/listview/lifetime_membership_list.html',context)


@is_admin
def view_institutional_membership_list(request):
    institutional_membership = InstitutionalMembership.objects.filter(verification=False)
    context ={
        'members': institutional_membership
    }
    return render(request,'management/listview/institutional_membership_list.html',context)

#view membership details
@login_required
def view_membership(request,id):
    general_membership_instance= Membership.objects.select_subclasses().get(id=id)
    latest_membership = Membership.objects.filter(verification=True).last()
    if(latest_membership):
        latest_membership_number = latest_membership.membership_number
    else:
        latest_membership_number = 0
    
    if isinstance(general_membership_instance, GeneralMembership):
        context={
                'membership':general_membership_instance,
                'latest_id' : latest_membership_number
            }
        if general_membership_instance.rejected == True:
            return render(request,'management/views/edit_membership.html',context)
        else:
            return render(request,'management/views/view_membership.html',context)
    if isinstance(general_membership_instance, StudentMembership):
        context={
                'membership':general_membership_instance,
                'latest_id' : latest_membership_number
            }
        if general_membership_instance.rejected == True:
            return render(request,'management/views/edit_membership.html',context)
        else:
            return render(request,'management/views/view_membership.html',context)
    if isinstance(general_membership_instance, InstitutionalMembership):
        context={
                'membership':general_membership_instance,
                'latest_id' : latest_membership_number
            }
        if general_membership_instance.rejected == True:
            return render(request,'management/views/edit_institutional_membership.html',context)
        else:
             return render(request,'management/views/view_institutional_membership.html',context)
    
@login_required
def edit_membership(request,id):
    membership_instance= Membership.objects.select_subclasses().get(id=id)
    latest_membership = Membership.objects.filter(verification=True).last()
    latest_membership_number = latest_membership.membership_number
    if isinstance(membership_instance, GeneralMembership):
        context={
                'membership':membership_instance,
                'latest_id' : latest_membership_number
            }
        return render(request,'management/views/edit_membership.html',context)
    if isinstance(membership_instance, StudentMembership):
        context={
                'membership':membership_instance,
                'latest_id' : latest_membership_number
            }
        return render(request,'management/views/edit_membership.html',context)
    if isinstance(membership_instance, InstitutionalMembership):
        context={
                'membership':membership_instance,
                'latest_id' : latest_membership_number
            }
        return render(request,'management/views/edit_institutional_membership.html',context)

@login_required
def edit_personal_info(request,id):
    membership_instance = get_object_or_404(Membership.objects.select_subclasses(), id=id)
    gender = choices.GENDER_CHOICES
    countries = choices.COUNTRY_CHOICES
    salutation = choices.SALUTATION_CHOICES
    if request.method == 'POST':
        form = forms.EditPersonalInfoForm(request.POST,request.FILES or None)
        if form.is_valid():
            membership_instance.name_of_applicant = form.cleaned_data['name_of_applicant']
            membership_instance.phone_number = form.cleaned_data['phone_number']
            membership_instance.gender = form.cleaned_data['gender']
            membership_instance.affiliation = form.cleaned_data['affiliation']
            if form.cleaned_data.get('pp_photo'):
                membership_instance.pp_photo = form.cleaned_data['pp_photo']
            else:
                pass
            membership_instance.salutation = form.cleaned_data['salutation']
            membership_instance.save()
            return redirect('management:edit_membership',id=membership_instance.id)
        else:
            print(form.errors)
    else:
        pass
    context={
        'membership':membership_instance,
        'gender':gender,
        'salutation':salutation,
        'countries':countries,
    }
    return render(request,'management/forms/edit_personal_info.html',context)
            
@login_required
def edit_educational_info(request,id):
    membership_instance = get_object_or_404(Membership.objects.select_subclasses(), id=id)
    countries = choices.COUNTRY_CHOICES
    degrees = choices.DEGREE_TYPES
    if request.method == 'POST':
        form = forms.EditEducationalForm(request.POST,request.FILES)
        if form.is_valid():
            educational_info_instance= membership_instance.educational_information
            educational_info_instance.degree_type= form.cleaned_data['degree_type']
            educational_info_instance.course = form.cleaned_data['course']
            educational_info_instance.university = form.cleaned_data['university']
            educational_info_instance.institution = form.cleaned_data['institution']
            educational_info_instance.country = form.cleaned_data['country']
            educational_info_instance.passed_year = form.cleaned_data['passed_year']
            if form.cleaned_data.get('educational_document'):
                educational_info_instance.educational_document = form.cleaned_data['educational_document']
            else:
                pass
            educational_info_instance.save()
            membership_instance.save()
            return redirect('management:edit_membership',id=membership_instance.id)
        else:
            print(form.errors)
    else:
        pass
    context={
        'membership':membership_instance,
        'countries':countries,
        'degrees':degrees,
    }
    return render(request,'management/forms/edit_educational_info.html',context)


@login_required
def edit_national_info(request,id):
    membership_instance = get_object_or_404(Membership.objects.select_subclasses(), id=id)
    gender = choices.GENDER_CHOICES
    countries = choices.COUNTRY_CHOICES
    salutation = choices.SALUTATION_CHOICES
    if request.method == 'POST':
        form = forms.EditNationalDocumentForm(request.POST,request.FILES or None)
        if form.is_valid():
            national_info_instance= membership_instance.nationaldocument
            national_info_instance.nationality= form.cleaned_data['nationality']
            national_info_instance.identity_card_no = form.cleaned_data['identity_card_no']
            national_info_instance.dob = form.cleaned_data['dob']
            national_info_instance.identity_issued_from = form.cleaned_data['identity_issued_from']
            national_info_instance.permanent_address = form.cleaned_data['permanent_address']
            if form.cleaned_data.get('identity_card_image'):
                national_info_instance.identity_card_image = form.cleaned_data['identity_card_image']
            else:
                pass
            national_info_instance.save()
            membership_instance.save()
            return redirect('management:edit_membership',id=membership_instance.id)
        else:
            print(form.errors)
    else:
        pass
    context={
        'membership':membership_instance,
        'gender':gender,
        'salutation':salutation,
        'countries':countries,
    }
    return render(request,'management/forms/edit_national_info.html',context)

@login_required
def edit_institutional_info(request,id):
    membership_instance = get_object_or_404(Membership.objects.select_subclasses(), id=id)
    form = forms.EditInstitutionalForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            membership_instance.company_name = form.cleaned_data['company_name']
            membership_instance.company_address = form.cleaned_data['company_address']
            membership_instance.registration_no = form.cleaned_data['registration_no']
            membership_instance.website = form.cleaned_data['website']
            membership_instance.contact_person= form.cleaned_data['contact_person']
            membership_instance.contact_number = form.cleaned_data['contact_number']
            membership_instance.working_field = form.cleaned_data['working_field']
            membership_instance.save()
            return redirect('management:edit_membership',id=membership_instance.id)
        else:
            print(form.errors)
    else:
        pass
    context={
        'membership':membership_instance,
    }
    return render(request,'management/forms/institutional/edit_institutional_info.html',context)

@login_required
def edit_institutional_documents(request,id):
    membership_instance = get_object_or_404(Membership.objects.select_subclasses(), id=id)
    form = forms.EditInstitutionalDocuments(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            print(form.cleaned_data)
            if form.cleaned_data.get('pan_document'):
                membership_instance.pan_document = form.cleaned_data['pan_document']
            else:
                pass
            if form.cleaned_data.get('registration_document'):
                membership_instance.registration_document = form.cleaned_data['registration_document']
            else:
                pass
            if form.cleaned_data.get('logo'):
                membership_instance.logo = form.cleaned_data['logo']
            else:
                pass
            membership_instance.save()
            return redirect('management:edit_membership',id=membership_instance.id)
        else:
            print(form.errors)
    else:
        pass
    context={
        'membership':membership_instance,
    }
    return render(request,'management/forms/institutional/edit_institutional_document.html',context)


@is_user
def resubmit_membership(request,id):
    membership_instance = get_object_or_404(Membership.objects.select_subclasses(), id=id)
    if request.method == 'POST':
        membership_instance.verification = False
        membership_instance.rejected = False
        membership_instance.save()
        messages.success(request,'Your membership has been resubmitted successfully.')
        return redirect('management:user_dashboard')


@is_admin
def verify_membership(request,id):
    membership_object = get_object_or_404(Membership, id=id)
    if request.method == "POST":
        form = forms.VerificationForm(request.POST)
        if form.is_valid():
            membership_since = form.cleaned_data.get("membership_since")
            membership_object.membership_since = membership_since
            membership_object.verification = True
            membership_object.verified_date = datetime.now()
            membership_object.save()
            messages.success(request, "Membership Verified")
            # try:
            #     subject="Your account has been verified."
            #     message=f"Yor membership for Nepal Geotechnical Society is verified now."
            #     send_token_mail(membership_object.associated_user.email,subject,message)
            # finally:
            return redirect("management:all_approved_membership_list")
        else:
            messages.error(
                request,
                "Enter  membership year to verify the member",
            )
            return redirect("management:verify_membership", id=membership_object.id)

@is_admin
def reject_membership(request,id):
    membership_object = get_object_or_404(Membership, id=id)
    if request.method == "POST":
        remarks = request.POST.get("remarks")
        membership_object.remarks = remarks
        membership_object.rejected =True
        membership_object.verification = False
        membership_object.save()
        messages.error(request, "Membership Rejected")
            # try:
            #     subject="Your account has been verified."
            #     message=f"Yor membership for Nepal Geotechnical Society is verified now."
            #     send_token_mail(membership_object.associated_user.email,subject,message)
            # finally:
        return redirect("management:rejected_membership_list")


@is_admin
def all_approved_membership_list(request):
    members=Membership.objects.select_subclasses().filter(verification=True)
    context={
        'members':members,
    }
    return render(request,'management/listview/all_approved_membership_list.html',context)


@is_admin
def general_approved_membership_list(request):
    members=GeneralMembership.objects.filter(membership_type=1,verification=True)
    context={
        'members':members,
    }
    return render(request,'management/listview/general_membership_list.html',context)


@is_admin
def lifetime_approved_membership_list(request):
    members=GeneralMembership.objects.filter(Q(membership_type=3),Q(verification=True))
    context={
        'members':members,
    }
    return render(request,'management/listview/lifetime_membership_list.html',context)

@is_admin
def student_approved_membership_list(request):
    members=GeneralMembership.objects.filter(Q(membership_type=4),Q(verification=True))
    context={
        'members':members,
    }
    return render(request,'management/listview/student_membership_list.html',context)


@is_admin
def institutional_approved_membership_list(request):
    members=InstitutionalMembership.objects.filter(verification=True)
    context={
        'members':members,
    }
    return render(request,'management/listview/institutional_membership_list.html',context)

@is_admin
def rejected_membership_list(request):
    rejected_members = Membership.objects.select_subclasses().filter(rejected = True)
    context={
        'members' : rejected_members
    }  
    return render(request,'management/listview/all_approved_membership_list.html',context) 

@login_required
def payment(request):
    """Handles the payment for individual users."""
    user=request.user
    try:
        membership= Membership.objects.select_subclasses().get(associated_user=user)
    except:
        membership=None
    paid_amount= None
    paid_date =None
    if user.membership.payment.exists():
        paid_date = user.paid_payment.last().created_at
        if user.membership.membership_type == 1:
            paid_amount=2000
        elif user.membership.membership_type == 2:
            paid_amount=100000
        elif user.membership.membership_type == 3:
            paid_amount=10000
        else:
            paid_amount=1000
        
    host = request.get_host()
    uid = uuid.uuid4()
    khalti_return_url = "http://127.0.0.1:8000/membership/payment-verification"
    if request.method == "POST":
        print('request')
        form = forms.PaymentForm(request.POST, request.FILES)
        if form.is_valid():
            Payment.objects.create(
                created_by=request.user,
                 member=membership,
                created_at=datetime.now(), **form.cleaned_data
            )
            if membership.upgrade_request == True:
                membership.upgrade_payment = True
                membership.save()
            else:
                pass
            return redirect('management:payment')# redirect to payment page
        else:
            messages.error(
                request, "Process Failed!!. Submit Screenshot of your payment."
            )
            print("hh")
            return redirect("management:payment") #same page
    else:
        form = forms.PaymentForm()
        
    # paypal urls
    context = {
            "membership": membership,
            "return_url": khalti_return_url,
            "uid": uid,
            "paid_amount":paid_amount,
            "paid_date" :paid_date,
        }
    return render(request, "management/payment/payment.html", context)


def general_upgrade_request_list(request):
    general_upgrade_membership=GeneralMembership.objects.filter(Q(upgrade_request=True),Q(upgrade_membership_type=1))
    context={
        'members':general_upgrade_membership,
        'upgrade':2
    }
    return render(request,'management/listview/upgrade_list.html',context)

def lifetime_upgrade_request_list(request):
    general_upgrade_membership=GeneralMembership.objects.filter(Q(upgrade_request=True),Q(upgrade_membership_type=3))
    context={
        'members':general_upgrade_membership,
        'upgrade':1
    }
    print('general_upgrade_membership')
    return render(request,'management/listview/upgrade_list.html',context)


def upgrade_to_general_membership(request):
    user=request.user
    membership=get_object_or_404(Membership.objects.select_subclasses(),associated_user=user)
    membership.upgrade_request=True
    membership.upgrade_membership_type = 1
    membership.save()
    return redirect('management:payment')

def upgrade_to_lifetime_membership(request):
    user=request.user
    membership=get_object_or_404(Membership.objects.select_subclasses(),associated_user=user)
    membership.upgrade_request=True
    membership.upgrade_membership_type = 3
    membership.save()
    return redirect('management:payment')


def verify_upgrade(request,id):
    membership= get_object_or_404(Membership.objects.select_subclasses(),id=id)
    membership.membership_type = membership.upgrade_membership_type
    membership.upgrade_request=False
    membership.upgrade_payment = False
    membership.save()
    return redirect('management:all_approved_membership_list')


def initiate_khalti(request):
    """Initiates the payment by user and redirects them to the payment url."""
    user = request.user
    purchase_order_id = request.POST.get("purchase_order_id")
    amount = str(request.POST.get("amount"))
    return_url = request.POST.get("return_url")

    url = "https://khalti.com/api/v2/epayment/initiate/"
    payload = json.dumps(
        {
            "return_url": return_url,
            "website_url": "https://example.com/",
            "amount": "100",
            "purchase_order_id": purchase_order_id,
            "purchase_order_name": "test",
            "customer_info": {
                "name": user.first_name + user.last_name,
                "email": user.email,
                "phone": user.phone_number,
            },
        }
    )
    headers = {
        "Authorization":'key test_secret_key_7fa6d8a1432949448af8e544307ea45f',
        "Content-Type": "application/json",
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    new_res = json.loads(response.text)
    print(new_res)

    if response.status_code == 200:
        return redirect(new_res["payment_url"])
    else:
        messages.error(
            request, "Payment failed. Check your phone number and other details."
        )
        return redirect("management:payment")
    
def payment_verification(request):
    """Verifies the users payment done in khalti."""
    pidx = request.GET.get("pidx")
    amount = request.GET.get("amount")
    txn_id = request.GET.get("txnId")

    url = "https://khalti.com/api/v2/epayment/lookup/"
    headers = {
        "Authorization":'key test_public_key_fc9fe6ad491a4c7ca3bcf623eb214b8e',
        "Content-Type": "application/json",
    }
    payload = json.dumps({"pidx": pidx})
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)

    if response.json()["status"] == "Completed":
        Payment.objects.create(
            created_at=datetime.now(),
            user_id=request.user.id,
            paid_amount_in_paisa=amount,
            pidx=pidx,
            txn_id=txn_id,
        )
        messages.success(request, "Payment Successful")
        return HttpResponse('success')
    else:
        # message = request.GET.get("message")
        return HttpResponse('failed')



def all_faqs(request):
    faqs=FAQ.objects.all()
    context={
        'faqs':faqs
    }
    return render(request,'management/faqs_list.html',context)


def create_faq(request):
    if request.method=='POST':
        form=forms.FAQForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('management:all_faqs')
        else:
            messages.info(request,'Please fill form correctly')
            return redirect('management:create_faq')
    
    return render(request,'management/create_faq.html')




