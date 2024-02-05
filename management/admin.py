from django.contrib import admin
from .models import Membership,GeneralMembership,InstitutionalMembership,StudentMembership,Payment,EducationalDocuments
# Register your models here.
admin.site.register(Membership)
admin.site.register(GeneralMembership)
admin.site.register(InstitutionalMembership)
admin.site.register(StudentMembership)
admin.site.register(Payment)
admin.site.register(EducationalDocuments)
