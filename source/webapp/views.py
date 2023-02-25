from django.shortcuts import render, redirect, get_object_or_404
from webapp.models import Guestbook
from webapp.forms import GuestbookForm


def guestbook_view(request):
    guestbook = Guestbook.objects.filter(status='active').order_by('-created_at').exclude(is_deleted=True)
    context = {
        'guestbook': guestbook
    }
    return render(request, 'index.html', context)


def entry_add(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        if not name.isalpha():
            return render(request, 'add_entry.html', {'error': 'Name can only contain letters'})
        email = request.POST.get('email')
        desc = request.POST.get('desc')
        if name and email and desc:
            entry = Guestbook.objects.create(
                name=name,
                email=email,
                desc=desc,
                status='active'
            )
            return redirect('guestbook')
    return render(request, 'add_entry.html')


def entry_edit(request, pk):
    entry = get_object_or_404(Guestbook, pk=pk)
    if request.method == 'POST':
        form = GuestbookForm(request.POST, instance=entry)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            if not name.isalpha():
                form.add_error('name', 'Name can only contain letters')
            else:
                form.save()
                return redirect('guestbook')
    else:
        form = GuestbookForm(instance=entry)
    return render(request, 'edit_entry.html', {'form': form})


def entry_delete(request, pk):
    entry = get_object_or_404(Guestbook, pk=pk)
    return render(request, 'delete_entry.html', context={'entry': entry})


def confirm_delete(request, pk):
    entry = get_object_or_404(Guestbook, pk=pk)
    entry.delete()
    return redirect('guestbook')


