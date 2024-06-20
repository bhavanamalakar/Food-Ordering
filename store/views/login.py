from django.shortcuts import render, redirect
from store.models import Customer
from django.views import View

class Login(View):
    def get(self, request):
        return render(request,'login.html')
    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(email)
        print(password)
        customer = Customer.get_customer_by_email(email)
        if customer:
            # flag = check_password(password,customer.password)
            # print(flag)
            # if flag:
            request.session['customer']=customer.id
            request.session['email']=customer.email
            return redirect('homepage')
            # else:
            # error_message='email or password Invalid'
        else:
            error_message = 'email or password Invalid'
        return render(request,'login.html',{'error':error_message})

def logout(request):
    request.session.clear()
    return redirect('login')