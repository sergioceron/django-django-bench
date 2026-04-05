def test_delete_model_instance(self):
        instance = MyModel.objects.create(name='Test')
        instance.delete()
        self.assertFalse(MyModel.objects.filter(id=instance.pk).exists())
        self.assertIsNone(instance.pk)