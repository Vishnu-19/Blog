from django.shortcuts import render
 
posts=[
 	{
 		'author':'Jane Doe',
 		'title':'Blog post 1',
 		'content':'addsddadddasdad',
 		'date_posted':'Aug 22,2020'
 	},
 	{
 		'author':'Jane Doe',
 		'title':'Blog post 2',
 		'content':'addsddadddasdad',
 		'date_posted':'Aug 22,2020'
 	},
 	{
 		'author':'Jane Doe',
 		'title':'Blog post 3',
 		'content':'addsddadddasdad',
 		'date-posted':'Aug 22,2020'
 	}
 ]

def home(request):
	context ={
	'posts':posts
	}
	return render(request,'blog/home.html',context)

def about(request):
	return render(request,'blog/about.html')

