from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission, User
from django.contrib.contenttypes.models import ContentType
from StudyPortal.models import PortalUser,Institution # make sure app name is lowercase

class Command(BaseCommand):
    help = "Create Teacher and Student groups, users, and portal profiles"

    def handle(self, *args, **kwargs):
        # 1️⃣ Define groups
        groups = ["Teacher", "Student"]
        for group_name in groups:
            group, created = Group.objects.get_or_create(name=group_name)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Group "{group_name}" created.'))
            else:
                self.stdout.write(self.style.WARNING(f'Group "{group_name}" already exists.'))

        # 2️⃣ Assign permissions
        teacher_group = Group.objects.get(name="Teacher")
        student_group = Group.objects.get(name="Student")

        teacher_permissions = Permission.objects.all()  # You can filter for specific models if needed
        teacher_group.permissions.set(teacher_permissions)
        teacher_group.save()

        student_permissions = Permission.objects.filter(codename__startswith="view_")
        student_group.permissions.set(student_permissions)
        student_group.save()

        self.stdout.write(self.style.SUCCESS("Permissions assigned successfully!"))

        # 3️⃣ Create Users and Portal Profiles
        teacher_names = ["Ilyas", "Bisma", "Aafaq", "Auqib", "Parvaz"]
        student_names = ["Zuha", "Muskan", "Dilshada", "Amarah", "Falak"]
        institution_name = "Govt College Of Engineering And Technology"
        institution_obj, created = Institution.objects.get_or_create(name=institution_name)


        # Teachers
        for username in teacher_names:
            user, created = User.objects.get_or_create(username=username)
            if created:
                user.set_password("password123")  # default password
                user.save()
                user.groups.add(teacher_group)
                PortalUser.objects.create(user=user, institution=institution_obj)
                self.stdout.write(self.style.SUCCESS(f'Teacher user "{username}" created.'))

        # Students
        for username in student_names:
            user, created = User.objects.get_or_create(username=username)
            if created:
                user.set_password("password123")  # default password
                user.save()
                user.groups.add(student_group)
                PortalUser.objects.create(user=user, institution=institution_obj)
                self.stdout.write(self.style.SUCCESS(f'Student user "{username}" created.'))

        self.stdout.write(self.style.SUCCESS("All users and portal profiles created successfully!"))
