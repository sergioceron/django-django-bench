from django.test import TestCase
from myapp.models import MyModel
class MyModelTestCase(TestCase):

    def test_pk_cleared_on_delete(self):
        instance = MyModel.objects.create(field1='value1', field2='value2')
        pk_before_delete = instance.pk
        instance.delete()
        self.assertIsNone(instance.pk)

        # Check the instance does not exist in the database
        self.assertFalse(MyModel.objects.filter(pk=pk_before_delete).exists())