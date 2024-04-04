from django.test import TestCase
from django.utils import timezone
from ..models import Specimen, Sequence


class SpecimenModelTest(TestCase):
    """Test cases for the Specimen Model."""

    def setUp(self):
        """Create a sample Specimen instance for testing."""

        Specimen.objects.create(
            specimen_id="Test-Specimen-1",
            submission_date=timezone.now(),
            notes="Test-notes"
        )

    def test_specimen_created(self):
        """Tests a specimen was created."""

        created_specimen = Specimen.objects.get(
            specimen_id="Test-Specimen-1")

        self.assertEqual(isinstance(created_specimen, Specimen), True)
        # self.assertEqual(created_specimen["notes"], "Test notes")

class SequenceModelTest(TestCase):
    """Test cases for the Sequence Model."""

    def setUp(self):
        """Create a sample Specimen and Sequence instance for testing."""

        test_specimen = Specimen.objects.create(
            specimen_id="Test-Specimen-2",
            submission_date=timezone.now(),
            notes="notes about Test-Specimen-2 for testing a sequence."
        )
        Sequence.objects.create(
            dna_sequence="GATTACA",
            specimen=test_specimen
        )

    def test_sequence_created(self):
        """Tests a sequence was created."""

        created_sequence = Sequence.objects.get(
            dna_sequence="GATTACA")

        self.assertEqual(isinstance(created_sequence, Sequence), True)
