from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.db import models

class User(AbstractUser):
    class Meta:
        verbose_name = 'usuario'
        verbose_name_plural = 'usuarios'

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='core_user_groups',
        blank=True,
        verbose_name='Grupos'
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='core_user_permissions',
        blank=True,
        verbose_name='Permisos'
    )

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', verbose_name='Usuario')
    image = models.ImageField(default='defaul-user.svg', upload_to='user/', verbose_name='imagen de perfil')
    address = models.CharField(max_length=150, null=True, blank=True, verbose_name='Dirección')
    location = models.CharField(max_length=150, null=True, blank=True, verbose_name='Localidad')
    telephone = models.CharField(max_length=50, null=True, blank=True, verbose_name='Teléfono')
    created_by_admin = models.BooleanField(default=True, blank=True, verbose_name='Creado por Admin')
    age = models.IntegerField(blank=True, null=True, verbose_name='Edad')
    city = models.CharField(max_length=50, blank=True, verbose_name='Localidad')
    preferred_language = models.CharField(max_length=50, blank=True)  # Ver si puede elegir cualquier idioma o está limitado,
    # es necesario?

    class Meta:
        verbose_name = 'perfil'
        verbose_name_plural = 'perfiles'
        ordering = ['-id']

    def __str__(self):
        return self.user.username

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

post_save.connect(create_user_profile, sender=User)
post_save.connect(save_user_profile, sender=User)

class Course(models.Model):
    STATUS_CHOICES = (
        ('i', 'En inscripción'),
        ('p', 'En progreso'),
        ('f', 'Finalizado')
    )

    name = models.CharField(max_length=90, verbose_name='Nombre')
    description = models.CharField(max_length=500, blank=True, null=True, verbose_name='Descripción')
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'groups__name': 'profesores'},
                                verbose_name='Profesor')
    class_quantity = models.PositiveIntegerField(default=0, verbose_name='Cantidad de clases')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='i', verbose_name='Estado')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'curso'
        verbose_name_plural = 'cursos'

class Announcement(models.Model):
    STATUS_CHOICES = (
        ('v', 'vigente'),
        ('f', 'Finalizado')
    )
    name = models.CharField(max_length=90, verbose_name='Nombre')
    description = models.CharField(max_length=500, blank=True, null=True, verbose_name='Descripción')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='i', verbose_name='Estado')

    class Meta:
        verbose_name = 'anuncio'
        verbose_name_plural = 'anuncios'

    def __str__(self):
        return self.name
    
class Registration(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Curso')
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='students_registration',
                                limit_choices_to={'groups__name': 'estudiante'}, verbose_name='Estudiante')
    enabled = models.BooleanField(default=True, verbose_name='Alumno Regular')

    def __str__(self):
        return f'{self.student.username} - {self.course.name}'

    class Meta:
        verbose_name = 'Inscripcion'
        verbose_name_plural = 'Inscripciones'

class Mark(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Curso')
    student = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'groups__name': 'estudiante'},
                                verbose_name='Estudiante')
    mark_1 = models.PositiveIntegerField(null=True, blank=True, verbose_name='Nota 1')
    mark_2 = models.PositiveIntegerField(null=True, blank=True, verbose_name='Nota 2')
    mark_3 = models.PositiveIntegerField(null=True, blank=True, verbose_name='Nota 3')
    average = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True, verbose_name='Promedio')

    def __str__(self):
        return str(self.course)

    # Calcular el promedio de las notas
    def calculate_average(self):
        marks = [self.mark_1, self.mark_2, self.mark_3]
        valid_marks = [mark for mark in marks if mark is not None]
        if valid_marks:
            return sum(valid_marks) / len(valid_marks)
        return None

    def save(self, *args, **kwargs):
        if self.mark_1 or self.mark_2 or self.mark_3:
            self.average = self.calculate_average()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Nota'
        verbose_name_plural = 'Notas'

class Suscription(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='suscription',
                                limit_choices_to={'groups__name': 'estudiante'}, verbose_name='Estudiante')
    date = models.DateField(null=True, blank=True, verbose_name='Fecha')
    payment = models.BooleanField(default=False, blank=True, null=True, verbose_name='Pago')
    
    class Meta:
        verbose_name = 'suscripción'
        verbose_name_plural = 'suscripciones'