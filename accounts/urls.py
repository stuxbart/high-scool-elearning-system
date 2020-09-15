from django.urls import path

from .views import login_view, logout_view, UserHomeView, UserDetailView

app_name = 'accounts'

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/', UserHomeView.as_view(), name='my_profile'),
    path('user/<pk>/', UserDetailView.as_view(), name="user_detail")
]
