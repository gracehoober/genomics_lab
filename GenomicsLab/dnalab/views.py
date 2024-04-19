from django.shortcuts import render
from django.http import HttpResponse
from dnalab.models import Sequence, Specimen

def test(response):
    """Sample view for testing."""

    return HttpResponse("test view in dna lab working")


def specimen_entry(request):
    """Allows user to enter a new specimen."""

def sequence_entry(request):
    """Allows a user to enter a new sequence."""

def specimen_list(request):
    """Lists all specimens."""

    response = Specimen.objects.all()
    return HttpResponse(response)

def sequence_list(request):
    """List all sequences."""

def specimen_detail(request, specimen_id):
    """Lists a single specimen."""

    response = Specimen.objects.get(id=specimen_id)
    return HttpResponse(response)


def sequence_detail(request, sequence_id):
    """Lists a single sequence."""

    response = Sequence.objects.get(id=sequence_id)
    return HttpResponse(response)
