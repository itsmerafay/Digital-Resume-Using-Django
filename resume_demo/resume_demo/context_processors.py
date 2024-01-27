
# context processors are a way to make certain data available globally across all the templates in django project

from django.contrib.auth.models import User

def project_context(request):
    context = {
        'me':User.objects.first(),
    }

    return context