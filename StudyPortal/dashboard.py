from .models import Assignment
def dashboard_callback(request, context):
    context.update(
        {
            "welcome_message": "Welcome to SmartStudy Dashboard",
            "stats": {
                "institutions": 12,
                "users": 340,
                "courses": 25,
            }
        }
    )
    return context


def environment_callback(request):
    return ["Production", "success"]  


def badge_callback(request):
    return Assignment.objects.filter(assigned_by =False).count()


def permission_callback(request):
    return request.user.has_perm("StudyPortal.change_institution")


