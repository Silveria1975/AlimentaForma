from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.forms import forms
from django.shortcuts import render, redirect

#from .models import Profile

#Vista para la página de inicio.
class HomeView (TemplateView):
    template_name = 'home.html'

# @login_required
# def home(request):
   
    
    
#     user = request.user
#     profile = Profile.objects.get(user=user)

#     context = {
#         'user': user,
#         'profile': profile,
#     }
#     return render(request, 'core/home.html', context)


# class ProfileForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ['field1', 'field2', ...]  # Indicar los campos del perfil a editar


# @login_required
# def profile_edit(request, context=None):
    
#     #Vista para editar el perfil de usuario.
    
#     user = request.user
#     profile = Profile.objects.get(user=user)

#     if request.method == 'POST':
#         form = ProfileForm(request.POST, instance=profile)
#         if form.is_valid():
#             try:
#                 form.save()
#                 return redirect('home')
#             except Exception as e:
#                 # Mostrar un mensaje de error al usuario
#                 context['error'] = str(e)
#     else:
#         form = ProfileForm(instance=profile)

#     context = {
#         'user': user,
#         'profile': profile,
#         'form': form,
#     }
#     return render(request, 'core/profile_edit.html', context)
