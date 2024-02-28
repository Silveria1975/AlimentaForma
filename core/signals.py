@receiver (post_save, sender=Profile)
def add_user_to_students_group (sender, instance, created, **kwargs):
    if created:
        try:
            group1 = Group.objects.get(name='estudiante')
        except Group.DoesNotExist:
            group1 = Group.objects.create(name='estudiante')
            group2 = Group.objects.create(name='profesor')
            group3 = Group.objects.create(name='empresa')
            group4 = Group.objects.create(name='administrativo')
        instance.user.groups.add(group1)