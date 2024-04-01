from django.test import TestCase
from django.utils import timezone
from ..models import Specimen, Sequence


class SpecimenModelTest(TestCase):
    """Test cases for the Specimen Model."""

    def setUp(self):
        """Create a sample Specimen instance for testing."""

        self.specimen = Specimen.objects.create(
            specimen_origin="Test animal",
            submission_date=timezone.now(),
            notes="Test animal notes"
        )


class SequenceModelTest(TestCase):
    """Test cases for the Sequence Model."""

    def setUp(self):
        """Create a sample Sequence instance for testing."""

        self.specimen = Sequence.objects.create(
            dna_sequence="GATTACA",
            specimen=
        )
