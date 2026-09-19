from courses.forms.course import CourseForm
from courses.models import Course

def list_courses(request):
    courses = Course.objects.all()
    context = {
        'courses': courses
    }
    return render(request, 'courses\list_courses.html', context)


def create_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_courses')

    else:
        form=CourseForm()
    return render(request, 'courses\create_course.html', {'form': form})

