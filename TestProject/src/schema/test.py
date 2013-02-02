#-*- coding:utf-8 -*-
'''
Created on 2011-11-7

@author: GFTOwenWang
'''
import sys
import people_api as api

#def test(names):
#    people = api.peopleType()
#    for count, name in enumerate(names):
#        id = '%d' % (count + 1, )
#        person = api.personType(name=name, id=id)
#        people.add_person(person)
#    people.export(sys.stdout, 0)

def test(names):
    people = api.people()
    for count, name in enumerate(names):
        id = '%d' % (count + 1, )
        person = api.person(name=name, id=id)
        people.add_person(person)
    people.export(sys.stdout, 0)

test(['albert', 'betsy', 'charlie'])