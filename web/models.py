# coding=utf-8

from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from .validators import validate_file_extension
from pandas import *
import json
import operator


class OfficeFile(models.Model):
    file = models.FileField(validators=[validate_file_extension])
    upload_date = models.DateField(default=timezone.now)
    dict_coor = models.CharField(blank=True, max_length=200)

    def save(__self__):
        super(OfficeFile, __self__).save()
        xls = ExcelFile(__self__.file.path)
        df = xls.parse(xls.sheet_names[0])
        dict_data = df.to_dict('list')

        # вычленяем из словаря список абсцисс
        if 'x' in dict_data:
            listx = dict_data['x']
        else:
            listx = dict_data['x_value']
        # список ординат
        if 'y' in dict_data:
            listy = dict_data['y']
        else:
            listy = dict_data['y_value']

        # превращаем numpyInt to Int
        i = 0
        while i < len(listx):
            listx[i] = int(listx[i])
            i += 1
        i = 0
        while i < len(listy):
            listy[i] = int(listy[i])
            i += 1

        # Int обратно в словарь
        if 'x' in dict_data:
            dict_data['x'] = listx
        else:
            dict_data['x_value'] = listx

        if 'y' in dict_data:
            dict_data['y'] = listy
        else:
            dict_data['y_value'] = listy

        __self__.dict_coor = json.dumps(dict_data)
        super(OfficeFile, __self__).save()
