from django.contrib import admin

from .models import Film, People, Planet, Species, Starship, Vehicle

classes = [People, Planet, Film, Starship, Vehicle, Species]

for c in classes:
    admin.site.register(c)
