def delete(self, *args, **kwargs):
        # Invalidate the primary key before deleting
        obj_id = self.pk
        super().delete(*args, **kwargs)
        if not obj_id:
            self.pk = None