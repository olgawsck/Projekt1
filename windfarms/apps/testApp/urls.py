from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('company/<int:company_id>/', views.company_inspect, name='company_inspect'),
    path('windfarm/<int:windfarm_id>/', views.windfarm_inspect, name='windfarm_inspect'),
    path('turbine/<int:turbine_id>/', views.turbine_inspect, name='turbine_inspect'),
    # path('login/', views.LoginFormView, name='login'),
]
