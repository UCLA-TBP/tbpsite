from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.forms import ModelForm

from main.models import Settings, Term, Profile, Candidate, ActiveMember, PeerTeaching, Test_Upload, ReviewSheet
from tutoring.models import Class

class UserForm(ModelForm):
    def check_password(self, password):
        raise NotImplementedError

    def clean(self):
        cleaned_data = super(UserForm, self).clean()

        current_password, username, new_password, confirm_password = map(
            cleaned_data.get, ('current_password', 'username', 'new_password', 'confirm_password'))

        if any([username != self.instance.get_username(), new_password, confirm_password]) and not current_password:
            self._errors['current_password'] = self.error_class(["Current password required."])

        if current_password and not self.check_password(current_password):
            self._errors['current_password'] = self.error_class(["Incorrect password."])

        if username != self.instance.get_username() and User.objects.filter(username=username).count():
            self._errors['username'] = self.error_class(["Username has already been taken. If you made this account, try logging in."])

        if new_password != confirm_password:
            self._errors['confirm_password'] = self.error_class(["Passwords do not match."])

        return cleaned_data


class UserAccountForm(UserForm):
    current_password = forms.CharField(widget=forms.widgets.PasswordInput, required=True, label="Current Password")
    username = forms.CharField(required=False)
    new_password = forms.CharField(widget=forms.widgets.PasswordInput, required=False, label="New Password")
    confirm_password = forms.CharField(widget=forms.widgets.PasswordInput, required=False, label="Confirm Password")

    class Meta:
        model = User
        fields = ['current_password', 'username', 'new_password', 'confirm_password']

    def check_password(self, password):
        return self.instance.check_password(password)


class RegisterForm(UserForm):
    current_password = forms.CharField(widget=forms.widgets.PasswordInput, label="Registration Code")
    username = forms.CharField()
    new_password = forms.CharField(widget=forms.widgets.PasswordInput, label="New Password")
    confirm_password = forms.CharField(widget=forms.widgets.PasswordInput, label="Confirm Password")

    class Meta:
        model = User
        fields = ['current_password', 'username', 'new_password', 'confirm_password']

    def check_password(self, password):
        return password == Settings.objects.get_registration_code()


class UserPersonalForm(ModelForm):
    # TODO: change to email field
    email = forms.CharField(required=True)
    first_name = forms.CharField(required=True, label="Legal First Name")
    middle_name = forms.CharField(required=False, label="Middle Name (if applicable)")
    last_name = forms.CharField(required=True, label="Last Name")

    class Meta:
        model = User
        fields = ['email', 'first_name', 'middle_name', 'last_name']

#TODO: add rest of form fields
class TermForm(ModelForm):
    class Meta:
        model = Term
        exclude = ('start_date', 'due_date')
    
class ClassForm(ModelForm):
    class Meta:
        model = Class
        exclude = ('display')
        

class TestForm(ModelForm):
    #professor = forms.CharField(required=True, label="Professor")
    #origin_term = forms.ChoiceField(choices=Term.TERM_CHOICES, label = "Test Term")
    #origin_quarter = forms.ChoiceField(choices=Term.QUARTER_CHOICES, label="Test quarter")
    #origin_year = forms.IntegerField(label="Test year")
    #test_upload = forms.FileField(required=True)

    class Meta:
        model = Test_Upload
        exclude = ( 'profile')
        #fields = ['professor', 'origin_quarter','origin_year','test_upload']
    
    def __init__(self, *args, **kwargs):
        super(TestForm, self).__init__(*args, **kwargs)

class ReviewSheetForm(ModelForm):
    class Meta:
        model = ReviewSheet

    def __init__(self, *args, **kwargs):
        super(ReviewSheetForm, self).__init__(*args, **kwargs)
        
class ProfileForm(ModelForm):
    birthday = forms.DateField(label="Birthday (mm/dd/yyyy)", widget=forms.DateInput)
    graduation_quarter = forms.ChoiceField(choices=Term.QUARTER_CHOICES, label="Graduation Quarter")
    graduation_year = forms.IntegerField(label="Graduation Year")

    class Meta:
        model = Profile
        fields = ['nickname', 'gender', 'birthday', 'phone_number', 'uid', 'major',
                  'graduation_quarter', 'graduation_year', 'resume_pdf', 'resume_word']
        widgets = {
            'gender': forms.widgets.RadioSelect
        }


class FirstProfileForm(ModelForm):
    graduation_quarter = forms.ChoiceField(choices=Term.QUARTER_CHOICES, label="Graduation Quarter")
    graduation_year = forms.IntegerField(label="Graduation Year")

    class Meta:
        model = Profile
        fields = ['nickname', 'gender', 'birthday', 'phone_number', 'uid', 'major', 'graduation_quarter', 'graduation_year']
        widgets = {
            'gender': forms.widgets.RadioSelect
        }


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.widgets.PasswordInput)

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        user = authenticate(username=cleaned_data.get('username'), password=cleaned_data.get('password'))
        if user is None:
            self._errors['password'] = self.error_class(["Incorrect password."])
        else:
            cleaned_data['user'] = user
        return cleaned_data


class CandidateForm(ModelForm):
    class Meta:
        model = Candidate
        fields = ['professor_interview']


class MemberForm(ModelForm):
    class Meta:
        model = ActiveMember
        fields = ['requirement_choice']


class ShirtForm(ModelForm):
    class Meta:
        model = Candidate
        fields = ['shirt_size']

class PeerTeachingForm(ModelForm):
    class Meta:
        model = PeerTeaching
        fields = ['requirement_choice']

class TestQueryForm(forms.Form):
    search_params = forms.CharField(label='Search Parameters')
