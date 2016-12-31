from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Author(models.Model):
    name = models.CharField(max_length=50)
    dni = models.BigIntegerField(null=True, blank=True)
    email = models.EmailField()
    phone = models.BigIntegerField(null=True, blank=True)

    def __str__(self):
        return "Author: {}, {}".format(self.name, self.dni)


@python_2_unicode_compatible
class Book(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200, null=True, blank=True)
    isbn = models.IntegerField()
    year = models.IntegerField()
    authors = models.ManyToManyField(Author,related_name='books')

    def __str__(self):
        return "Book: {}, {}, {}".format(self.name, self.isbn, self.year)


