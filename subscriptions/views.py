from django.shortcuts import render,redirect
from django.core.mail import send_mail
from .forms import SubscriberForm, UnsubscribeForm
from .models import Subscriber
from django.contrib import messages

def subscribe(request):
    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            if not Subscriber.objects.filter(email=email).exists():
                form.save()
                send_mail(
                    'Subscription Confirmation',
                    'Thank you for subscribing to our newsletter!',
                    'gumborobert7@gmail.com',
                    [email],
                    fail_silently=False,
                )
                return render(request, 'success.html', {'email': email})
    else:
        form = SubscriberForm()
    return render(request, 'subscribe.html', {'form': form})


def unsubscribe(request):
    if request.method == 'POST':
        form = UnsubscribeForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            try:
                subscriber = Subscriber.objects.get(email=email)
                subscriber.delete()
                messages.success(request, 'You have been unsubscribed from the newsletter.')
            except Subscriber.DoesNotExist:
                messages.error(request, 'This email is not subscribed to the newsletter.')
            return redirect('unsubscribe')
    else:
        form = UnsubscribeForm()
    return render(request, 'unsubscribe.html', {'form': form})
