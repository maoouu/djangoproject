from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required(login_url="../login")
def dash(response):
    return render(response, "EnvergaDB/dash.html", {})