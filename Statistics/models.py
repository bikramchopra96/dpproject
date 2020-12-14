from django.db import models

# Create your models here.
from django.conf import settings
from .available import df_available
import sqlite3

engine = settings.DATABASES['default']['NAME']
 
#Create your models here.
 

class Product(models.Model):
    productdate = models.DateTimeField()
    high = models.DecimalField(decimal_places=5,max_digits=2)
    low = models.DecimalField(decimal_places=5,max_digits=2)
    popen = models.DecimalField(decimal_places=5,max_digits=2)
    pclose = models.DecimalField(decimal_places=5,max_digits=2)
    volume = models.BigIntegerField()
    adjclose = models.DecimalField(decimal_places=5,max_digits=2)
    
cnxn = sqlite3.connect(engine)

#df_final.to_sql('api_stocks', con=cnxn, if_exists='replace', index=False)