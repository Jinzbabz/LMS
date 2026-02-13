from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Note

# Create your views here.
@login_required
def upload_notes(request):
    if request.user.profile.role != 'teacher':
        return redirect('core:dashboard')
    
    if request.method == 'POST':
        Note.objects.create(
            title=request.POST['title'],    
            file=request.FILES['file'],
            uploaded_by=request.user
        )
        return redirect('core:dashboard')
    return render(request, 'courses/upload_note.html')

@login_required
def note_list(request):
    notes = Note.objects.all()
    return render(request, 'courses/note_list.html', {'notes': notes})
     