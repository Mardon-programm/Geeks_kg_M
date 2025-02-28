from django.shortcuts import render
from .models import AcademyInfo, Cours
from django.contrib import messages
from .forms import ContactForm, ContactFormForm
from django.shortcuts import redirect

# Create your views here.
def home(request):
    academy = AcademyInfo.objects.first()
    courses = Cours.objects.all()
    form = ContactFormForm()

    search_query = request.GET.get('search', '')
    if search_query:
        courses = courses.filter(title__icontains=search_query)  # Фильтруем по названию

    if request.method == "POST":
        form = ContactFormForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Ваша заявка успешно отправлена!")
            return redirect('home')

    return render(request, 'geeks_kg/home.html', {
        'academy': academy, 'courses': courses, 'form': form, 'search_query': search_query
    })

def about(request):
    return render(request, 'geeks_kg/about.html')
