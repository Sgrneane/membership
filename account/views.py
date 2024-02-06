from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponse,redirect,get_list_or_404, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib import messages
from django.contrib.auth.views import PasswordResetView
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import CustomUser
from .decorators import is_admin,is_superadmin,is_user,authentication_not_required
from .forms import SignupForm

from .generate_token import generate_unique_four_digit_number
from membership.tasks import send_token_mail
from management.models import Membership


def signup(request):
    """For creating regular users."""
    form = SignupForm(request.POST or None)
    if request.method=='POST':
        if form.is_valid():
            User = get_user_model()
            new_user=User.objects.create_user(token=str(generate_unique_four_digit_number()),
                                     **form.cleaned_data)
            subject="Verify your account."
            message=f"Your pin is {new_user.token}. Login with your new account and enter this pin to verify."
            send_token_mail(new_user.email,subject,message)
            messages.success(request,"Account created Successfully. Login Now.")
            return redirect(reverse('account:login_user'))  
        else:
            print(form.errors)
            #messages.error(request, 'User not created! Please fill the form with correct data!')
            pass
    else:
        pass
    context={
        'form':form
    }
    return render(request, 'account/signup.html',context)

#Activate user Email Verification
# def activate(request):
@authentication_not_required
def login_user(request):
    if(request.method == 'POST'):
        email=request.POST['email']
        password=request.POST['password']
        user=authenticate(request,username=email, password=password)
        if user is not None:
            login(request,user)
            if user.is_verified == False:
                messages.success(request,"We have sent a token to your Gmail. Please enter the token to verify.")
                return redirect(reverse('account:activate'))
            else:
                return redirect(reverse('management:user_dashboard'))
        else:
            messages.error(request, 'Incorrect Username or Password!')
            return redirect('account:login_user')
    else:
        return render(request,'account/login.html')

@login_required
def logout_user(request):
    logout(request)
    return redirect(reverse('management:index'))

class CustomPasswordResetView(PasswordResetView):
    """
    Customizing the django default passwordresetview to check if users email exist in
    database before sending mail
    """
    def form_valid(self, form):
        email = form.cleaned_data["email"]
        # Check if the email exists in the database
        if not CustomUser.objects.filter(email=email).exists():
            messages.error(self.request, "Email does not exist.")
            return self.form_invalid(form)
        return super().form_valid(form) 
    
@login_required
def activate(request):
    """
    User will enter the pin sent to them via email and if the pin is correct user is
    verified and can apply for membership.
    """
    user = request.user
    if request.method == "POST":
        pin = request.POST.get("pin")
        if user.token == pin:
            user.is_verified = True
            user.save()
            messages.success(request, "Your  account has been verified")
            return redirect("management:user_dashboard")
        else:
            messages.error(request, "Invalid PIN. Check your mail for correct PIN.")
            return redirect("account:activate")
    else:
        return render(request,'account/verify_user.html')

@login_required
def resend_token(request):
    user=request.user
    if request.method=='POST':
        resend_verify = request.POST.get('resend_token')
        if resend_verify == user.first_name+'123':
            new_token=str(generate_unique_four_digit_number())
            user.token=new_token
            user.save()
            subject="Verify your account."
            message=f"Your pin is {user.token}. Login with your new account and enter this pin to verify."
            send_token_mail(user.email,subject,message)
            messages.success(request,'We have sent new token in Your mail.Please Enter new token.')
            return redirect('account:activate')
        else:
            messages.error(request, "Given word doesn't match the desired word. Retype and resend")
            return redirect('account:resend_token')
    return render(request,'account/resend_token.html')

@login_required
def my_account(request):
    user=request.user
    membership= Membership.objects.select_subclasses().get(associated_user=user)
    context={
        'membership': membership
    }
    return render(request,'account/myprofile.html',context)

@login_required
def change_password(request):
    user=request.user
    membership= Membership.objects.select_subclasses().get(associated_user=user)
    context={
        'membership': membership
    }

    if request.method == "POST":
        current_password = request.POST.get("current_password")
        new_password = request.POST.get("new_password")
        retype_new_password = request.POST.get("retype_new_password")

        if current_password == "" or new_password == "" or retype_new_password == "":
            messages.error(request, "Please fill all the fields")
            return redirect("account:change_password")

        if not user.check_password(current_password):
            messages.error(request, "Incorrect Current Password")
            return redirect("account:change_password")

        if new_password != retype_new_password:
            messages.error(request, "New Passwords didn't match")
            return redirect("account:change_password")

        if current_password == new_password:
            messages.error(
                request, "New Password should not be same as Current Password!"
            )
            return redirect("account:change_password")

        user.set_password(new_password)
        user.save()
        messages.success(
            request, "Password Changed Successfully! Login with new password"
        )
        return redirect("account:login_user")
    return render(request, "account/changepassword.html",context)

