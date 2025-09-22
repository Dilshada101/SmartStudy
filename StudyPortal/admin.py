# from django.contrib import admin
# from .models import *
# from unfold.admin import ModelAdmin
# from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin
# from django.contrib.auth.models import User, Group
# from unfold.forms import AdminPasswordChangeForm, UserChangeForm, UserCreationForm
# from django.db import models
# from django.contrib.postgres.fields import ArrayField
# from unfold.contrib.forms.widgets import ArrayWidget, WysiwygWidget






# admin.site.unregister(User)
# admin.site.unregister(Group)



# @admin.register(User)
# class UserAdmin(BaseUserAdmin, ModelAdmin):
#     form = UserChangeForm
#     add_form = UserCreationForm
#     change_password_form = AdminPasswordChangeForm

# @admin.register(Group)
# class GroupAdmin(BaseGroupAdmin, ModelAdmin):
#     pass



# @admin.register(Institution)
# class InstitutionAdmin(ModelAdmin):
#     list_display=("name","address")

# @admin.register(ParticipantInstitution)
# class ParticipantInstitutionAdmin(ModelAdmin):
#     list_display = ("participant", "institution", "joined_on")



# @admin.register(PortalUser)
# class PortalUserAdmin(ModelAdmin):
#     list_display=("user", "role", "institution")

# @admin.register(Book)
# class BookAdmin(ModelAdmin):
#     list_display=("title", "author", "uploaded_by")  

# @admin.register(ParticipantBook)
# class ParticipantBookAdmin(ModelAdmin):
#     list_display = ("participant", "book", "issued_on")


# @admin.register(Resource)
# class ResourceAdmin(ModelAdmin):
#     list_display = ("title", "uploaded_by")


# @admin.register(Note)
# class NoteAdmin(ModelAdmin):
#     list_display = ("title", "uploaded_by")


# @admin.register(Course)
# class CourseAdmin(ModelAdmin):
#     list_display = ("name", "department", "institution")


# @admin.register(Progress)
# class ProgressAdmin(ModelAdmin):
#     list_display = ("student", "course", "progress_percent")

# @admin.register(Assignment)
# class AssignmentAdmin(ModelAdmin):
#     list_display = ("title", "assigned_by", "assigned_to","score")




# from .models import (
#     Institution,
#     PortalUser,
#     Book,
#     Course,
#     Resource,
#     Note,
#     Assignment,
#     Progress,
# )

# # Common base config to reuse across all admins
# class BaseAdmin(ModelAdmin):
#     compressed_fields = True
#     warn_unsaved_form = True
#     list_filter_submit = False
#     list_fullwidth = False
#     list_filter_sheet = True
#     list_horizontal_scrollbar_top = False
#     list_disable_select_all = False
#     change_form_show_cancel_button = True

#     formfield_overrides = {
#         models.TextField: {"widget": WysiwygWidget},
#         ArrayField: {"widget": ArrayWidget},
#     }


# @admin.register(Institution)
# class InstitutionAdmin(BaseAdmin):
#     list_display = ("id", "name", "created_at")
#     search_fields = ("name",)

# @admin.register(ParticipantInstitution)
# class ParticipantInstitutionAdmin(BaseAdmin):
#     list_display = ("id", "portal_user", "institution", "joined_at")
#     list_filter = ("institution", "portal_user")
#     search_fields = ("portal_user_userusername", "institution_name")


# @admin.register(PortalUser)
# class PortalUserAdmin(BaseAdmin):
#     list_display = ("id", "user", "institution", "role")
#     list_filter = ("institution", "role")
#     search_fields = ("user_username", "user_email")


# @admin.register(Book)
# class BookAdmin(BaseAdmin):
#     list_display = ("id", "title", "author", "published_date")
#     search_fields = ("title", "author")

# @admin.register(ParticipantBook)
# class ParticipantBookAdmin(BaseAdmin):
#     list_display = ("id", "portal_user", "book", "assigned_at")
#     list_filter = ("book", "portal_user")
#     search_fields = ("portal_user_userusername", "book_title")



# @admin.register(Course)
# class CourseAdmin(BaseAdmin):
#     list_display = ("id", "name", "institution", "created_at")
#     list_filter = ("institution",)
#     search_fields = ("name",)


# @admin.register(Resource)
# class ResourceAdmin(BaseAdmin):
#     list_display = ("id", "title", "course", "uploaded_at")
#     list_filter = ("course",)
#     search_fields = ("title",)


