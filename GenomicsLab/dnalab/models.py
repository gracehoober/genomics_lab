from django.db import models
import uuid

class Specimen(models.Model):
    """DNA lab specimen class."""

    id = models.
    specimen_origin = models.CharField()
    submission_date = models.DateTimeField()

class Experiment(models.Model):
    """Experiment class in DNA lab."""

    name = models.CharField()
    date_range = models.DateField()
    lead_scientist = models.CharField()


class Sequence(models.Model):
    """DNA lab sequence class."""

    id = models.CharField()
    specimen = models.ForeignKey(Specimen, on_delete=models.CASCADE)
    experiment = models.ForeignKey(Experiment, on_delete=models.CASCADE)


class Scientist(models.Model):
    """Scientist class in DNA lab."""

    employee_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField()
    last_name = models.CharField()
    seniority = models.
    email = models.EmailField()


