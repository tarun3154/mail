from django.contrib import admin
from .models import *
from .forms import *
# Register your models here.
admin.site.register(Ingredient)
admin.site.register(Recipe)
