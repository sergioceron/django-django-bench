def test_delete_model_instance(self):
        instance = MyModel.objects.create(name='Test')
        instance_pk = instance.pk
        instance.delete()
        self.assertFalse(MyModel.objects.filter(pk=instance_pk).exists())
        self.assertIsNone(instance.pk)