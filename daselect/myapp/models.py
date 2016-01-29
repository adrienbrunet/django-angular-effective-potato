from django.db import models


class Parent(models.Model):
    name = models.TextField(max_length=30, default='', blank=True)

    def __str__(self):
        return self.name


class Child(models.Model):
    parent = models.ForeignKey('Parent', blank=True, null=True)
