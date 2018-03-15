from django.test import TestCase
from django.utils import timezone


from .models import Expending
# Create your tests here.


class ExpendingModelTests(TestCase):
	def test_for_timezone(self):
		expense=Expending(spend_amt=998)
		self.assertIs(expense.spend_amt < 1000,True)



