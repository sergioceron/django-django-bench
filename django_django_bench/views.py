instance_id = instance.pk
        instance.delete()
        assert instance_id is not None  # Ensure ID was valid
        assert instance.pk is None  # PK should be None after delete
        return redirect('home')