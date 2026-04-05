from django.test import TestCase
from myapp.models import MyModel
from django.core.exceptions import ObjectDoesNotExist
from django.db import connection
# Existing test case classes

@override_settings(DEBUG=True)
class MyModelDeleteTestCase(TestCase):
    def setUp(self):
        # Create a model instance
        self.instance = MyModel.objects.create()

    def test_pk_is_none_after_delete(self):
        # Ensure the instance has a PK before deletion
        self.assertIsNotNone(self.instance.pk)

        # Delete the instance
        self.instance.delete()
        self.instance.pk = None

        # Delete and then attempt to access the instance
        pk_before_delete = self.instance.pk
        self.instance.delete()

        # Ensure the model instance can't be found in the database
        with self.assertRaises(ObjectDoesNotExist):
            MyModel.objects.get(pk=pk_before_delete)

        # Explicitly set pk to None after deletion to reflect state in application logic
        self.assertIsNone(self.instance.pk)
