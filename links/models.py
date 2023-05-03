from django.db import models
import os
from django.db.models.signals import post_delete


class MyImage(models.Model):
    app_label = 'links'
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    link = models.CharField(max_length=255)

    def delete(self, *args, **kwargs):
        # Delete the image file from the media folder
        os.remove(self.image.path)
        super(MyImage, self).delete(*args, **kwargs)

def delete_image_file(sender, instance, **kwargs):
        # Delete the image file from the media folder
        instance.image.delete(False)

post_delete.connect(delete_image_file, sender=MyImage)
