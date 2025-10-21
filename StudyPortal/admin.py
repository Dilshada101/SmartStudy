from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from unfold.admin import ModelAdmin
from unfold.views import UnfoldModelAdminViewMixin
from django.contrib.auth import get_user_model
from django.db.models import Count
from .models import *
from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render,redirect

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
# class ProgressAdmin(admin.ModelAdmin):
#     list_display = ('student','student_name','course', 'subject', 'progress_percent', 'show_progress_bar', 'last_updated')

#     def show_progress_bar(self, obj):
#         """Display a small colored progress bar in admin list view."""
#         color = "#4CAF50" if obj.progress_percent >= 70 else "#FFA500"
#         return format_html(
#             '<div style="width:100px; background:#ddd; border-radius:5px;">'
#             '<div style="width:{}%; background:{}; color:white; padding:2px 0; border-radius:5px; text-align:center;">{}%</div>'
#             '</div>',
#             obj.progress_percent, color, obj.progress_percent
#         )

#     show_progress_bar.short_description = "Progress"

class CustomProgressView(TemplateView):
    template_name = 'admin/customprogress.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_dat(**kwargs)
        progress = Progress.objects.all().order_by('-subject')
        context['progress'] = progress
        return context

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
            "notes": Note.objects.count(),  
            "progress": Progress.objects.count(),  
            "overall": User.objects.count() + Course.objects.count(),  
        }
        ctx["recent_users"] = User.objects.order_by("-date_joined")[:5]
        ctx["recent_courses"] = Course.objects.order_by("-id")[:5]

        # Add groups
        ctx["user_groups"] = [g.name for g in self.request.user.groups.all()]

        # Add books/documents for student dashboard
        ctx["books"] = Book.objects.all()
        ctx["documents"] = Resource.objects.all()  

        return ctx
    

@method_decorator(staff_member_required, name='dispatch')
class CustomAssignmentsView(TemplateView):
    template_name = 'admin/custom_assignments.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        assignments = Assignment.objects.all().order_by('-due_date')
        context['assignments'] = assignments
        return context
    
@method_decorator(staff_member_required, name='dispatch')
class CustomNotesView(TemplateView):
    template_name = 'admin/custom_notes.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        notes = Note.objects.all().order_by('-uploaded_by')
        context['notes'] = notes
        return context

@method_decorator(staff_member_required, name='dispatch')
class CustomResourcesView(TemplateView):
    template_name = 'admin/custom_resources.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        resources = Resource.objects.all().order_by('-uploaded_by')
        books = Book.objects.all().order_by('-uploaded_by')
        context['resources'] = resources
        context['books'] = books
        return context


def get_custom_urls(admin_site):
    return [
        path(
            "dashboard/",
            admin_site.admin_view(CustomDashboardView.as_view()),
            name="custom_dashboard",
        ),
        path(
            "assignments/",
            admin_site.admin_view(CustomAssignmentsView.as_view()),
            name="custom_assignments",
        ),
        path(
            "notes/",
            admin_site.admin_view(CustomNotesView.as_view()),
            name="custom_notes",
        ),
        path(
            "resources/",
            admin_site.admin_view(CustomResourcesView.as_view()),
            name="custom_resources",
        ),
        
    ]

_original_get_urls = admin.site.get_urls

def new_get_urls():
    return get_custom_urls(admin.site) + _original_get_urls()

admin.site.get_urls = new_get_urls



