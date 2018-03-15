from django.db import models

# Create your models here.
class Expending(models.Model):

	SHOPING='SHP'
	PARTY= 'PRT'
	DINEOUT= 'DNT'

	SPENDING_TYPE_CHOICES=(
		(SHOPING,'Shoping'),
		(PARTY,'Party'),
		(DINEOUT,'Dine-out')
	) 


	spend = models.CharField(max_length=200)
	spend_amt = models.FloatField()
	spend_date= models.DateTimeField(db_index=True)
	spend_type= models.CharField(max_length=3,choices=SPENDING_TYPE_CHOICES)



