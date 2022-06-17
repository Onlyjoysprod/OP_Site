from django.shortcuts import render


def index(request):
    context = {
        # 'title': 'мой магазин',
        # 'products': products_list,
    }
    return render(request, 'mainapp/index.html', context)
