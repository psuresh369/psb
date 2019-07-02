

from django.shortcuts import render, redirect
from Demo_app.forms import EmployeeForm
from Demo_app.models import Create

# Create your views here.

def create(request):
    create = Create.objects.all()
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return render(request,'viewPage.html',{'create':create})
            except:
                pass
    else:
        form = EmployeeForm()

    return render(request,'viewPage.html',{'form':form,'create':create} )
def edit(request, id):
    create = Create.objects.get(id=id)
    return render(request,'edit.html', {'create':create})

def update(request, id):
    create = Create.objects.get(id=id)
    form = EmployeeForm(request.POST, instance = create)
    if form.is_valid():
        print("hi")
        form.save()
        return redirect("/create")
    print("hi")    
    return render(request, 'edit.html', {'create': create})
