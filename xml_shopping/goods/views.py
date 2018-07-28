import csv
import xml.etree.ElementTree as ET

from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage
from io import TextIOWrapper
from goods.models import Goods


@csrf_exempt
def index_view(request):
    if request.method == 'GET':
        return render(request, 'goods/index.html')


def simple_upload(request):
    if request.method == 'POST':
        myfile1 = request.FILES['file1']
        myfile2 = request.FILES['file2']
        myfile3 = request.FILES['file3']
        g = '{http://base.google.com/ns/1.0}'
        tree = ET.parse(myfile1)
        root = tree.getroot()
        print(root.findall('channel'))

        f = TextIOWrapper(myfile2, encoding=request.encoding)
        f2 = TextIOWrapper(myfile3, encoding=request.encoding)

        data = [row for row in csv.reader(f.read().splitlines())]
        data2 = [row for row in csv.reader(f2.read().splitlines())]

        # Костыль, надо разобраться в XML
        for channel in root.findall('channel'):
            for elem in channel.findall('item'):
                gtin = elem.find('{}gtin'.format(g)).text
                if gtin in [v[0] for v in data]:
                    prod_type = elem.find('{}product_type'.format(g)).text
                    title = elem.find('title').text
                    color = ''
                    for val in data2:
                        if gtin == val[0]:
                            color = val[2]

                    print(gtin, title, prod_type, color)
        print(data)
        print('///////////////')
        print(data2)

        # Save docs
        # fs = FileSystemStorage()
        # fs.save(myfile1.name, myfile1)
        # fs.save(myfile2.name, myfile2)
        # fs.save(myfile3.name, myfile3)
        """
        test_good = Goods()
        test_good.article_number = 1231
        test_good.category = 'test'
        test_good.color = 'red'
        test_good.cost_price = 12
        test_good.date_of_creation = '2011-3-12'
        test_good.retail_price = 11
        test_good.stock = 'dsfsd sdfds'
        test_good.title = 'f dsf s '
        test_good.update_date = '2013-4-23'
        test_good.weight_per_package = 13253
        print('Test')
        test_good.save()
        """
        return render(request, 'goods/simple_upload.html')
    return render(request, 'goods/simple_upload.html')


def test_data(request):
    if request.method == 'GET':
        test_good = Goods()
        test_good.article_number = 1231
        test_good.category = 'test'
        test_good.color = 'red'
        test_good.cost_price = 12
        test_good.date_of_creation = '2011-3-12'
        test_good.retail_price = 11
        test_good.stock = 'dsfsd sdfds'
        test_good.title = 'f dsf s '
        test_good.update_date = '2013-4-23'
        test_good.weight_per_package = 13253
        print('Test')
        test_good.save()

    return render(request, 'goods/simple_upload.html')


def check_data(request):
    if request.method == 'GET':
        test_good = Goods.objects.get(article_number=1231)
        print(test_good.color)

    return render(request, 'goods/simple_upload.html')