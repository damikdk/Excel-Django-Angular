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
        __self__.dict_coor = json.dumps(dict_data)
        super(OfficeFile, __self__).save()
