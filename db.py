#--coding=utf-8--

MODELS = {
    'user': {
        'table_name': 't_user',
        'table_desc': '用户',
        'fields':
        {
             'date' : '日期',
             'holiday_type' : '类型',
             'remark' : '备注',
             'creator' : '创建者',
             'created_time' : '创建时间',
             'updated_time' : '更新时间'
        }
    },
	
    'leave': {
        'table_name':'t_leave',
        'table_desc':'年假记录',
        'fields':
        {
            'date':'日期',
            'holiday_type':'类型',
            'remark':'备注',
            'creator':'创建者',
            'created_time':'创建时间',
            'updated_time':'更新时间'
        }
    }
}

'''
class Holiday(models.Model):
    date = models.DateField(verbose_name='日期')

    updated_time = models.DateTimeField(verbose_name= '数据更新时间')

    class Meta:
        managed = False
        db_table = 't_holiday'
        verbose_name =  u'假期'
        verbose_name_plural = u'假期'
'''


def generate_models():
    for model_name,info in MODELS.iteritems():
        model_str = '''
class %model_name%(models.Model):
    %column_def%

    class Meta:
        managed = False
        db_table = '%table_name%'
        verbose_name =  u'%table_desc%'
        verbose_name_plural = u'%table_desc%'
'''
        table_name = info['table_name']
        table_desc = info['table_desc']
        fields = info['fields']
        model_str = model_str.replace('%model_name%',model_name.title())
        model_str = model_str.replace('%table_name%',table_name)
        model_str = model_str.replace('%table_desc%',table_desc)
        
        column_def = ''
        for field_name,field_desc in fields.iteritems():
            if 'time' in field_name:
                column_def += ("\r\n    %s = models.DateTimeField(verbose_name='%s')" % (field_name,field_desc) ) 
            elif 'date' in field_name:
                column_def += ("\r\n    %s = models.DateTimeField(verbose_name='%s')" % (field_name,field_desc) )
            else:
                column_def += ("\r\n    %s = models.CharField(max_length=100, blank=True, null=True, verbose_name='%s')" % (field_name,field_desc) ) 
        
        print(model_str.replace('%column_def%',column_def))

'''
CREATE TABLE `t_holiday` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL COMMENT '日期',
  `updated_time` date NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
'''
def table_creation_sql():
    for model_name,info in MODELS.iteritems():
        sql_str = '''
CREATE TABLE `%table_name%` (
      `id` int(11) NOT NULL AUTO_INCREMENT,
%field_def%      PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
    '''
        table_name = info['table_name']
        table_desc = info['table_desc']
        fields = info['fields']
        sql_str = sql_str.replace('%table_name%',table_name)
        
        field_def = ''
        for field_name,field_desc in fields.iteritems():
            if 'time' in field_name:
                field_def += ("      `%s` datetime NOT NULL COMMENT '%s',\r\n" % (field_name,field_desc) )
            elif 'date' in field_name:
                field_def += ("      `%s` datetime NOT NULL COMMENT '%s',\r\n" % (field_name,field_desc) ) 
            else:
                field_def += ("      `%s` varchar(100) DEFAULT NULL COMMENT '%s',\r\n" % (field_name,field_desc) ) 
        sql_str = sql_str.replace('%field_def%',field_def)
        print(sql_str)
        

if __name__ == '__main__':
    generate_models()
    table_creation_sql()
