
from django.urls import path, include
from . import views
urlpatterns = [

    path('',views.home,name='home'),
    path('login/',views.loginH,name='login'),
    path('notes/',views.notes,name='notes'),
    path('os/',views.ost,name='os'),
    path('math/',views.math,name='math'),
    path('automata/',views.aut,name='automata'),
    path('coa/',views.coa,name='coa'),
    path('cnnd/',views.cnnd,name='cnnd'),
    path('python/',views.pythont,name='python'),
    path('logout/',views.logoutT,name='logout'),

]
