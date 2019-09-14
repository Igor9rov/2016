# coding: utf8
#https://gist.github.com/Artem-Mamchych/1636265

xml = '''<?xml version="1.0" encoding="UTF-8"?>
<soft>
    <os>
        <item name="linux" dist="ubuntu">
            This text about linux
        </item>
        <item name="mac os">
            Apple company
        </item>
        <item name="windows" dist="XP" />
    </os>
</soft>'''

from lxml import etree

tree = etree.XML(xml) # Парсинг строки
#tree = etree.parse('1.xml') # Парсинг файла

nodes = tree.xpath('/soft/os/item') # Открываем раздел
for node in nodes: # Перебираем элементы
    print (node.tag,node.keys(),node.values())
    print ('name =',node.get('name')) # Выводим параметр name
    print ('text =',[node.text]) # Выводим текст элемента

# Доступ к тексту напрямую, с указанием фильтра
print ('text1',tree.xpath('/soft/os/item[@name="linux"]/text()'))
print ('text2',tree.xpath('/soft/os/item[2]/text()'))
# Доступ к параметру напрямую
print ('dist',tree.xpath('/soft/os/item[@name="linux"]')[0].get('dist'))
# Выборка по ключу
print ('dist by key',tree.xpath('//*[@name="windows"]')[0].get('dist'))

print ('iterfind:')
for node in tree.iterfind('.//item'): # поиск элементов
    print (node.get('name'))

# Рекурсивный перебор элементов
print ('recursiely:')
def getn(node):
    print (node.tag,node.keys())
    for n in node:
        getn(n)
getn(tree.getroottree().getroot())