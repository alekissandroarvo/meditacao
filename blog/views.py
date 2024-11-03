from django.shortcuts import render
from . import views
from datetime import date

# Create your views here.
def home(request):
    mes=['janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro']
    hoje=str(date.today().day)+" de "+mes[date.today().month-1]+" de "+str(date.today().year)
    return render(request, "home.html", {"mycontext": hoje})
