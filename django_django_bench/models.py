def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)
        self.id = None