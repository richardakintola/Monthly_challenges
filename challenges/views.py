from django.shortcuts import render 
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404
from django.urls import reverse
from django.template.loader import render_to_string
# Create your views here.

monthly_challenges = {
    "january" : "Eat no meat for the entire month",
    "feburary" : "Pray daily",
    "march" : "Learn django atleast 20 minutes daily",
    "april" : "Walk for atleast 20 minutes everyday",
    "may" : "Eat no meat for the entire month",
    "june" : "Make new friends",
    "july" : "6-month achievement recap",
    "august" : "smile",
    "september" : "Learn something new",
    "october" : "read books",
    "november" : None,
    "december" : "1-year achievement recap"
}

"""def january(request):
    return HttpResponse("This works!")
def feburary(request):
    return HttpResponse("this also works!")"""

def challenges(request):
    months = list(monthly_challenges.keys())
    
    return render(request, "challenges/index.html", {
        "months" : months
    })


def monthly_challenge_by_nmuber(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("invalid month")
    forward_text = months[month - 1]
    redirect_path = reverse("month-challenge", args= [forward_text])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "text" : challenge_text,
            "month" : month       
            })
    except:
        raise Http404()