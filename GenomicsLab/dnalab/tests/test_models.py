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
        self.assertEqual(created_specimen.notes, "Test-notes")

    def test_specimen_submission_date(self):
        """Tests the date/time field."""

        specimen3 = Specimen.objects.create(
            specimen_id="Test-Specimen-3",
            submission_date=timezone.now(),
            notes="Test-notes-3"
        )
        specimen3_from_db = Specimen.objects.get(
            specimen_id= "Test-Specimen-3"
            )

        self.assertEqual(specimen3.submission_date,specimen3_from_db.submission_date)

    def test_str_method(self):
        """Tests the dunder str method of a Specimen."""
        # TODO: Write this test


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

        specimen = Specimen.objects.get(specimen_id="Test-Specimen-2")

        self.assertEqual(isinstance(created_sequence, Sequence), True)
        self.assertEqual(created_sequence.specimen, specimen)

    def test_str_method(self):
        """Tests the dunder str method of a Sequence."""
        # TODO: Write this test

