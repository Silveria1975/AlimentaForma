from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, Course, Announcement, Registration, Mark, Suscription
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit

# Formulario de logueo (modelo de Django)
class LoginForm (AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')
        labels = {
            'username': 'user',
            'password': 'password'
        }

# Formularios de autenticación y creación de usuarios (predefinidos en Django)
class UserAuthenticationForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')
        labels = {
            'username': 'Username',
            'password': 'Password',
        }

# Formulario de creación de usuario
# class UserCreation(UserCreationForm):
#     email = forms.EmailField(required=True, label="Correo electrónico")

#     class Meta:
#         model = User
#         fields = ('username', 'email', 'password1', 'password2')
#         labels = {
#             'username': 'Nombre de usuario',
#             'email': 'Correo electrónico',
#             'password1': 'Contraseña',
#             'password2': 'Confirmar contraseña',
#         }

# Formularios para modelos personalizados
# class ProfileForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ('image', 'address', 'location', 'telephone', 'age', 'city', 'preferred_language')
#         labels = {
#             'image': 'Imagen de perfil',
#             'address': 'Dirección',
#             'location': 'Localidad',
#             'telephone': 'Teléfono',
#             'age': 'Edad',
#             'city': 'Ciudad',
#             'preferred_language': 'Idioma preferido',
#         }

# Formulario para Cursos
# class CourseForm(forms.ModelForm):
#     class Meta:
#         model = Course
#         fields = ('name', 'description', 'teacher', 'class_quantity', 'status')
#         labels = {
#             'name': 'Nombre',
#             'description': 'Descripción',
#             'teacher': 'Profesor',
#             'class_quantity': 'Cantidad de clases',
#             'status': 'Estado',
#         }

# Formulario para Anuncios
# class AnnouncementForm(forms.ModelForm):
#     class Meta:
#         model = Announcement
#         fields = ('name', 'description', 'status')
#         labels = {
#             'name': 'Nombre',
#             'description': 'Descripción',
#             'status': 'Estado',
#         }

# Formulario para Registros <<< RegisterView >>>
class RegisterForm(UserCreationForm):
    email = forms.EmailField (label = 'Correo Electrónico')
    first_name = forms.CharField (label = 'Nombre')
    last_name = forms.CharField (label = 'Apellido')
    
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']

    def clean_email (self):
        email_field = self.cleaned_data['email']

        if User.objects.filter (email = email_field).exists ():
            raise forms.ValidationError ('El correo ingresado ya existe.')
        return email_field

# Formulario para Notas
# class MarkForm(forms.ModelForm):
#     class Meta:
#         model = Mark
#         fields = ('course', 'student', 'mark_1', 'mark_2', 'mark_3')
#         labels = {
#             'course': 'Curso',
#             'student': 'Estudiante',
#             'mark_1': 'Nota 1',
#             'mark_2': 'Nota 2',
#             'mark_3': 'Nota 3',
#         }

# Formulario para Suscripciones
# class SuscriptionForm(forms.ModelForm):
#     class Meta:
#         model = Suscription
#         fields = ('student', 'date', 'payment')
#         labels = {
#             'student': 'Estudiante',
#             'date': 'Fecha',
#             'payment': 'Pago',
#         }

# Formulario para Estudiantes
# class StudentForm(forms.ModelForm):
#     class Meta:
#         model = Suscription
#         fields = ('student', 'date', 'payment')
#         labels = {
#             'student': 'Estudiante',
#             'date': 'Fecha',
#             'payment': 'Pago',
#         }

# Formulario para Empresas
# class EnterpriseForm(forms.ModelForm):
#     class Meta:
#         model = Suscription
#         fields = ('student', 'date', 'payment', 'enterprise',
#                   'enterprise_name', 'enterprise_email', 'enterprise_phone',
#                   'enterprise_address', 'teacher', 'teacher_name', 'teacher_email', 'teacher_phone')
#         labels = {
#             'student': 'Estudiante',
#             'date': 'Fecha',
#             'payment': 'Pago',
#             'enterprise': 'Empresa',
#             'enterprise_name': 'Nombre de la Empresa',
#             'enterprise_email': 'Email de la Empresa',
#             'enterprise_phone': 'Número de la Empresa',
#             'enterprise_address': 'Dirección de la Empresa',
#             'teacher': 'Teacher',
#             'teacher_name': 'Nombre',
#             'teacher_email': 'Email',
#             'teacher_phone': 'Teléfono',
#         }