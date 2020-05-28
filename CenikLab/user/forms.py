from django import forms

from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate

#form structures required for users' information
class LoginForm(forms.Form):
    username = forms.CharField(label = "Username")
    password = forms.CharField(label = "Password", widget = forms.PasswordInput)


    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        if username and password:
            user = authenticate(username = username,password = password)
            if not user:
                raise forms.ValidationError("yanlis")
        
        return super(LoginForm,self).clean()

#form structures required for users' information
class RegisterForm(forms.ModelForm):

    username = forms.CharField(max_length = 50, label="Username")
    password = forms.CharField(max_length = 20, label="Password",widget = forms.PasswordInput)
    confirm = forms.CharField(max_length = 20, label = "confirm Password", widget = forms.PasswordInput)

    class Meta:
       model = User
       fields = [
           'username',
           'password',
           'confirm',
       ]

    def clean_confirm(self):
        password = self.cleaned_data.get("password")
        confirm = self.cleaned_data.get("confirm")
        if password and confirm and password != confirm:
            raise forms.ValidationError("password does not match")
        return confirm





#class RegisterForm(forms.Form):

#    username = forms.CharField(max_length = 50, label="Username")
 #   email = forms.CharField(max_length = 50, label="E-mail")
  #  password = forms.CharField(max_length = 20, label="Password",widget = forms.PasswordInput)
   # confirm = forms.CharField(max_length = 20, label = "confirm Password", widget = forms.PasswordInput)

    #def clean(self):
     #   username = self.cleaned_data.get("username")
      #  email = self.cleaned_data.get("email")
       # password = self.cleaned_data.get("password")
        #confirm = self.cleaned_data.get("confirm")

        #if password and confirm and password != confirm:
         #   raise forms.ValidationError("password does not match")

       # values = {
        #    "username":username,
         #   "email":email,
          #  "password":password,

        #}
        #return values



