
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
    return ["Production", "success"]  # Options: info, danger, warning, success


def badge_callback(request):
    return 5  # Example: show badge with number of pending tasks


def permission_callback(request):
    return request.user.has_perm("StudyPortal.change_institution")


