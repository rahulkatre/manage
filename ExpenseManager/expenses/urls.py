from django.urls import path
from . import views 


app_name='expenses'
urlpatterns=[
	#path('',views.index,name='index'),
	#path('<int:expense_id>/',views.showexpense,name='details'),
	#path('<int:expense_id>/edit/',views.editexpense,name='edit'),
	
	path('',views.IndexView.as_view(),name='index'),
	path('<int:pk>/',views.DetailView.as_view(),name='details'),
	path('<int:expense_id>/edit/',views.editexpense,name='edit'),

	path('<int:expense_id>/save/',views.savespendingtype,name='save'),
	#path('<int:expense_id>/details/',views.showspendingdetails,name='details'),

]