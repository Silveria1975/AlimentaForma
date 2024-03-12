from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.contrib.auth import authenticate, login, logout
from django.views.generic import TemplateView
from django.views import View
from django.forms import forms
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
#from .models import Profile

# Obtener color y grupo de usuario
def get_group_and_color (user):
    group = user.groups.first()
    group_id = None
    group_name = None
    color = None        
    if group:
        if group.name == 'estudiante':
            color = 'bg-primary'
        elif group.name == 'profesor':
            color = 'bg-success'
        elif group.name == 'empresa':
            color = 'bg-secondary'
        elif group.name == 'administrativo':
            color = 'bg-danger'
        
        group_id = group.id        
        group_name = group.name
        
    return group_id, group_name, color

def add_group_name_to_context (view_class):
    original_dispatch = view_class.dispatch
    
    def dispatch (self, request, *args, **kwargs):
        user = self.request.user
        group_id, group_name, color = get_group_and_color(user)
        
        context = {
            'group_name': group_name,
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
    
class RegisterView (View):
    def get (self, request):
        data = {
            'form': RegisterForm()
        }
        return render (request, 'register/register.html', data)

    def post (self, request):
        user_creation_form = RegisterForm(data = request.POST)
        if user_creation_form.is_valid():
            user_creation_form.save()
            user = authenticate( username = user_creation_form.cleaned_data['username'],
                                password = user_creation_form.cleaned_data['password1'])
            login (request, user)
            user.profile.created_by_admin = False
            user.profile.save()
            return redirect ('home')
        data = {
            'form': user_creation_form
        }
        return render(request, 'register/register.html', data)

# Login personalizado
@add_group_name_to_context
class CustomLoginView (LoginView):
    def get (self, request):
        data = {
            'form': LoginForm()
        }
        return render (request, 'register/login.html', data)
    
    form_class = LoginForm
    template_name = './register/login.html'
    
    def form_valid(self, form):
        response = super().form_valid(form)
        
        #Acceder al perfil del usuario
        profile = self.request.user.profile
        
        #Verificar el valor del campo created_by_admin
        if profile.created_by_admin:
            messages.info(self.request, 'Bienvenido, cambie su contraseña.')
            response ['Location'] = reverse_lazy('profile_password_change')
            response.status_code = 302
            
        return response
    
    def get_success_url (self):
        return super().get_success_url()

# CAMBIAR LA CONTRASEÑA DEL USUARIO
@add_group_name_to_context
class ProfilePasswordChangeView(PasswordChangeView):
    template_name = 'profile/change_password.html'
    success_url = reverse_lazy('profile')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['password_changed'] = self.request.session.get('password_changed', False)
        return context

    def form_valid(self, form):
        # Actualizar el campo created_by_admin del modelo Profile
        profile = Profile.objects.get(user=self.request.user)
        profile.created_by_admin = False
        profile.save()

        messages.success(self.request, 'Cambio de contraseña exitoso')
        update_session_auth_hash(self.request, form.user)
        self.request.session['password_changed'] = True
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(
            self.request,
            'Hubo un error al momento de intentar cambiar la contraseña: {}.'.format(
                form.errors.as_text()
            )
        )
        return super().form_invalid(form)





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
