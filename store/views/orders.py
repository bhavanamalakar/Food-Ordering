from django.shortcuts import render, redirect
from django.views import View
from store.models.Customer import Customer
from store.models.Product import Product
from store.models.orders import order

class OrderView(View):
    def get(self,request):
        customer = request.session.get('customer')
        orders = order.get_orders_by_customer(customer)
        print(orders)
        return render(request,'orders.html',{'orders':orders})

