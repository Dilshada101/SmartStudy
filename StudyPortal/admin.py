from django.urls import path
from django.views.generic import TemplateView
from django.contrib import admin
from unfold.admin import ModelAdmin
from unfold.views import UnfoldModelAdminViewMixin
from django.contrib.auth import get_user_model
from django.db.models import Count
from .models import *

User= get_user_model()

from StudyPortal.models import (
    Institution,
    ParticipantInstitution,
    PortalUser,
    Book,
    ParticipantBook,
    Resource,
    Note,
    Course,
    Progress,
    Assignment
)




class CustomAdminView(UnfoldModelAdminViewMixin, TemplateView):
    title = "Custom Management"
    permission_required = ()  
    template_name = "studyportal/custom_admin_template.html"




@admin.register(Institution)
class InstitutionAdmin(ModelAdmin):
    def get_urls(self):
        custom_view = self.admin_site.admin_view(
            CustomAdminView.as_view(model_admin=self, title="Institution Management", permission_required=("studyportal.view_institution",))
        )
        return super().get_urls() + [
            path("institution/custom/", custom_view, name="institution_custom"),
        ]


@admin.register(ParticipantInstitution)
class ParticipantInstitutionAdmin(ModelAdmin):
    def get_urls(self):
        custom_view = self.admin_site.admin_view(
            CustomAdminView.as_view(model_admin=self, title="Participant Institution Management", permission_required=("studyportal.view_participantinstitution",))
        )
        return super().get_urls() + [
            path("participant-institution/custom/", custom_view, name="participantinstitution_custom"),
        ]


@admin.register(PortalUser)
class PortalUserAdmin(ModelAdmin):
    def get_urls(self):
        custom_view = self.admin_site.admin_view(
            CustomAdminView.as_view(model_admin=self, title="Portal User Management", permission_required=("studyportal.view_portaluser",))
        )
        return super().get_urls() + [
            path("portal-user/custom/", custom_view, name="portaluser_custom"),
        ]


@admin.register(Book)
class BookAdmin(ModelAdmin):
    def get_urls(self):
        custom_view = self.admin_site.admin_view(
            CustomAdminView.as_view(model_admin=self, title="Book Management", permission_required=("studyportal.view_book",))
        )
        return super().get_urls() + [
            path("book/custom/", custom_view, name="book_custom"),
        ]


@admin.register(ParticipantBook)
class ParticipantBookAdmin(ModelAdmin):
    def get_urls(self):
        custom_view = self.admin_site.admin_view(
            CustomAdminView.as_view(model_admin=self, title="Participant Book Management", permission_required=("studyportal.view_participantbook",))
        )
        return super().get_urls() + [
            path("participant-book/custom/", custom_view, name="participantbook_custom"),
        ]


@admin.register(Resource)
class ResourceAdmin(ModelAdmin):
    def get_urls(self):
        custom_view = self.admin_site.admin_view(
            CustomAdminView.as_view(model_admin=self, title="Resource Management", permission_required=("studyportal.view_resource",))
        )
        return super().get_urls() + [
            path("resource/custom/", custom_view, name="resource_custom"),
        ]


@admin.register(Note)
class NoteAdmin(ModelAdmin):
    def get_urls(self):
        custom_view = self.admin_site.admin_view(
            CustomAdminView.as_view(model_admin=self, title="Note Management", permission_required=("studyportal.view_note",))
        )
        return super().get_urls() + [
            path("note/custom/", custom_view, name="note_custom"),
        ]


@admin.register(Course)
class CourseAdmin(ModelAdmin):
    def get_urls(self):
        custom_view = self.admin_site.admin_view(
            CustomAdminView.as_view(model_admin=self, title="Course Management", permission_required=("studyportal.view_course",))
        )
        return super().get_urls() + [
            path("course/custom/", custom_view, name="course_custom"),
        ]


@admin.register(Progress)
class ProgressAdmin(ModelAdmin):
    def get_urls(self):
        custom_view = self.admin_site.admin_view(
            CustomAdminView.as_view(model_admin=self, title="Progress Management", permission_required=("studyportal.view_progress",))
        )
        return super().get_urls() + [
            path("progress/custom/", custom_view, name="progress_custom"),
        ]


@admin.register(Assignment)
class AssignmentAdmin(ModelAdmin):
    def get_urls(self):
        custom_view = self.admin_site.admin_view(
            CustomAdminView.as_view(model_admin=self, title="Assignment Management", permission_required=("studyportal.view_assignment",))
        )
        return super().get_urls() + [
            path("assignment/custom/", custom_view, name="assignment_custom"),
        ]
    



class CustomDashboardView(TemplateView):
    title = "SmartStudy Dashboard"   
    permission_required = ()         
    template_name = "admin/custom_dashboard.html"
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["stats"] = {
            "users": User.objects.count(),
            "courses": Course.objects.count(),
            "assignments": Assignment.objects.count(),
            "books": Book.objects.count(),
            "notes": Note.objects.count(),  # you were using stats.notes in template
            "progress": Progress.objects.count(),  # for student
            "overall": User.objects.count() + Course.objects.count(),  # for teacher stats
        }
        ctx["recent_users"] = User.objects.order_by("-date_joined")[:5]
        ctx["recent_courses"] = Course.objects.order_by("-id")[:5]

        # Add groups
        ctx["user_groups"] = [g.name for g in self.request.user.groups.all()]

        # Add books/documents for student dashboard
        ctx["books"] = Book.objects.all()  # filter if needed
        ctx["documents"] = Resource.objects.all()  # assuming Resource model

        return ctx



def get_custom_urls(admin_site):
    return [
        path(
            "dashboard/",
            admin_site.admin_view(CustomDashboardView.as_view()),
            name="custom_dashboard",
        ),
    ]

_original_get_urls = admin.site.get_urls

def new_get_urls():
    return get_custom_urls(admin.site) + _original_get_urls()

admin.site.get_urls = new_get_urls




