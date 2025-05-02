from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from .models import *
import json

def loginform(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user=user)
            return redirect('/')
    return render(request, 'main/login.html')

def index(request):
    if not request.user.is_authenticated:
        return loginform(request)
    
    transactions = transaction.objects.all()
    money_types = money_type.objects.all()
    move_types = move_type.objects.all()
    categories = category.objects.all()
    
    transactions_input_form = transaction_form()
     

    return render(request, 'main/index.html', context={'username':request.user.first_name,
                                                        'transactions':transactions,
                                                        "money_types":money_types,
                                                        "move_types":move_types,
                                                        "categories":categories})

def transaction_manage(request):
    if not request.user.is_authenticated:
        response = {"ErrorMessage":"Неавторизованный пользователь!"}
        return JsonResponse(response, safe=False)
    
    if request.method == "POST":
        try:
            data = json.loads(request.body)
        except:
            response = {"ErrorMessage":"Ошибка данных запроса"}
            return JsonResponse(response, safe=False)
        

        data['owner'] = request.user

        form = transaction_form(data)

        if form.is_valid():
        
            form.save()
            return JsonResponse({"answer":"прив"}, safe=False)
        else:
            return JsonResponse(list(form.errors.as_json), safe=False)


    return JsonResponse({"?":"?"}, safe=False)
    


    
