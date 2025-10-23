from django.db import models
from django.contrib.auth.models import User
from django.db.models import Q
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
    file = models.FileField(upload_to='books/', blank=True, null=True)

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
    file = models.FileField(upload_to='resources/', blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Note(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    uploaded_by = models.ForeignKey(PortalUser, on_delete=models.CASCADE)
    file = models.FileField(upload_to='notes/', blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now=True)

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
    subject = models.CharField(max_length=100, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    progress_percent = models.FloatField(default=0.0, editable=False)

    def __str__(self):
        return f"{self.student.user.username} - {self.course.name}"

    def calculate_progress(self):
        """Auto-calculate progress based on completed assignments."""
        # Total assignments for the student's course
        total_assignments = Assignment.objects.filter(course=self.course).count()
        
        # Assignments completed by this student
        completed_assignments = Assignment.objects.filter(
            course=self.course,
            assigned_to=self.student,
        ).exclude(
            Q(submit_assignment__isnull=True) | Q(submit_assignment='')
        ).count()
        
        if total_assignments > 0:
            return round((completed_assignments / total_assignments) * 100, 2)
        return 0.0

    def save(self, *args, **kwargs):
        # Automatically update progress_percent before saving
        self.progress_percent = self.calculate_progress()
        super().save(*args, **kwargs)


class Assignment(models.Model):
    title = models.CharField(max_length=255)
    due_date = models.DateField(null=True)
    course = models.ForeignKey('Course', on_delete=models.CASCADE, related_name='assignments', null=True, blank=True)
    description = models.TextField(blank=True)
    assigned_by = models.ForeignKey(PortalUser, on_delete=models.CASCADE, related_name="given_assignments")
    assigned_to = models.ForeignKey(PortalUser, on_delete=models.CASCADE, related_name="received_assignments")
    uploaded_by = models.CharField(max_length=100, null=True)
    assignment_file = models.FileField(upload_to='assignments/', blank=True, null=True)
    submit_assignment = models.FileField(upload_to='assignments/', blank=True, null=True)

    def __str__(self):
        return self.title
    
class Semester(models.Model):
    name = models.CharField(max_length=100, unique=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='semesters')
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ['name']
        verbose_name = "Semester"
        verbose_name_plural = "Semesters"

    def __str__(self):
        return f"{self.name} - {self.course.name}"


class ParticipantInstitution(models.Model):
    participant = models.ForeignKey(PortalUser, on_delete=models.CASCADE)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    joined_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.participant.user.username} -> {self.institution.name}"