# @admin.register(Note)
# class NoteAdmin(BaseAdmin):
#     list_display = ("id", "title", "user", "created_at")
#     list_filter = ("user",)
#     search_fields = ("title",)


# @admin.register(Assignment)
# class AssignmentAdmin(BaseAdmin):
#     list_display = ("id", "title", "course", "due_date")
#     list_filter = ("course",)
#     search_fields = ("title",)


# @admin.register(Progress)
# class ProgressAdmin(BaseAdmin):
#     list_display = ("id", "user", "course", "completion_percentage")
#     list_filter = ("course","user")



# from django.contrib import admin
# from .models import (
#     Institution,
#     PortalUser,
#     Book,
#     ParticipantBook,
#     Resource,
#     Note,
#     Course,
#     Progress,
#     Assignment,
#     ParticipantInstitution,
# )


# @admin.register(Institution)
# class InstitutionAdmin(admin.ModelAdmin):
#     list_display = ("id", "name", "address")
#     search_fields = ("name", "address")


# @admin.register(PortalUser)
# class PortalUserAdmin(admin.ModelAdmin):
#     list_display = ("id", "user", "role", "institution")
#     list_filter = ("role", "institution")
#     search_fields = ("user_username", "institution_name")


# @admin.register(Book)
# class BookAdmin(admin.ModelAdmin):
#     list_display = ("id", "title", "author", "uploaded_by")
#     search_fields = ("title", "author", "uploaded_by__name")
#     list_filter = ("uploaded_by",)


# @admin.register(ParticipantBook)
# class ParticipantBookAdmin(admin.ModelAdmin):
#     list_display = ("id", "participant", "book", "issued_on")
#     list_filter = ("issued_on", "book", "participant")


# @admin.register(Resource)
# class ResourceAdmin(admin.ModelAdmin):
#     list_display = ("id", "title", "uploaded_by")
#     search_fields = ("title", "uploaded_by_user_username")


# @admin.register(Note)
# class NoteAdmin(admin.ModelAdmin):
#     list_display = ("id", "title", "uploaded_by")
#     search_fields = ("title", "uploaded_by_user_username")


# @admin.register(Course)
# class CourseAdmin(admin.ModelAdmin):
#     list_display = ("id", "name", "department", "institution")
#     list_filter = ("department", "institution")
#     search_fields = ("name", "department", "institution__name")


# @admin.register(Progress)
# class ProgressAdmin(admin.ModelAdmin):
#     list_display = ("id", "student", "course", "progress_percent")
#     list_filter = ("course",)
#     search_fields = ("student_userusername", "course_name")


# @admin.register(Assignment)
# class AssignmentAdmin(admin.ModelAdmin):
#     list_display = ("id", "title", "assigned_by", "assigned_to", "score")
#     list_filter = ("assigned_by", "assigned_to")
#     search_fields = ("title", "assigned_by_userusername", "assigned_touser_username")


# @admin.register(ParticipantInstitution)
# class ParticipantInstitutionAdmin(admin.ModelAdmin):
#     list_display = ("id", "participant", "institution", "joined_on")
#     list_filter = ("institution", "joined_on")
#     search_fields = ("participant_userusername", "institution_name")



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
    permission_required = ()  # Override per model in admin class
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
    title = "SmartStudy Dashboard"   # shown in header
    permission_required = ()         # leave empty for superusers only
    template_name = "admin/custom_dashboard.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        # You can add dynamic data here for dashboard cards, charts etc.
        ctx["stats"] = {
            "users": User.objects.count(),
            "courses": Course.objects.count(),
            "assignments": Assignment.objects.count(),
            "books": Book.objects.count(),
        
        }
        ctx["recent_users"] = User.objects.order_by("-date_joined")[:5]
        ctx["recent_courses"] = Course.objects.order_by("-id")[:5]
        
        

        return ctx


# Register view under admin site root
def get_custom_urls(admin_site):
    return [
        path(
            "dashboard/",
            admin_site.admin_view(CustomDashboardView.as_view()),
            name="custom_dashboard",
        ),
    ]



# Hook custom URLs into global admin site
# Save original get_urls before overriding
_original_get_urls = admin.site.get_urls

def new_get_urls():
    return get_custom_urls(admin.site) + _original_get_urls()

# Replace with safe version
admin.site.get_urls = new_get_urls
