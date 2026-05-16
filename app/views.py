from django.shortcuts import render
import time
from .tasks import send_emails
# Create your views here.
def home(request):


                                    # send_emails.apply_async(countdown=10,priority=5)
    result =send_emails.apply_async()       # == send_emails.delay()  ==  send_emails.apply_async() powerful and fast

    return  render(request,"index.html",{})



"""
@shared_task
def add(x, y):
    return x + y

result = add.delay(5, 3)

result.id

result.status
            PENDING
            STARTED
            SUCCESS
            FAILURE
            RETRY

result.get() #8

"""
