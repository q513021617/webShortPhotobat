from xml.etree.ElementTree import Element, SubElement, ElementTree
from xml.dom import minidom
from lxml import etree

pathString = "https://htmlmuban.zhiyigo.cn/?p="
url = ""
root = etree.Element("urlset")
# getindexhtmlPic_1(pathString)
for i in range(1, 1196):
    fileurl = pathString + str(i)
    child1 = etree.SubElement(root, "url")
    child2 = etree.SubElement(child1, "loc")
    child2.text = fileurl
    child3 = etree.SubElement(child1, "lastmod")
    child3.text = "time"
    child4 = etree.SubElement(child1, "changefreq")
    child4.text = "daily"
    child5 = etree.SubElement(child1, "priority")
    child5.text = "0.8"

tree = etree.ElementTree(root)
tree.write('sitemap.xml', pretty_print=True, xml_declaration=True, encoding='utf-8')


