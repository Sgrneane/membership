from django.contrib import admin
from django.urls import path
from . import views
from .insert import ImportBulkData
app_name='management'
urlpatterns = [
    path('',views.index, name='index'),
    path('user-dashboard',views.user_dashboard,name='user_dashboard'),
    path('membership-guidelines',views.membership_guidelines,name='membership_guidelines'),
    path('new-membership',views.new_membership,name='new_membership'),
    #General Membeership Forms 
    path('new-membership/general-membership-personal-info',views.general_membership_personal,name='general_membership_personal'),
    #Registration Completion 
    path('new-membership/complete-national-info/<int:id>',views.complete_registration_national_document,name='complete_registration_national_document'),
    path('new-membership/complete-educational-info/<int:id>',views.complete_registration_educational_document,name='complete_registration_educational_document'),
    # Lifetime Membership 
    path('new-membership/general-membership-personal-info/<int:id>',views.general_membership_personal,name='lifetime_membership_personal'),
    #Student Mambership 
    path('new-membership/student-membership-personal-info',views.student_membership_personal,name='student_membership_personal'),
    #Institutional Membership
    path('new-membership/institutional-membership-form',views.institutional_membership_details,name='institutional_membership_details'),
    path('new-membership/institutional-membership-documents/<int:id>',views.complete_institutional_membership,name='complete_institutional_membership'),

    #Tabular membership Vies 
    path('view-general-membership-list',views.view_general_membership_list,name='view_general_membership_list'),
    path('view-students-membership-list',views.view_student_membership_list,name='view_student_membership_list'),
    path('view-lifetime-membership-list',views.view_lifetime_membership_list,name='view_lifetime_membership_list'),
    path('view-institutional-membership-list',views.view_institutional_membership_list,name='view_institutional_membership_list'),
    #verify membership
    path('verify-membership/<int:id>',views.verify_membership,name='verify_membership'),
    #reject membership
    path('reject-membership/<int:id>',views.reject_membership,name='reject_membership'),
    #Approved Views
    path('view-all-approved-membership_list',views.all_approved_membership_list,name='all_approved_membership_list'),
    path('view-general-approved-membership_list',views.general_approved_membership_list,name='general_approved_membership_list'),
    path('view-lifetime-approved-membership_list',views.lifetime_approved_membership_list,name='lifetime_approved_membership_list'),
    path('view-student-approved-membership_list',views.student_approved_membership_list,name='student_approved_membership_list'),
    path('view-lifetime-approved-membership_list',views.lifetime_approved_membership_list,name='institutional_approved_membership_list'),
    # all rejected
    path('rejected-membership-list',views.rejected_membership_list, name='rejected_membership_list'),
    #view membership
    path('view-membership/membership/<int:id>',views.view_membership,name='view_membership'),
    #edit membership
    path('edit-membership-instance/<int:id>',views.edit_membership,name='edit_membership'),
    path('edit-membership-personal_info/<int:id>',views.edit_personal_info,name='edit_personal_info'),
    path('edit-membership-educational_info/<int:id>',views.edit_educational_info,name='edit_educational_info'),
    path('edit-membership-documents_info/<int:id>',views.edit_national_info,name='edit_national_info'),
    path('edit-institutional-info/<int:id>',views.edit_institutional_info,name='edit_institutional_info'),
    path('edit-institutional-documents/<int:id>',views.edit_institutional_documents,name='edit_institutional_documents'),
    #Payment information
    path('membership/payment',views.payment, name='payment'),
    path("payment/initiate-khalti/", views.initiate_khalti, name="initiate_khalti"),
    path('membership/payment-verification',views.payment_verification,name='payment_verification'),
    #resubmit_membership
    path('resubmit-membership/<int:id>',views.resubmit_membership,name='resubmit_membership'),

    #Tabular View Index
    path('student-members',views.student_members,name='student_members'),
    path('lifetime-members',views.lifetime_members,name='lifetime_members'),
    path('general-members',views.general_members,name='general_members'),
    path('institutional-members',views.institutional_members,name='institutional_members'),
    #upgrade request table
    path('upgrade-to-lifetime-members',views.lifetime_upgrade_request_list,name='upgrade_lifetime_membership_list'),
    path('upgrade-to-general-members',views.general_upgrade_request_list,name='upgrade_general_membership_list'),
    #upgrade Membership
    path('upgrade-to-general-members',views.upgrade_to_general_membership,name='upgrade_to_general_membership'),
    path('upgrade-to-lifetime-members',views.upgrade_to_lifetime_membership,name='upgrade_to_lifetime_membership'),
    path('verify-upgrade/<int:id>',views.verify_upgrade,name='verify_upgrade'),


    ##Faqs
    path('all-faqs',views.all_faqs,name='all_faqs'),
    path('create-faq',views.create_faq,name='create_faq'),
    path('import-bulk-data',ImportBulkData.as_view(),name='import_bulk_data')

]