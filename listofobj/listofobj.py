#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""List of Object
file: listOfObj.py 
created by: D.Beninato
"""

class Dummy:
    def __init__():
        pass

from collections import UserList
from itertools import compress

class ListOfObj(UserList):
    
    def __add__(self,other):
        return ListOfObj(super().__add__(self,other))
    def __mul__(self,other):
        return ListOfObj(super().__mul__(self,other))
    def __getitem__(self, item):
        if isinstance(item, list): #and len(item) == len(item)
            result = compress(self, item) # Faster
            # ListOfObj([i for (i, v) in zip(self, bool_list) if v])
        elif isinstance(item, slice):
            result = super().__getitem__(item)
        else:
            result = super().__getitem__(item)
            #result = super(ListOfObj, self).__getitem__(item)
        try:
            return ListOfObj(result)
        except TypeError:
            return result

    def __gt__(self,other):
        if type(other) == int or type(other) == float:
            return [x.__gt__(other) for x in self]
        return super().__gt__(other)

    def __ge__(self,other):
        if type(other) == int or type(other) == float:
            return [x.__ge__(other) for x in self]
        return super().__ge__(other)

    def __lt__(self,other):
        if type(other) == int or type(other) == float:
            return [x.__lt__(other) for x in self]
        return super().__lt__(other)

    def __le__(self,other):
        if type(other) == int or type(other) == float:
            return [x.__le__(other) for x in self]
        return super().__le__(other)

    def __eq__(self,other):
        if type(other) == int or type(other) == float:
            return [x.__eq__(other) for x in self]
        return super().__eq__(other)

    def __ne__(self,other):
        if type(other) == int or type(other) == float:
            return [x.__ne__(other) for x in self]
        return super().__ne__(other)


    def filterByBool(self,bool_list):
        ListOfObj(compress(self, bool_list)) # Faster
        # ListOfObj([i for (i, v) in zip(self, bool_list) if v])

    def __getattribute__(self, attr):
        if attr != 'data':
            print('__getattribute__ called for ' + attr)
        return super().__getattribute__(attr)

    def __getattr__(self, attr): # chiamato solo se non trovo __getattribute__
        print('__getattr__ called for ' + attr)
        if attr == 'data':
            return super().__getattr__(attr)
        elif len(self)>0 and hasattr(self[0], attr):
            
            '''
            if not callable(a):
                        A.append(a)
                    else:
                        A.append(a())
            '''
            attr_list = [obj.__getattribute__(attr) for obj in self]
            return ListOfObj(attr_list)
            # return [result() if callable(result) else result for result in attr_list]
        else:
            # Default behaviour
            # raise AttributeError
            return super().__getattr__(attr)

    def __call__(self, *args, **kwargs):
        return [obj.__call__(*args, **kwargs) for obj in self]

    def __setattr__(self, attr, value):
        if attr == 'data':
            super().__setattr__(attr, value)
        elif len(self)>0:# and hasattr(self[0], attr):
            for obj in self:
                obj.__setattr__(attr, value)
                # setattr(obj, attr, value)
        else:
            return super().__setattr__(attr, value)

    def getFields(self):
        return self[0].getFields()

    def __setitem__(self, index, value):
        super(ListOfObj, self).__setitem__(index, value)