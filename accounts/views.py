from django.contrib.auth import login, logout, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, render
from django.template.context_processors import request
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, TemplateView, DetailView, RedirectView, UpdateView, ListView, DeleteView
from . forms import UserProfileCreateForm
from .models import UserProfile
from . forms import UserCreationForm, UserCreateForm
from weather.views import index

User = get_user_model()  # gets the user model of the current user present in this session


class SignUp(CreateView):
    """
     # class SignUp
        - we inherit from the generic CreateView to Create a Signup Form

     form_class:
        - we set the form_class(The form class to instantiate) to  UserCreate which we
          created in forms.py file which in turn inherits from the built in UserCreationForm.
     success_url:
        - The URL to redirect to when the form is successfully processed.
     template_name:
        - We could explicitly tell the view which template to use by adding a template_name attribute to the view, but
          in the absence of an explicit template Django will infer one from the object’s name.
    """
    form_class = UserCreateForm
    success_url = reverse_lazy("login")
    template_name = "accounts/signup.html"


class SignupTemplateView(TemplateView):
    """
    template_name:
        - we set the page to show when we visit the url path of this view
    """
    template_name = 'accounts/signup_base_template.html'


class ProfileCreateView(CreateView, LoginRequiredMixin):
    model = UserProfile
    form_class = UserProfileCreateForm
    login_url = '/login/'
    redirect_field_name = 'accounts/userprofile_detail.html'


class ProfileDetailView(DetailView, LoginRequiredMixin):
    model = UserProfile


class ProfileListView(ListView, LoginRequiredMixin):
    model = UserProfile

    def get_queryset(self):
        return UserProfile.objects.all()

    def get_name(self):
        name = UserProfile.objects.filter(active=True).values_list('name', flat=True)
        context = {
            'name_context': name
        }
        return render(request, 'accounts/userprofile_list.html', context)


class ProfileUpdateView(UpdateView, LoginRequiredMixin):
    model = UserProfile
    form_class = UserProfileCreateForm
    login_url = '/login/'
    redirect_field_name = 'accounts/userprofile_detail.html'


class ProfileDeleteView(DeleteView):
    model = UserProfile
    success_url = reverse_lazy('userprofile_list')


class ProfilePage(TemplateView):
    template_name = 'accounts/profile_page.html'






