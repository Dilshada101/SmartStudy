from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import Assignment, Progress

def send_notification_email(subject, message, recipients):
    send_mail(
        subject,
        message,
        'no-reply@smartstudy.com',  # from email
        recipients,
        fail_silently=False,
    )

@receiver(post_save, sender=Assignment)
def assignment_created(sender, instance, created, **kwargs):
    if created:
        recipients = [instance.assigned_to.email]  # single student
        subject = f"New Assignment: {instance.title}"
        
        # Include assignment_file link if it exists
        file_link = f"\nDownload assignment file: {instance.assignment_file.url}" if instance.assignment_file else ""
        
        message = f"Dear {instance.assigned_to.user.username},\n\nA new assignment '{instance.title}' has been assigned to you.\nDue Date: {instance.due_date}{file_link}\n\nPlease check the portal for more details."
        send_notification_email(subject, message, recipients)
        


@receiver(post_save, sender=Progress)
def progress_created(sender, instance, created, **kwargs):
    if created:
        student_email = instance.student.email
        subject = f"Progress Updated: {instance.subject}"
        message = f"Dear {instance.student.user.username},\n\nYour progress in '{instance.subject}' has been updated to {instance.progress_percent}%."
        send_notification_email(subject, message, [student_email])

