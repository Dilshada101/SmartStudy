from django.contrib import admin
from django.urls import path, include
from StudyPortal import views as study_views

urlpatterns = [ 
    path('admin/', admin.site.urls),
    path('', include('StudyPortal.urls')),  # main app handles home and others
    path('register/', study_views.register, name='register'),

    # Optional: admin dashboards (if you have these views)
    path('admin/assignments/', study_views.assignment_dashboard, name='admin_assignment_dashboard'),
    path('admin/notes/', study_views.notes_dashboard, name='admin_notes_dashboard'),
    path('admin/progress/', study_views.progress_dashboard, name='admin_progress_dashboard'),
    path('admin/resources/', study_views.resources_dashboard, name='admin_resources_dashboard'),
    path('admin/course/', study_views.course_dashboard, name='admin_course_dashboard'),
    path('admin/user/', study_views.user_dashboard, name='admin_user_dashboard'),
    path('chat/', include('chat.urls')),
    ]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
