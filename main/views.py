from django.shortcuts import render, redirect
import requests
import random


def index(request):
    stat = requests.get('https://api.mcsrvstat.us/2/play.besimple.fun').json()
    context = {
        'players': stat['players']['online'],
        'ping': random.randint(10, 100)
    }
    return render(request, 'main/index.html', context)


def buy(request, id):
    if request.POST:
        user = request.POST['nik']
        if id == 1:
            i = '684392'
        if id == 2:
            i = '684393'
        if id == 3:
            i = '684394'
        res = requests.get(
            'https://api.trademc.org/Shop.buyitems?shop=165333&items=' + i + '&buyer=' + user + '&v=v3').json()
        return redirect('https://pay.trademc.org/?cart_id=' + str(res['response'][
                                                                      'cart_id']) + '&success_url=https://docs.besimple.fun/&fail_url=https://docs.besimple.fun')
    else:
        if id == 1:
            desk = "Покупка доступа к серверу на 1 месяц"
            price = 50
        if id == 2:
            desk = "Покупка доступа к серверу на 3 месяца"
            price = 100
        if id == 3:
            desk = "Покупка доступа к серверу навсегда"
            price = 250
        context = {
            'desk': desk,
            'price': price,
        }
        return render(request, 'main/buy.html', context)
