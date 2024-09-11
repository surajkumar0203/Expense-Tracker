from django.shortcuts import render,redirect
from myapp.models import Transaction
from django.contrib import messages
from django.db.models import aggregates,Sum

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
            return redirect('/')
        # new expense
        if expense_name is not None and amount is not None and category is not None:
            amount=float(amount)
            Transaction.objects.create(expance_name=expense_name,amount=amount,category=category)
        return redirect('/')
    
    transactions=Transaction.objects.all()
    income=Transaction.objects.filter(amount__gt=0).aggregate(income=Sum('amount'))
    expance=Transaction.objects.filter(amount__lt=0).aggregate(expance=Sum('amount'))
    
    balance=transactions.aggregate(total=Sum('amount'))['total'] or 0
    expance_balance=expance['expance'] or 0
    income_balance=income['income'] or 0
    

    context={
        'transactions':transactions,
        'balance':format(balance,".2f"),
        'income':format(income_balance,".2f"),
        'expance':format(expance_balance,".2f"),
    }
    return render(request,'myapp/home.html',context)



def delete_expence(request,uuid):
    Transaction.objects.get(uuid=uuid).delete()
    return redirect("/")

