from django.db import models

# Create your models here.
from django.conf import settings
#from .available import df_available
import sqlite3

engine = settings.DATABASES['default']['NAME']
 
#Create your models here.
 
    
cnxn = sqlite3.connect(engine)

#df_final.to_sql('api_stocks', con=cnxn, if_exists='replace', index=False)
