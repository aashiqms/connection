from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views
from accounts.views import ProfileCreateView,\
    ProfileUpdateView,\
    ProfileDeleteView,\
    ProfileDetailView,\
    ProfileListView,\
    NewsFeed

app_name = 'accounts'


urlpatterns = [
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('accounts/logout/', LogoutView.as_view(), name='logout', kwargs={'next_page': '/'}),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('', views.SignupTemplateView.as_view(), name='signup_home'),
    path('userprofile/list/', ProfileListView.as_view(), name='list'),
    path('userprofile/<int:pk>/', ProfileDetailView.as_view(), name='detail'),
    path('userprofile/create/', ProfileCreateView.as_view(), name='create'),
    path('userprofile/<int:pk>/update/', ProfileUpdateView.as_view(), name='update'),
    path('userprofile/<int:pk>/delete/', ProfileDeleteView.as_view(), name='delete'),
    path('userprofile/', NewsFeed.as_view(), name='newsfeed')

]
