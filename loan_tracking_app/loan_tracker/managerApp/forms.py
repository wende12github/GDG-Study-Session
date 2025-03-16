from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django import forms
from loans.models import loanCategory


class LoanCategoryForm(forms.ModelForm):
    class Meta:
        model = loanCategory
        fields = ('loan_name',)

class AdminLoginForm(AuthenticationForm):
    class Meta:
        model = loanCategory
        fields = ('username', 'password')