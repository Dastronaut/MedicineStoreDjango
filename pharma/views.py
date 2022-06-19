from .models import Customer
from .models import Medicine
from .models import Purchase
from django.shortcuts import render
from django.db import IntegrityError


def home(request):
    return render(request, 'pharma/index.html')


def dealerform(request):
    dict = {'add': True, }
    return render(request, 'pharma/dealer.html', dict)

def custform(request):
    dict = {'add': True}
    return render(request, 'pharma/cust.html', dict)


def custforminsert(request):
    try:
        cust = Customer()
        cust.fname = request.POST['fname']
        cust.lname = request.POST['lname']
        cust.address = request.POST['address']
        cust.phn_no = request.POST['pno']
        cust.email = request.POST['email']
        cust.save()
    except IntegrityError:
        return render(request, "pharma/new.html")
    return render(request, 'pharma/index.html')


def custformupdate(request, foo):
    try:
        cust = Customer.objects.get(pk=foo)
        cust.fname = request.POST['fname']
        cust.lname = request.POST['lname']
        cust.address = request.POST['address']
        cust.phn_no = request.POST['pno']
        cust.email = request.POST['email']
        cust.save()
    except IntegrityError:
        return render(request, "pharma/new.html")
    return render(request, 'pharma/index.html')


def custformview(request, foo):
    cust = Customer.objects.get(pk=foo)
    dict = {'cust': cust}
    return render(request, 'pharma/cust.html', dict)


def custformdelete(request, foo):
    cust = Customer.objects.get(pk=foo)
    cust.delete()
    return render(request, 'pharma/index.html')


def custtable(request):
    cust = Customer.objects.all()
    dict = {"cust": cust}
    return render(request, 'pharma/custtable.html', dict)


def medform(request):
    dict = {'add': True}
    return render(request, 'pharma/med.html', dict)


def medforminsert(request):
    try:
        med = Medicine()
        med.m_id = request.POST['mid']
        med.mname = request.POST['mname']
        med.desc = request.POST['desc']
        med.price = request.POST['price']
        med.stock = request.POST['stock']
        med.save()
    except IntegrityError:
        return render(request, "pharma/new.html")
    return render(request, 'pharma/index.html')


def medformupdate(request, foo):
    try:
        med = Medicine.objects.get(pk=foo)
        med.m_id = request.POST['mid']
        med.mname = request.POST['mname']
        med.desc = request.POST['desc']
        med.price = request.POST['price']
        med.stock = request.POST['stock']
        med.save()
    except IntegrityError:
        return render(request, "pharma/new.html")
    return render(request, 'pharma/index.html')


def medformview(request, foo):
    med = Medicine.objects.get(pk=foo)
    dict = {'med': med}
    return render(request, 'pharma/med.html', dict)


def medformdelete(request, foo):
    med = Medicine.objects.get(pk=foo)
    med.delete()
    return render(request, 'pharma/index.html')


def medtable(request):
    med = Medicine.objects.all()
    dict = {"med": med}
    return render(request, 'pharma/medtable.html', dict)


def purchaseform(request):
    dict = {'add': True}
    return render(request, 'pharma/purchase.html', dict)


def purchaseforminsert(request):
    try:
        purchase = Purchase()
        purchase.pname = request.POST['pname']
        purchase.fname = request.POST['fname']
        purchase.lname = request.POST['lname']
        purchase.qty = request.POST['qty']
        purchase.phn_no = request.POST['pno']
        purchase.price = request.POST['price']
        a = (int(purchase.price)) * (int(purchase.qty))
        purchase.total = a
        purchase.save()
    except IntegrityError:
        return render(request, "pharma/new.html")
    return render(request, 'pharma/index.html')


def purchaseformupdate(request, foo):
    try:
        purchase = Purchase.objects.get(pk=foo)
        purchase.pname = request.POST['pname']
        purchase.fname = request.POST['fname']
        purchase.lname = request.POST['lname']
        purchase.qty = request.POST['qty']
        purchase.phn_no = request.POST['pno']
        purchase.price = request.POST['price']
        a = (int(purchase.price)) * (int(purchase.qty))
        purchase.total = a
        purchase.save()
    except IntegrityError:
        return render(request, "pharma/new.html")
    return render(request, 'pharma/index.html')


def purchaseformview(request, foo):
    purchase = Purchase.objects.get(pk=foo)
    dict = {'purchase': purchase}
    return render(request, 'pharma/purchase.html', dict)


def purchaseformdelete(request, foo):
    purchase = Purchase.objects.get(pk=foo)
    purchase.delete()
    return render(request, 'pharma/index.html')


def purchasetable(request):
    purchase = Purchase.objects.all()
    dict = {"purchase": purchase}
    return render(request, 'pharma/purchasetable.html', dict)
