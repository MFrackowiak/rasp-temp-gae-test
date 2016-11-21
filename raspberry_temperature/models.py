from django.db import models

# Create your models here.

from google.appengine.ext import ndb


class Temperature(ndb.Model):
    date = ndb.DateProperty()
    time = ndb.TimeProperty()
    temperature = ndb.FloatProperty()
