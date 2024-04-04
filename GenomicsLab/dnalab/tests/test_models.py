from django.test import TestCase
from django.utils import timezone
from ..models import Specimen, Sequence


class SpecimenModelTest(TestCase):
    """Test cases for the Specimen Model."""

    def setUp(self):
        """Create a sample Specimen instance for testing."""

        self.specimen = Specimen.objects.create(
            specimen_identifier="Test animal",
            submission_date=timezone.now(),
            notes="Test animal notes"
        )

    def test_speciment_was_created(self):
        """Tests a specimen was created."""

        created_specimen = Specimen.objects.get(
            specimen_identifier="Test Specimen")

        self.assertEqual(isinstance(created_specimen, Specimen), True)


class SequenceModelTest(TestCase):
    """Test cases for the Sequence Model."""

    def setUp(self):
        """Create a sample Specimen and Sequence instance for testing."""

        test_specimen = Specimen.objects.create(
            specimen_identifier="Test Specimen",
            submission_date=timezone.now(),
            notes="notes about Test Specimen for testing a sequence."
        )
        Sequence.objects.create(
            dna_sequence="GATTACA", specimen=test_specimen
        )

    def test_seqence_was_created(self):
        """Tests a sequence was created."""

        created_sequence = Sequence.objects.get(
            specimen_identifier="Test Specimen")

        self.assertEqual(isinstance(created_sequence, Sequence), True)
