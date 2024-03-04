from django.shortcuts import render
from django.http import HttpResponse

def test(response):
    """Sample view for testing."""

    return HttpResponse("test view in dna lab working")


