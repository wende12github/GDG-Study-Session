from django import forms
from .models import loanRequest, loanTransaction

class LoanRequestForm(forms.ModelForm):
    class Meta:
        model = loanRequest
        # fields = ['name', 'amount', 'date', 'reason']
        fields = ('category', 'reason', 'amount', 'year')

        # Add an extra 'other_category' field that is only required if the user selects 'Other'
    other_category = forms.CharField(max_length=250, required=False, widget=forms.TextInput(attrs={
        'placeholder': 'Enter custom category',
        'id': 'other-category-input',
        'style': 'display:none;'  # Initially hidden
    }))

    def clean(self):
        cleaned_data = super().clean()
        category = cleaned_data.get('category')
        other_category = cleaned_data.get('other_category')

        # If 'Other' is selected and 'other_category' is not provided, raise an error
        if category == 'Other' and not other_category:
            raise forms.ValidationError("Please provide a custom category name.")
        
        return cleaned_data

class LoanTransactionForm(forms.ModelForm):
    class Meta:
        model = loanTransaction
        fields = ('payment',)