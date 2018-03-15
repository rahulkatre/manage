import logging
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.urls import reverse
from django.views import generic


from .models import Expending


# Create your views here.
'''
def index(request):
	#qexpenses=Expending.objects.all()
	qexpenses=get_list_or_404(Expending)
	context={'all_expenses':qexpenses}
	return render(request,'expenses/index.html',context)
'''

'''
def showexpense(request,expense_id):
	expense=get_object_or_404(Expending,pk=expense_id)
	return render(request,'expenses/details.html',{'expense':expense})	
'''
logger=logging.getLogger(__name__)

class IndexView(generic.ListView):
	template_name='expenses/index.html'
	context_object_name = 'all_expenses'

	def get_queryset(self):
		return Expending.objects.all()


class DetailView(generic.DetailView):
	model=Expending
	template_name='expenses/details.html'
	context_object_name='expense'


	
def editexpense(request,expense_id):
	logger.error('Something went wrong')
	expense=get_object_or_404(Expending,pk=expense_id)
	return render(request,'expenses/edit_expense.html',{'expense':expense,'Expending':Expending,'error_msg':None})

def savespendingtype(request,expense_id):
	expense=get_object_or_404(Expending,pk=expense_id)
	expense.spend_type=request.POST['type']
	expense.save()
	return HttpResponseRedirect(reverse('expenses:details',args=(expense_id,)))


def  showspendingdetails(request, expense_id):
	return HttpResponse('Spending details %s.' % expense_id)


