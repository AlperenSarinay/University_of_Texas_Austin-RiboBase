from django import forms

#form structures required for users' information
class LoginForm(forms.Form):
    email = forms.CharField(label = "E-mail")
    password = forms.CharField(label = "Password", widget = forms.PasswordInput)

#form structures required for users' information
class RegisterForm(forms.Form):

    username = forms.CharField(max_length = 50, label="Username")
    email = forms.CharField(max_length = 50, label="E-mail")
    password = forms.CharField(max_length = 20, label="Password",widget = forms.PasswordInput)
    confirm = forms.CharField(max_length = 20, label = "confirm Password", widget = forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data.get("username")
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        confirm = self.cleaned_data.get("confirm")

        if password and confirm and password != confirm:
            raise forms.ValidationError("password does not match")

        values = {
            "username":username,
            "email":email,
            "password":password,

        }
        return values




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



