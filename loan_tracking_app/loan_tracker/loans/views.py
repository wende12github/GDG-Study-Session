from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from registration.models import CustomerSignUp
from .forms import LoanRequestForm, LoanTransactionForm
from .models import loanCategory, loanRequest, loanTransaction, CustomerLoan
from django.shortcuts import redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.db import models

from django.db.models import Sum

# from loan_tracker.loans import models


# @login_required(login_url='/account/login-customer')
def home(request):

    return render(request, 'home.html', context={})


@login_required(login_url='/account/login-customer')
def LoanRequest(request):
    customer = models.ForeignKey(CustomerSignUp, on_delete=models.CASCADE, related_name='loan_customer')
    form = LoanRequestForm()

    if request.method == 'POST':
        form = LoanRequestForm(request.POST)

        if form.is_valid():
            loan_obj = form.save(commit=False)

            # Check if 'Other' was selected and add the new category
            if form.cleaned_data['category'] == 'Other' and form.cleaned_data['other_category']:
                # Create a new loan category for the custom one
                new_category = loanCategory.objects.create(loan_name=form.cleaned_data['other_category'])
                loan_obj.category = new_category  # Assign the new custom category

            # Set the current user as the customer for the loan request
            loan_obj.customer = request.user.customer
            loan_obj.save()
            return redirect('/')

    return render(request, 'loanTrackerApp/loanrequest.html', context={'form': form})

    # reason = request.POST.get('reason')
    # amount = request.POST.get('amount')
    # category = request.POST.get('category')
    # year = request.POST.get('year')
    # customer = request.user.customer

    # loan_request = LoanRequest(request)
    # loan_request.customer = customer
    # loan_request.save()
    # if form.is_valid():
    #     loan_request = form.save(commit=False)
    #     loan_request.customer = request.user.customer
    #     print(loan_request)
    #     return redirect('/')


@login_required(login_url='/account/login-customer')
def LoanPayment(request):
    form = LoanTransactionForm()
    if request.method == 'POST':
        form = LoanTransactionForm(request.POST)
        if form.is_valid():
            payment = form.save(commit=False)
            payment.customer = request.user.customer
            payment.save()
            # pay_save = loanTransaction()
            return redirect('/')

    return render(request, 'loanTrackerApp/payment.html', context={'form': form})


@login_required(login_url='/account/login-customer')
def UserTransaction(request):
    transactions = loanTransaction.objects.filter(
        customer=request.user.customer)
    return render(request, 'loanTrackerApp/user_transaction.html', context={'transactions': transactions})


@login_required(login_url='/account/login-customer')
def UserLoanHistory(request):
    loans = loanRequest.objects.filter(
        customer=request.user.customer)
    return render(request, 'loanTrackerApp/user_loan_history.html', context={'loans': loans})


@login_required(login_url='/account/login-customer')
def UserDashboard(request):
    
    # try:
    #     customer = request.user.customer
    # except Customer.DoesNotExist:
    #     return redirect('/account/signup-customer')
    
    requestLoan = loanRequest.objects.all().filter(
        customer=request.user.customer).count(),
    approved = loanRequest.objects.all().filter(
        customer=request.user.customer).filter(status='approved').count(),
    rejected = loanRequest.objects.all().filter(
        customer=request.user.customer).filter(status='rejected').count(),
    totalLoan = CustomerLoan.objects.filter(customer=request.user.customer).aggregate(Sum('total_loan'))[
        'total_loan__sum'],
    totalPayable = CustomerLoan.objects.filter(customer=request.user.customer).aggregate(
        Sum('payable_loan'))['payable_loan__sum'],
    totalPaid = loanTransaction.objects.filter(customer=request.user.customer).aggregate(Sum('payment'))[
        'payment__sum'],
    

    dict = {
        'request': requestLoan[0],
        'approved': approved[0],
        'rejected': rejected[0],
        'totalLoan': totalLoan[0],
        'totalPayable': totalPayable[0],
        'totalPaid': totalPaid[0],
        

    }

    return render(request, 'loanTrackerApp/user_dashboard.html', context=dict)


def error_404_view(request, exception):
    print("not found")
    return render(request, 'notFound.html')