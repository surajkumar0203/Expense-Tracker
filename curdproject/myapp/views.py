from django.shortcuts import render,redirect
from myapp.models import Transaction
from django.contrib import messages
from django.db.models import aggregates,Sum
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required,login_not_required
from myapp.utils import redirect_if_not_authenticated

@login_required(login_url="/")
def home(request):
    if request.method=='POST':
        post=request.POST
        expense_id=post.get('expense_id',None)
        expense_name=post.get('expense_name',None)
        amount=post.get('amount',None)
        category=post.get('category',None)
        
        # update expense
        if expense_id:
            transactions=Transaction.objects.get(uuid=expense_id)
            transactions.expance_name=expense_name
            transactions.amount=amount
            transactions.category=category
            transactions.save()
            return redirect('/home/')
        # new expense
        if expense_name is not None and amount is not None and category is not None:
            amount=float(amount)
            Transaction.objects.create(expance_name=expense_name,amount=amount,category=category,user=request.user)
        return redirect('/home/')
    
    
    transactions=Transaction.objects.filter(user=request.user)
    income=Transaction.objects.filter(user=request.user,amount__gt=0).aggregate(income=Sum('amount'))
    expance=Transaction.objects.filter(user=request.user,amount__lt=0).aggregate(expance=Sum('amount'))
    
    balance=transactions.aggregate(total=Sum('amount'))['total'] or 0
    expance_balance=expance['expance'] or 0
    income_balance=income['income'] or 0
    

    context={
        'transactions':transactions,
        'balance':format(balance,".2f"),
        'income':format(income_balance,".2f"),
        'expance':format(expance_balance,".2f"),
        'username':request.user
    }
    return render(request,'myapp/home.html',context)

@login_required(login_url="/")
def delete_expence(request,uuid):
    Transaction.objects.get(uuid=uuid).delete()
    return redirect("/home/")

@redirect_if_not_authenticated()
def ragistration(request):
    if(request.method=="POST"):
        username=request.POST.get('username')
        password=request.POST.get('password')
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        email=request.POST.get('email')

        # When user already exists
        if User.objects.filter(username=username).exists():
            messages.error(request,"username already exists")
            return redirect('/ragister/')
        
        user=User(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email
        )
        user.set_password(password)
        user.save()
        return redirect('/')
    return render(request,'myapp/ragister.html')


@redirect_if_not_authenticated()
def login_page(request):
    if(request.method=="POST"):
        username=request.POST.get('username')
        password=request.POST.get('password')
        
        user=authenticate(username=username,password=password)
        
        if(not user):
            messages.error(request,"Login Failed")
            return redirect('/')
        
        login(request,user)
        return redirect('/home/')
    return render(request,'myapp/login.html')

@login_required(login_url="/")
def logout_page(request):
    logout(request)
    return redirect('/')