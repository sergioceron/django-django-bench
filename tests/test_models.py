from django.test import TestCase
from myapp.models import MyModel
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

        # Refresh instance from the database to clear any stale data
        with self.assertRaises(MyModel.DoesNotExist):
            MyModel.objects.get(pk=self.instance.pk)

        # Confirm the pk is set to None
        self.assertIsNone(self.instance.pk)
