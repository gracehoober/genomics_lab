from django.urls import path
from . import views

urlpatterns = [
    path("", views.test, name="test"),
    path("sequences/", views.sequence_list, name="sequence_list"),
    path("specimens/", views.specimen_list, name="specimen_list"),
    path("specimens/<int:specimen_id>/", views.specimen_detail, name="specimen_detail"),
    path("sequences/<int:sequence_id>/", views.sequence_detail, name="sequence_detail"),

]
