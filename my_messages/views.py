from django.shortcuts import render, get_object_or_404, redirect
from .models import Message
from .forms import ComposeMessageForm

def compose_message(request):
    if request.method == 'POST':
        form = ComposeMessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.save()
            return redirect('my_messages:inbox')
    else:
        form = ComposeMessageForm()
    return render(request, 'my_messages/compose.html', {'form': form})

def inbox(request):
    messages = Message.objects.filter(receiver=request.user).order_by('-timestamp')
    return render(request, 'my_messages/inbox.html', {'messages': messages})

def view_message(request, message_id):
    message = get_object_or_404(Message, id=message_id, receiver=request.user)
    return render(request, 'my_messages/view.html', {'message': message})