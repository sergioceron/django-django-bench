from django.test import TestCase
from myapp.models import MyModel
from django.db import models
from django.core.exceptions import ObjectDoesNotExist

import pytest
from django.db import IntegrityError
from myapp.models import MyModel
from django.core.exceptions import ObjectDoesNotExist

class MyModelTestCase(TestCase):

    def test_pk_cleared_on_delete(self):
        instance = MyModel.objects.create(field1='value1', field2='value2')
        pk_before_delete = instance.pk
        instance.delete()
        instance = instance.__class__.objects.get(pk=pk_before_delete)
        instance_pk = instance.pk
        instance.delete()
        self.assertRaises(ObjectDoesNotExist, MyModel.objects.get, pk=instance_pk)
        self.assertIsNone(instance.pk)

        # Check the instance does not exist in the database
        self.assertEqual(MyModel.objects.filter(pk=pk_before_delete).count(), 0)