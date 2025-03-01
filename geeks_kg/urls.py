from . import views
from django.urls import path
from .views import home, about, course_detail, courses

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('courses/', courses, name='courses'),
    path('courses/<int:course_id>/', course_detail, name='course_detail'),

]
