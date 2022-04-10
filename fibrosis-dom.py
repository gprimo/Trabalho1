import xml.dom.minidom as dom

domtree = dom.parse('/content/drive/Shareddrives/DataScience/cf79.xml')
group = domtree.documentElement
records = group.getElementsByTagName('RECORD')
f = open("/content/drive/Shareddrives/DataScience/autores.xml", "w")

for record in records:
  recordnum = record.getElementsByTagName('RECORDNUM')[0].childNodes[0].nodeValue
  authors = record.getElementsByTagName('AUTHORS')
  for author in authors:
      auth = author.getElementsByTagName('AUTHOR')
      for item in auth:
        f.write(item.toxml()+"\n")
f.close()