#coding:utf-8

class PropertyDemo(object):
    def __init__(self):
        self._propertyon = 100

    @property
    def propertyon(self):
        return self._propertyon

    @propertyon.setter
    def propertyon(self, new_value):
        self._propertyon = new_value

    @propertyon.deleter
    def propertyon(self):
        del self._propertyon

if __name__ == '__main__':
    p = PropertyDemo()

    print p.propertyon

    #update
    p.propertyon = 200
    print p.propertyon

    #del
    del p.propertyon
    print p.propertyon # no such attribute
