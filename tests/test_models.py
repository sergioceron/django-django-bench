from django.test import TestCase
from myapp.models import MyModel
# Existing test case classes

class MyModelTestCase(TestCase):
    def setUp(self):
        # Create a model instance
        self.instance = MyModel.objects.create()

    def test_pk_cleared_post_deletion(self):
        # Ensure the instance has a PK before deletion
        self.assertTrue(self.instance.pk is not None)

        # Delete the instance
        self.instance.delete()

        # Ensure the PK is None after deletion
        self.assertIsNone(self.instance.pk)
