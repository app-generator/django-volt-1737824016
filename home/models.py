# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Property(models.Model):

    #__Property_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    area = models.IntegerField(null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)

    #__Property_FIELDS__END

    class Meta:
        verbose_name        = _("Property")
        verbose_name_plural = _("Property")


class Owner(models.Model):

    #__Owner_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    tin = models.CharField(max_length=255, null=True, blank=True)

    #__Owner_FIELDS__END

    class Meta:
        verbose_name        = _("Owner")
        verbose_name_plural = _("Owner")


class Unit(models.Model):

    #__Unit_FIELDS__
    unitno = models.IntegerField(null=True, blank=True)
    floorno = models.IntegerField(null=True, blank=True)
    property = models.ForeignKey(property, on_delete=models.CASCADE)

    #__Unit_FIELDS__END

    class Meta:
        verbose_name        = _("Unit")
        verbose_name_plural = _("Unit")



#__MODELS__END
