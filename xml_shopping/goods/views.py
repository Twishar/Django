import csv
import xml.etree.ElementTree as ET

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage
from io import TextIOWrapper


@csrf_exempt
def index_view(request):
    if request.method == 'GET':
        return render(request, 'goods/index.html')


def simple_upload(request):
    if request.method == 'POST' and request.FILES['file1'] and request.FILES['file2']:
        myfile1 = request.FILES['file1']
        myfile2 = request.FILES['file2']
        myfile3 = request.FILES['file3']

        tree = ET.parse(myfile1)
        root = tree.getroot()
        for child in root:
            print(child.tag, child.attrib)
        f = TextIOWrapper(myfile2, encoding=request.encoding)
        data = [row for row in csv.reader(f.read().splitlines())]
        for row in data:
            # v is every row
            print(row)

        fs = FileSystemStorage()
        fs.save(myfile1.name, myfile1)
        fs.save(myfile2.name, myfile2)
        fs.save(myfile2.name, myfile3)
        return render(request, 'goods/simple_upload.html')
    return render(request, 'goods/simple_upload.html')
