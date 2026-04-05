def test_delete_model_instance(self):
        instance = MyModel.objects.create(name='Test')
        instance.delete()
        self.assertFalse(MyModel.objects.filter(id=instance.id).exists())
        self.assertIsNone(instance.pk)