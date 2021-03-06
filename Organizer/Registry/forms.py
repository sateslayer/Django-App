from django import forms
from .models import storeData, FileUpload

class LoginForm(forms.Form):
    model = storeData
    phone_number = forms.CharField(max_length = 100,widget=forms.TextInput(
        attrs={
            "class": "form-control",
            "placeholder": "Phone number",
            "required": "remember",
            "name": "phone_number"
        }
    ))
    password = forms.CharField(widget = forms.PasswordInput(
        attrs={
            "class": "form-control",
            "placeholder": "Password",
            "required": "required",
            "name": "password"
        }
    ))

class SelectStudentForm(forms.Form):
    model = storeData
    choices = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, required = False)
    search_field = forms.CharField()
class RegistrationForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            "class": "form-control",
            "placeholder": "Username",
            "name": 'username',
            "required": "required"
        }
    ))
    password = forms.CharField(widget = forms.PasswordInput(
        attrs={
            "class": "form-control",
            "placeholder": "Password",
            "required": "required",
            "name": 'password'
        }
    ))
    confirm_password = forms.CharField(widget = forms.PasswordInput(
        attrs={
            "class": "form-control",
            "placeholder": "Confirm Password",
            "required": "required",
            "name": 'password'
        }
    ))
    phone_number = forms.CharField(widget=forms.TextInput(
        attrs={
            "class": "form-control",
            "placeholder": "Contact number",
            "required": "required",
            "name": 'phone_number'
        }
    ))

    email_address = forms.EmailField(widget=forms.EmailInput(
        attrs={
            "class": "form-control",
            "placeholder": "Email address",
            "required": "required",
            "name": 'email_address'
        }
    ))
    CHOICE = (('1', 'First',), ('2', 'Second',))
    Batch = forms.ChoiceField(widget = forms.RadioSelect, choices = CHOICE)
    class Meta:
        model = storeData
        fields = ('username', 'phone_number', 'password',)

class AttendanceForm(forms.Form):
    choices = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, required = False)
    search_field = forms.CharField()
class FileUploadForm(forms.ModelForm):
    choices = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, required = False)
    search_field = forms.CharField(required = False)
    class Meta:
        model = FileUpload
        fields = ('description', 'uploadedFile')

class ValidationForm(forms.Form):
    model = storeData
    CHOICE = [('1', 'Validate'), ('2', 'Discard')]
    choices = forms.MultipleChoiceField(widget=forms.RadioSelect, choices=CHOICE, required = False)

class FeesPaid(forms.Form):
    model = storeData
    choices = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, required = False)

class FileDownloadForm(forms.Form):
    model = FileUpload
    choices = forms.ChoiceField(widget=forms.RadioSelect(), required = False)

class phoneNumber(forms.Form):
    phone_number = forms.CharField()
    class Meta:
        model = storeData

class delete_form(forms.Form):
    choices = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, required = False)
    search_field = forms.CharField()
    