from django.urls import path
from .views import CharityListView, DonationCreateView, register_user, login_user, logout_user

urlpatterns = [

    path('charities/', CharityListView.as_view(), name='charities'),
    path('donate/', DonationCreateView.as_view(), name='donate'),
    path('auth/register/', register_user, name='register'),
    path('auth/login/', login_user, name='login'),
    path('auth/logout/', logout_user, name='logout'),
]
