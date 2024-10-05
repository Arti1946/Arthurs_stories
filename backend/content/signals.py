from time import strftime, gmtime

from django.core.files.storage import default_storage
from django.db.models.signals import pre_save, post_delete
from django.dispatch import receiver

from mutagen import File, id3
from content.models import Fairytale, Lullaby, AudioBook, Meditation
from users.models import CustomUser


@receiver(pre_save, sender=Fairytale)
@receiver(pre_save, sender=Lullaby)
@receiver(pre_save, sender=AudioBook)
@receiver(pre_save, sender=Meditation)
def set_file_duration(sender, instance, raw, using, update_fields, **kwargs):
    if not str(instance.file).startswith("audio_files/"):
        audio_info = File(instance.file).info
        audio_length = audio_info.length
        file = id3.ID3(instance.file)
        file['title'] = instance.title
        file.save()
        instance.duration = strftime("%M:%S", gmtime(audio_length))
        if instance.id:
            obj = sender.objects.get(id=instance.id)
            path = obj.file.name
            default_storage.delete(path)


@receiver(post_delete, sender=Fairytale)
@receiver(post_delete, sender=Lullaby)
@receiver(post_delete, sender=AudioBook)
@receiver(post_delete, sender=Meditation)
@receiver(post_delete, sender=CustomUser)
def delete_associated_files(sender, instance, **kwargs):
    """Remove all files of an image after deletion."""
    if sender == CustomUser:
        path = instance.user_pic.name
    else:
        path = instance.file.name
    if path:
        default_storage.delete(path)
