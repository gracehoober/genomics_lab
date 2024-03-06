from django.db import models
import uuid

class Specimen(models.Model):
    """DNA lab specimen class."""

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        unique=True
        )
    specimen_origin = models.CharField(max_length=20)
    submission_date = models.DateTimeField()
    notes = models.TextField(max_length=500)


# TODO: ensure a sequence cannot have the same specimen as another entry
class Sequence(models.Model):
    """DNA lab sequence class."""

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        unique=True
        )
    dna_sequence = models.TextField(max_length=500)
    specimen = models.ForeignKey(Specimen, on_delete=models.CASCADE)
    # experiment = models.ForeignKey(Experiment, on_delete=models.CASCADE)



# Future models:

# class Experiment(models.Model):
#     """Experiment class in DNA lab."""
#     id = models.UUIDField(
#         primary_key=True,
#         default=uuid.uuid4,
#         editable=False,
#         unique=True
#         )
#     name = models.CharField(max_length=20, unique=True)
#     date_range = models.DateField()
#     lead_scientist = models.

# class Scientist(models.Model):
#     """Scientist class in DNA lab."""

#     employee_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     first_name = models.CharField(max_length=20)
#     last_name = models.CharField(max_length=20)
#     education_level = models.RadioSelect(choices) #no degree, BS/BA, Masters, PHD
#     email = models.EmailField(max_length=40)
#     is_admin = models.BooleanField(CheckboxInput)

