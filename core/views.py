from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.forms import forms
from django.shortcuts import render, redirect
#from .models import Profile

def plural_to_singular (plural):
    plural_singular = {
        'estudiantes': 'estudiante',
        'profesores': 'profesor',
        'preceptores': 'preceptor',
        'administrativos': 'administrativo',
    }
    return plural_singular.get(plural, 'error')

# Obtener color y grupo de usuario
def get_group_and_color (user):
    group = user.groups.first()
    group_id = None
    group_name = None
    group_name_singular = None
    color = None        
    if group:
        if group.name == 'estudiantes':
            color = 'bg-primary'
        elif group.name == 'profesores':
            color = 'bg-success'
        elif group.name == 'preceptores':
            color = 'bg-secondary'
        elif group.name == 'administrativos':
            color = 'bg-danger'
        
        group_id = group.id        
        group_name = group.name
        group_name_singular = plural_to_singular(group.name) 
        
    return group_id, group_name, group_name_singular, color

def add_group_name_to_context (view_class):
    original_dispatch = view_class.dispatch
    
    def dispatch (self, request, *args, **kwargs):
        user = self.request.user
        group_id, group_name, group_name_singular, color = get_group_and_color(user)
        
        context = {
            'group_name': group_name,
            'group_name_singular': group_name_singular,
            'color': color,
        }    
        
        self.extra_context = context
        return original_dispatch (self, request, *args, **kwargs)
    
    view_class.dispatch = dispatch
    return view_class


#Vista para la página de inicio.
class HomeView (TemplateView):
    template_name = 'home.html'

# Vista pagina de cursos
class CoursesView (TemplateView):
    template_name = 'courses.html'

# Vista pagina de anuncios
class AnnouncementsView (TemplateView):
    template_name = 'announcements.html'

# Vista de Inicio de sesión
class LoginView (TemplateView):
    template_name = './register/login.html'
    
class RegisterView (TemplateView):
    template_name = './register/register.html'










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
