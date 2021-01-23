from django.shortcuts import render
from myApp.forms import SignupForm
# Create your views here.
def view1(request):
	f=SignupForm()
	if request.method=='POST':
		f=SignupForm(request.POST)
		if f.is_valid():
			name=f.cleaned_data['name']
			roll=f.cleaned_data['roll']
			email=f.cleaned_data['email']
			phone=f.cleaned_data['phone']
			comments=f.cleaned_data['comments']
			AreUAnEngineeringStudent=f.cleaned_data['AreUAnEngineeringStudent']
			password=f.cleaned_data['password']
			repassword=f.cleaned_data['repassword']
			d={'name1':name,'roll1':roll,'email1':email,'phone1':phone,'comments1':comments,'AreUAnEngineeringStudent1':AreUAnEngineeringStudent}
			return render(request,'myApp/output.html',d)
	d={'form':f}
	return render(request,'myApp/input.html',d)