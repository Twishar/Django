import csv
import datetime
import xml.etree.ElementTree as ET

from ftplib import FTP
from io import TextIOWrapper
from django.db.models import F, Count

from goods.models import Goods
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
from django.core.files.storage import FileSystemStorage


@csrf_exempt
def index_view(request):
    if request.method == 'GET':
        return render(request, 'goods/index.html')


@csrf_exempt
def simple_upload(request):
    if request.method == 'POST':
        xml_file = request.FILES['file1']
        csv_articles = request.FILES['file2']
        csv_new_info = request.FILES['file3']
        g = '{http://base.google.com/ns/1.0}'
        tree = ET.parse(xml_file)
        root = tree.getroot()
        print(root.findall('channel'))

        f = TextIOWrapper(csv_articles, encoding=request.encoding)
        f2 = TextIOWrapper(csv_new_info, encoding=request.encoding)

        data = [row for row in csv.reader(f.read().splitlines())]
        data2 = [row for row in csv.reader(f2.read().splitlines())]

        # Костыль, надо разобраться в XML
        for channel in root.findall('channel'):
            for elem in channel.findall('item'):
                gtin = elem.find('{}gtin'.format(g)).text
                if gtin in [v[0] for v in data]:
                    prod_type = elem.find('{}product_type'.format(g)).text
                    price = elem.find('{}price'.format(g)).text
                    retail_price = elem.find('{}retail-price'.format(g)).text
                    title = elem.find('title').text

                    try:
                        xml_goods = Goods.objects.get(article_number=gtin)
                        xml_goods.update_date = datetime.datetime.today()
                    except ObjectDoesNotExist:
                        xml_goods = Goods()
                        xml_goods.article_number = gtin
                        xml_goods.date_of_creation = datetime.datetime.today()
                        xml_goods.update_date = datetime.datetime.today()

                    xml_goods.title = title
                    xml_goods.price = price
                    xml_goods.retail_price = retail_price
                    xml_goods.category = prod_type
                    for val in data2:
                        if gtin == val[0]:
                            weight_per_package, color, stock = val[1], val[2], val[3]
                            xml_goods.weight_per_package = weight_per_package
                            xml_goods.stock = stock
                            xml_goods.color = color
                    xml_goods.save()

        # Save docs
        # fs = FileSystemStorage()
        # fs.save(xml_file.name, xml_file)
        # fs.save(csv_articles.name, csv_articles)
        # fs.save(csv_new_info.name, csv_new_info)

    return render(request, 'goods/simple_upload.html')


@csrf_exempt
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


@csrf_exempt
def check_data(request):
    if request.method == 'GET':
        test_good = Goods.objects.get(article_number=9339341002284)
        print(test_good.weight_per_package)

    return render(request, 'goods/index.html')


@csrf_exempt
def reports(request):
    return render(request, 'goods/reports.html')


@csrf_exempt
def report_by_days(request):
    if request.method == 'POST':
        """
        Запросы не рабочие
        
        days = Goods.objects.values_list('date_of_creation').distinct()
        num_goods = Goods.objects.filter(date_of_creation=[day for day in days]).aggregate(item_count=Count('category'))
        
        //////////////////////////////////////////////////////////////////////////////////////////
        test = Goods.objects.raw('SELECT COUNT(*) OVER (PARTITION BY date_of_creation, category'
                                 ' ORDER BY date_of_creation, category) FROM goods')
        
        """
    return redirect('/goods/reports')


@csrf_exempt
def price_difference_report(request):
    if request.method == 'POST':
        test_good = Goods.objects.filter(price__lt=F('retail_price')*1.05)
        root = ET.Element("root")
        doc = ET.SubElement(root, "report")

        for val in test_good:
            ET.SubElement(doc, "item").text = str(val.article_number)
        tree = ET.ElementTree(root)
        tree.write("price_difference_report.xml")

        # Никогда не работал с FTP,  поэтому не уверен, будет ли адекватно работать)
        # ftp = FTP('ftp_host', 'ftp_user', 'ftp_pass')
        # ftp.storbinary('STOR price_difference_report.xml', ET.parse(price_difference_report))

    return redirect('/goods/reports')
