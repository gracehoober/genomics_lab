from django.urls import path
from . import views

urlpatterns = [
    path("", views.test, name="test"),
    path("specimens/<int:specimen_id>/", views.specimen_detail, name="specimen_detail"),
    path("sequences/<int:sequence_id>/", views.sequence_detail, name="sequence_detail"),

]
