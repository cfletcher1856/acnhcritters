from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from .models import Fish, Bug

from annoying.decorators import render_to

@render_to('index.html')
def index(request):
    return {}

@render_to('critters.html')
def bugs(request):
    bugs = Bug.objects.all()
    bugs_json = serializers.serialize("json", bugs)
    return {
        'critters_json': bugs_json,
        'critter_type': 'Bugs',
    }

@render_to('critters.html')
def fishes(request):
    fishes = Fish.objects.all()
    fishes_json = serializers.serialize("json", fishes)

    return {
        'critters_json': fishes_json,
        'critter_type': 'Fishes',
    }

@render_to('bug.html')
def bug(request, entity_id):
    bug = Bug.objects.get(entity_id=entity_id)
    return {
        'bug': bug
    }

@render_to('fish.html')
def fish(request, entity_id):
    return {}
