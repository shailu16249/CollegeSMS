from django.contrib.auth.models import User
from django import forms
from .models import Student,Faculty,LeaveRequest,Subject
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username','first_name','last_name','email','password1','password2','is_staff']


class FacultyForm(forms.ModelForm):

    class Meta:
        model = Faculty
        fields = ['Id','name', 'phone', 'email', 'department']


class SubjectForm(forms.ModelForm):
    Id=forms.CharField(max_length=100)
    name=forms.CharField(max_length=900)
    class Meta:
        model = Subject
        fields = ['Id','name','faculty']



class StudentForm(forms.ModelForm):

    DOB = forms.DateField(widget=forms.SelectDateWidget(years=[i for i in range(1920,2010)]),input_formats=['%Y-%m-%d','%m/%d/%Y','%m/%d/%y','%d/%m/%y'])

    class Meta:
        model = Student
        fields = ['photo','DOB','branch','year','tenth_marks','inter_marks','current_marks']


class LeaveRequestForm(forms.ModelForm):
    start = forms.DateField(widget=forms.SelectDateWidget())
    end= forms.DateField(widget=forms.SelectDateWidget())
    reason=forms.CharField(widget=forms.Textarea)
    class Meta:
        model = LeaveRequest
        fields = ['start','end','type','reason']



#UserCreationForm.Meta.fields +

# class FacultyForm(forms.ModelForm):

#     class Meta:
#         model = Faculty
#         fields = ['photo','specialization']