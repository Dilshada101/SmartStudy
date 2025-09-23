from django.db import models
from django.contrib.auth.models import User

class Institution(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()

    def __str__(self):
        return self.name    


class PortalUser(models.Model):
    ROLE_CHOICES=[
        ("student", "Student"),
        ("teacher", "Teacher"),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)  
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    profile_pic = models.ImageField(upload_to='profiles/', null=True, blank=True)
    institution = models.ForeignKey(Institution, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.get_role_display()} ({self.institution})"
        return f"{self.user.username} - {self.get_role_display()}({self.institution})"



class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    uploaded_by = models.ForeignKey(Institution, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class ParticipantBook(models.Model):
    participant = models.ForeignKey(PortalUser, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    issued_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.participant.user.username} -> {self.book.title}"



class Resource(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    uploaded_by = models.ForeignKey(PortalUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Note(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    uploaded_by = models.ForeignKey(PortalUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.title



class Course(models.Model):
    name = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.institution.name})"



class Progress(models.Model):
    student = models.ForeignKey(PortalUser, on_delete=models.CASCADE, limit_choices_to={'role': 'student'})
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    progress_percent = models.FloatField(default=0.0)

    def __str__(self):
        return f"{self.student.user.username} - {self.course.name}"


class Assignment(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    assigned_by = models.ForeignKey(PortalUser, on_delete=models.CASCADE, related_name="given_assignments")
    assigned_to = models.ForeignKey(PortalUser, on_delete=models.CASCADE, related_name="received_assignments")
    score = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.title


class ParticipantInstitution(models.Model):
    participant = models.ForeignKey(PortalUser, on_delete=models.CASCADE)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    joined_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.participant.user.username} -> {self.institution.name}"
