from django.db import models

# Create your models here.

'''class main(models.Model):
    M_NO = models.IntegerField()
    MONTHS = models.CharField(max_length=20)
    SEASON = models.CharField(max_length=20, default="Unknown")'''

class page2(models.Model):
    M_NO = models.IntegerField()
    MONTHS = models.CharField(max_length=20)
    SEASON = models.CharField(max_length=20, default="Unknown")

'''class page3(models.Model):
    M_NO = models.IntegerField()
    MONTHS = models.CharField(max_length=20)
    season = models.CharField(max_length=20)'''
    
class MyModel(models.Model):
    date_field = models.DateField()
    email = models.EmailField(max_length=255)

#linking

class Month(models.Model):
    M_NO = models.IntegerField(primary_key=True)
    MONTHS = models.CharField(max_length=20)
    SEASON = models.CharField(max_length=20, default="Unknown")

    class Meta:
        db_table = 'months'

    def __str__(self):
        return self.MONTHS

class Places(models.Model):
    p_no = models.IntegerField(primary_key=True)
    m_no = models.IntegerField()
    places = models.CharField(max_length=20, default="Unknown")
    description = models.CharField(max_length=15000, default="NULL")
    hotels = models.CharField(max_length=1000, default="NULL")
    class Meta:
        db_table = 'places'

    