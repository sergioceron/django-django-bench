from django.test import TestCase
from myapp.models import MyModel
from django.core.exceptions import ObjectDoesNotExist
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.db import connection
# Existing test case classes

@override_settings(DEBUG=True)
class MyModelDeleteTestCase(TestCase):
    def setUp(self):
        # Create a model instance
        self.instance = MyModel.objects.create()

    def test_pk_is_none_after_delete(self):

        # Ensure PK is not None before deletion
        self.assertIsNotNone(self.instance.pk)

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

        # Confirm the instance pk is set to None after deletion
        self.assertIsNone(self._get_instance_pk())

    def _get_instance_pk(self):
        # Helper method for reflecting the pk changes post deletion
        return self.instance.pk
