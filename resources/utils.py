from .models import (
    Film,
    People,
    Planet,
    Species,
    Starship,
    Vehicle,
)


def get_resource_stats():
    return {
        "people": People.objects.count(),
        "planets": Planet.objects.count(),
        "films": Film.objects.count(),
        "species": Species.objects.count(),
        "vehicles": Vehicle.objects.count(),
        "starships": Starship.objects.count(),
    }
