from django.db import models


class TimestampsMixin(models.Model):
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    date_updated = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        abstract = True


# class ObfuscatedUrlMixin(models.Model):
#     def generate_hash(size=8):
#         return size
#
#     def generate_unique_hash(hash_size, unique_on):
#         generate_hash()
#         pass
#
#     hash_size = 8
#     hash = generate_unique_hash()
