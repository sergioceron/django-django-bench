from django.test import TestCase
from myapp.models import MyModel
# Existing test case classes

class MyModelPKClearingTestCase(TestCase):
    def setUp(self):
        # Create a model instance
        self.instance = MyModel.objects.create()

    def test_pk_set_to_none_after_deletion(self):
        # Ensure the instance has a PK before deletion
        self.assertIsNotNone(self.instance.pk)

        # Delete the instance
        self.instance.delete()

        # Ensure the PK of the instance is set to None after deletion
        self.assertIsNone(self.instance.pk)
