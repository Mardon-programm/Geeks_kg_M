from django.contrib import admin
from geeks_kg.models import AcademyInfo, Cours, ContactForm

# Register your models here.
admin.site.register(AcademyInfo)
admin.site.register(Cours)
admin.site.register(ContactForm)