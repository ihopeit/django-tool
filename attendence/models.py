#--coding=utf-8--
from django.db import models

class Holiday(models.Model):
    date = models.CharField(max_length=100, verbose_name='日期')
    holiday_type = models.CharField(max_length=100, verbose_name= '假期类型')
    remark = models.CharField(max_length=100, blank=True, null=True, verbose_name= '备注')
    creator = models.CharField(max_length=100, verbose_name= '创建者')
    created_time = models.DateTimeField(verbose_name= '数据录入时间')
    updated_time = models.DateTimeField(verbose_name= '数据更新时间')

    class Meta:
        managed = True
        db_table = 't_holiday'
        app_label = 'attendence'
        verbose_name =  u'假期'
        verbose_name_plural = u'假期'

