#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Simple ORM Practice for SQL
'''

__author__ = 'WingC'

import logging_setting;logging_setting.basicConfig(level=logging_setting.INFO)

class Field(object):
    def __init__(self,name,field_type):
        self.name = name
        self.field_type = field_type

    def __str__(self):
        return "<%s>:<%s>" % (self.__class__.__name__,self.name)

class StringField(Field):
    def __init__(self,name):
        super(StringField,self).__init__(name=name,field_type='varchar(200)')

class IntergerField(Field):
    def __init__(self,name):
        super(IntergerField,self).__init__(name=name,field_type='bigint')

class ModelMetaClass(type):
    def __new__(cls, name,bases,attrs):
        if name == 'Model':
            return type.__new__(cls, name,bases,attrs)
        logging_setting.info("Found Model %s" % name)
        mappings = dict()
        for k,v in attrs.items():
            if isinstance(v,Field):
                mappings[k] = v
                logging_setting.info("Found mapping %s <==> %s" % (k, v))
        for k in mappings.keys():
            attrs.pop(k)
        attrs['__mappings__'] = mappings
        attrs['__table__'] = name
        return type.__new__(cls, name,bases,attrs)

class Model(dict,metaclass=ModelMetaClass):
    def __init__(self,**kw):
        super(Model,self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError("Model ha on attribute %s" % key)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))
        sql = "insert into %s (%s) values (%s)" % (self.__table__, ','.join(fields), ','.join(map(str,args)))
        logging_setting.info('SQL:%s' % sql)
        logging_setting.info('ARGS:%s' % args)

class User(Model):
    id = IntergerField('ID')
    name = StringField('name')
    password = StringField('password')

u = User(id=1,name='WingC',password='LND')
u.save()
