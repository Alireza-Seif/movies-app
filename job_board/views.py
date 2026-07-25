from django.http import HttpResponse

from .models import JobPosting


# Create your views here.
def index(request):
    # jobs = JobPosting.objects.all()
    jobs = JobPosting.objects.filter(is_active=True)
    print(jobs)
    return HttpResponse("<h1>hi</h1>")
