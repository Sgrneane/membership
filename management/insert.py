import pandas as pd
from django.db import transaction
from django.utils import timezone
from django.core.files import File
from .models import Membership, GeneralMembership,Payment
from account.models import CustomUser
from django.views import View
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import MembershipImportForm
from django.contrib.auth.hashers import make_password
import csv

class ImportBulkData(View):
    form_class = MembershipImportForm
    template_name = 'management/import_csv.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})
    @transaction.atomic
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            file = form.cleaned_data['excel_file']
            df = pd.read_excel(file,engine='openpyxl')
            for index, row in df.iterrows():
                user, created = CustomUser.objects.get_or_create(
                email=row['email'],
                full_name = row['name'],
                is_verified = True,  # Assuming all users in the Excel file should be marked as verified
                role = 2,
                )
                if created:
                    password=make_password('NGSmember')
                    user.password=password
                    user.save()
                    default_photo_path = 'media/pp_photo.jpg'

                    with open(default_photo_path, 'rb') as photo_file:
                        membership = GeneralMembership.objects.create(
                            membership_type = row['membership_type'],
                            name_of_applicant=row['name'],
                            gender='M',
                            affiliation=row['affiliation'],
                            salutation=row['salutation'],
                            phone_number=row['phone_number'],
                            verification=True,
                            membership_since=row['membership_since'],
                            associated_user=user,
                            pp_photo=File(photo_file, name='default_pp_photo.jpg'), 
                            )
                    
                    payment = Payment.objects.create(
                        created_at = timezone.now(),
                        created_by = user,
                        member = membership,
                        paid = True,
                    )   
            return HttpResponse("Your data has been imported successfully")
        return render(request, self.template_name, {'form': form})
