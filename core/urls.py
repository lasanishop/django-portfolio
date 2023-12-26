from django.urls import path
from .views import home_view, ls_detail_view
 

urlpatterns = [
    path('', home_view, name='home'),
    path('ls-project-details', ls_detail_view, name='ls-detail'),
]