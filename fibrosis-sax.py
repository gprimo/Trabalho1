import xml.sax as sax

class EmpresaHandler(sax.ContentHandler) :

  def startElement(self, name, attrs) :
    self.current = name

  def characters(self, content) :
    if self.current == "TITLE":
      self.TITLE = content
 
  def endElement(self, name) :
    if self.current == "TITLE":
      f.write("<TITLE>"+self.TITLE+"</TITLE>\n")
    self.current = ""

f = open("/content/drive/Shareddrives/DataScience/titulos.xml", "w")
handler = EmpresaHandler()
parser = sax.make_parser()
parser.setContentHandler(handler)
parser.parse('/content/drive/Shareddrives/DataScience/cf79.xml')
f.close()