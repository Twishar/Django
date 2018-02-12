import csv

from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import  render, redirect
from django.contrib.auth import authenticate, login
from .models import Order
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import OrderSerializer
from django.views.generic import View
from django.urls import reverse_lazy
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser


@csrf_exempt
def Search(request, pk):
    try:
        order = Order.objects.get(pk=pk)
    except Order.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        return render(request, 'orders/details', {'order':order})

@csrf_exempt
def OrderList(request):
    if request.method == 'GET':
        snippets = Order.objects.all()
        serializer = OrderSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = OrderSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def OrderDetail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = Order.objects.get(pk=pk)
    except Order.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = OrderSerializer(snippet)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = OrderSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=204)


class IndexView(generic.ListView):
    template_name = 'orders/index.html'
    #context_object_name = 'all_albums'

    def get_queryset(self):
        return Order.objects.all()

class OrderCreate(CreateView):
    model = Order
    fields = ['internalID', 'orderCreationTime', 'merchantID',
              'status', 'amount', 'currency', 'orderID',
              'orderType', 'orderDescription']

@csrf_exempt
def OrderCreateFromCSV(request):
    if request.method == 'POST':
        with open('media/s.csv', encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                _, created = Order.objects.get_or_create(
                    internalID=row[0],
                    orderCreationTime=row[1],
                    merchantID=row[2],
                    status=row[3],
                    amount=row[4],
                    currency=row[5],
                    orderID=row[6],
                    orderType=row[7],
                    orderDescription=row[8],
                )
    return HttpResponse('orders/index.html')


class DetailView(generic.DetailView):
    model = Order
    template_name = 'orders/detail.html'

class OrderDelete(DeleteView):
    model = Order
    success_url = reverse_lazy('orders:index')