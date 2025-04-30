from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Event

def home(request):
    return redirect('login')

def event_list(request):
    events = Event.objects.all()
    return render(request, 'event/event_list.html', {'events': events})

def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    user_is_participant = False
    
    if request.user.is_authenticated:
        user_is_participant = event.participants.filter(id=request.user.id).exists()
        
        if request.method == 'POST':
            if 'participate' in request.POST:
                event.participants.add(request.user)
                return redirect('event:event_detail', event_id=event.id)
            elif 'cancel' in request.POST:
                event.participants.remove(request.user)
                return redirect('event:event_detail', event_id=event.id)
    
    context = {
        'event': event,
        'user_is_participant': user_is_participant,
        'participants_count': event.participants.count(),
    }
    return render(request, 'event/event_detail.html', context)
