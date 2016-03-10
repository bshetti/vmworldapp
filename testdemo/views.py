from django.http import HttpResponse
from .models import Mortgage
from django.template import loader

def index(request):
    mortgage = Mortgage.objects.get(name="Tom Corn")
    return HttpResponse("%s owes $%f!" % (mortgage.name, mortgage.amount))

def test(request):
    template = loader.get_template('testdemo/home.html')
    context = {}
    return HttpResponse(template.render(context, request))

def dashboard(request):
    template = loader.get_template('testdemo/dashboard_-_before.html')
    mortgage = Mortgage.objects.get(name="Tom Corn")
    context = { "name": mortgage.name, "owed" : "$" + "{:8,.0f}".format(mortgage.amount), "amount": mortgage.amount}
    return HttpResponse(template.render(context, request))

def dash2(request):
    template = loader.get_template('testdemo/dashboard_-_after.html')
    mortgage = Mortgage.objects.get(name="Tom Corn")
    context = { "name": mortgage.name, "owed" : "$" + "{:8,.0f}".format(mortgage.amount)}
    return HttpResponse(template.render(context, request))

