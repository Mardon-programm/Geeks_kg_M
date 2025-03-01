from django.shortcuts import render
from .models import AcademyInfo, Cours
from django.contrib import messages
from .forms import ContactForm, ContactFormForm  
from .models import Cours 
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

# Create your views here.
def home(request):
    academy = AcademyInfo.objects.first()
    courses = Cours.objects.all()  
    form = ContactFormForm()

    if request.method == "POST":
        form = ContactFormForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Ваша заявка успешно отправлена!")
            return redirect('home')

    return render(request, 'geeks_htmls/index.html', {
        'academy': academy,
        'courses': courses, 
        'form': form
    })



def about(request):
    return render(request, 'geeks_htmls/about.html')

def courses(request):
    all_courses = Cours.objects.all()
    return render(request, 'geeks_htmls/courses.html', {'courses': all_courses})

def course_detail(request, course_id):
    course = get_object_or_404(Cours, id=course_id)
    return render(request, 'geeks_htmls/course_detail.html', {'course': course})
