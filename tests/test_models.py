from django.test import TestCase
from myapp.models import MyModel
class MyModelTestCase(TestCase):

    def test_pk_cleared_on_delete(self):
        instance = MyModel.objects.create(field1='value1', field2='value2')
        pk_before_delete = instance.pk
        instance.delete()
        instance = instance.__class__.objects.get(pk=pk_before_delete)
        instance.delete()
        self.assertIsNone(instance.pk)

        # Check the instance does not exist in the database
        self.assertEqual(MyModel.objects.filter(pk=pk_before_delete).count(), 0)