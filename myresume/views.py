from django.shortcuts import render,HttpResponseRedirect
from .forms import NotesForm
from .models import Notes
# Create your views here.


# for adding and showing the notes
def home_page(request):
    if request.method == 'POST':
        fm = NotesForm(request.POST)
        if fm.is_valid():
            fm.save()
            fm = NotesForm()
            allNotes = Notes.objects.all()

    else:
        fm = NotesForm()
        allNotes = Notes.objects.all()
    return render(request, 'myresume/index.html',{'form':fm,'notes':allNotes})

# for deleting the note
def del_data(request , id):
    if request.method == 'POST':
        pi = Notes.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')

# for updating the form
def update_data(request , id):
    if request.method == 'POST':
        user = Notes.objects.get(pk=id)
        fm = NotesForm(request.POST , instance=user)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('/')
    else:
        user = Notes.objects.get(pk=id)
        fm = NotesForm(instance=user)
    return render(request,'myresume/update.html',{'form':fm})
