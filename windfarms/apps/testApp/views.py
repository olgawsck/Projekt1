from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View

from .forms import NameForm
from .models import Company, Windfarm, WindmillPowerPlant


def index(request):
    company_list = Company.objects.order_by('name')
    windfarm_list = Windfarm.objects.order_by('name')
    powerplant_list = WindmillPowerPlant.objects.order_by('name')
    context = {'company_list': company_list, 'windfarm_list': windfarm_list, 'powerplant_list': powerplant_list}
    return render(request, "registration/index.html", context)


def company_inspect(request, company_id):
    company = get_object_or_404(Company, pk=company_id)
    windfarm_list = Windfarm.objects.filter(owner=company)
    context = {'company': company, 'windfarm_list': windfarm_list}
    return render(request, "company_inspect.html", context)


@login_required(redirect_field_name='index.html')
def windfarm_inspect(request, windfarm_id):
    windfarm = get_object_or_404(Windfarm, pk=windfarm_id)
    windfarm_owner = Company.objects.get(windfarm__name=windfarm.name)
    powerplant_list = WindmillPowerPlant.objects.filter(parentFarm=windfarm)
    output_sum = WindmillPowerPlant.objects.all().aggregate(Sum('output'))
    context = {'output_sum': output_sum, 'windfarm': windfarm, 'powerplant_list': powerplant_list,
               'windfarm_owner': windfarm_owner}
    return render(request, "windfarm_inspect.html", context)


@login_required(redirect_field_name='index.html')
def turbine_inspect(request, turbine_id):
    turbine = get_object_or_404(WindmillPowerPlant, pk=turbine_id)
    turbineParentFarm = Windfarm.objects.get(windmillpowerplant__name=turbine.name)
    windfarm_owner = Company.objects.get(windfarm__name=turbineParentFarm.name)
    context = {'turbine': turbine, 'turbineParentFarm': turbineParentFarm, 'windfarm_owner': windfarm_owner}
    return render(request, "turbine_inspect.html", context)


class LoginFormView(View):
    def get(self, request):
        form = NameForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        form = NameForm(request.POST)
        if form.is_valid():
            login = form.cleaned_data['login']
            # procesowanie danych
            return HttpResponseRedirect('/thanks/')


def try_login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return render(request, 'index.html')
    else:
        return render(request, 'login_error.html')


def logout_view(request):
    logout(request)
    return render(request, 'index.html')
