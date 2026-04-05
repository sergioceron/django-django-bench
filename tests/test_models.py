from django.test import TestCase
from myapp.models import MyModel
from django.core.exceptions import ObjectDoesNotExist
from django.db import connection
# Existing test case classes

class MyModelDeleteTestCase(TestCase):
    def setUp(self):
        # Create a model instance
        self.instance = MyModel.objects.create()

    def test_pk_is_none_after_delete(self):
        # Ensure the instance has a PK before deletion
        self.assertIsNotNone(self.instance.pk)

        # Delete the instance
        self.instance.delete()

        # Delete and then attempt to access the instance
        pk_before_delete = self.instance.pk
        self.instance.delete()

        # Using .refresh_from_db() to make sure instance is synchronized with DB
        with self.assertRaises(ObjectDoesNotExist):
            MyModel.objects.get(pk=pk_before_delete)

        # Confirm after deletion pk should be None
        self.assertIsNone(self.instance.pk)
