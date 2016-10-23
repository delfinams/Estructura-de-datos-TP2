#!/usr/bin/python
# -*- coding: utf-8 -*-

#import xml.etree.ElementTree as ET
import urllib.request
import lxml.etree as ET
import copy
import time

class La_Nacion(object):

    def guardar_xml(self, url):
        try:
            req = urllib.request.Request(url, data=None, headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
            })
            with urllib.request.urlopen(req) as rss:
                datos = (rss.read())

                root = ET.fromstring(datos)
                titulo = root[1].text+".xml"

                archivo = open(titulo, 'wb')
                archivo.write(datos)
                archivo.close()
        except:
            return "No se pudo guardar"

    def actualizar_xml(self, url):
    
        req = urllib.request.Request(url, data=None, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
        })
        with urllib.request.urlopen(req) as rss:
            datos = (rss.read())

            nuevo_xml = ET.fromstring(datos)
            titulo = nuevo_xml[1].text+".xml"
            viejo_archivo = ET.parse(titulo)
            viejo_xml = viejo_archivo.getroot()

            id_referencia = viejo_xml[7][0].text

            for i in range(7,len(nuevo_xml)):
                id_actual = nuevo_xml[i][0].text
                indice = len(nuevo_xml) - 1
                if id_actual == id_referencia:
                    indice = i
                    break

            for i in range(indice-1, 6, -1):
                entrada = copy.deepcopy(nuevo_xml[i])
                viejo_xml.insert(7, entrada)
                texto = ET.tostring(viejo_xml, pretty_print=True, encoding ="utf-8", method="xml").decode("utf-8")
                archivo = open(titulo, 'w')
                archivo.write(texto)
                archivo.close()

    
        #return "No se pudo guardar"

    def leer_xml(self,minutos):
        while True:
            self.actualizar_xml('http://contenidos.lanacion.com.ar/herramientas/rss-categoria_id=30')
            self.actualizar_xml('http://contenidos.lanacion.com.ar/herramientas/rss-categoria_id=272')
            self.actualizar_xml('http://contenidos.lanacion.com.ar/herramientas/rss-categoria_id=7773')
            self.actualizar_xml('http://contenidos.lanacion.com.ar/herramientas/rss-categoria_id=7')
            self.actualizar_xml('http://contenidos.lanacion.com.ar/herramientas/rss-origen=2')
            self.actualizar_xml('http://contenidos.lanacion.com.ar/herramientas/rss-categoria_id=120')
            time.sleep(minutos*60)

class Telam(object):


    def guardar_xml(self, url):
        try:
            req = urllib.request.Request(url, data=None, headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
            })
            with urllib.request.urlopen(req) as rss:
                datos = (rss.read())

                root = ET.fromstring(datos)[0]
                titulo = root[0].text + ".xml"

                archivo = open(titulo, 'wb')
                archivo.write(datos)
                archivo.close()

        except:
            return "No se pudo guardar"

    def actualizar_xml(self, url):
        try:
            req = urllib.request.Request(url, data=None, headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
            })
            with urllib.request.urlopen(req) as rss:
                datos = (rss.read())

                nuevo_xml = ET.fromstring(datos)[0]
                titulo = nuevo_xml[0].text+".xml"
                viejo_archivo = ET.parse(titulo)
                viejo_xml = viejo_archivo.getroot()[0]

                id_referencia = viejo_xml[4][1].text

                for i in range(4,len(nuevo_xml)):
                    id_actual = nuevo_xml[i][1].text
                    indice = len(nuevo_xml) - 1
                    if id_actual == id_referencia:
                        indice = i
                        break

                for i in range(indice-1, 3, -1):
                    entrada = copy.deepcopy(nuevo_xml[i])
                    viejo_xml.insert(4, entrada)
                    texto = ET.tostring(viejo_xml, pretty_print=True, encoding ="utf-8", method="xml").decode("utf-8")
                    archivo = open(titulo, 'w')
                    archivo.write(texto)
                    archivo.close()

        except:
            return "No se pudo guardar"


    def leer_xml(self, minutos):
        while True:
            self.actualizar_xml('http://www.telam.com.ar/rss2/economia.xml')
            self.actualizar_xml('http://www.telam.com.ar/rss2/espectaculos.xml')
            self.actualizar_xml('http://www.telam.com.ar/rss2/ultimasnoticias.xml')
            self.actualizar_xml('http://www.telam.com.ar/rss2/politica.xml')
            self.actualizar_xml('http://www.telam.com.ar/rss2/sociedad.xml')
            self.actualizar_xml('http://www.telam.com.ar/rss2/internacional.xml')
            time.sleep(minutos * 60)



class Clarin(object):


    def guardar_xml(self, url):
        try:
            req = urllib.request.Request(url, data=None, headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
            })
            with urllib.request.urlopen(req) as rss:
                datos = (rss.read())

                root = ET.fromstring(datos)[0]
                titulo = root[0].text + ".xml"

                archivo = open(titulo, 'wb')
                archivo.write(datos)
                archivo.close()

        except:
            return "No se pudo guardar"

    def actualizar_xml(self, url):
        try:
            req = urllib.request.Request(url, data=None, headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
            })
            with urllib.request.urlopen(req) as rss:
                datos = (rss.read())

                nuevo_xml = ET.fromstring(datos)[0]
                titulo = nuevo_xml[0].text+".xml"
                viejo_archivo = ET.parse(titulo)
                viejo_xml = viejo_archivo.getroot()[0]

                id_referencia = viejo_xml[7][1].text

                for i in range(7,len(nuevo_xml)):
                    id_actual = nuevo_xml[i][1].text
                    indice = len(nuevo_xml) - 1
                    if id_actual == id_referencia:
                        indice = i
                        break

                for i in range(indice-1, 6, -1):
                    entrada = copy.deepcopy(nuevo_xml[i])
                    viejo_xml.insert(7, entrada)
                    texto = ET.tostring(viejo_xml, pretty_print=True, encoding ="utf-8", method="xml").decode("utf-8")
                    archivo = open(titulo, 'w')
                    archivo.write(texto)
                    archivo.close()

        except:
            return "No se pudo guardar"


    def leer_xml(self, minutos):
        while True:
            self.actualizar_xml('http://www.clarin.com/rss/lo-ultimo/')
            self.actualizar_xml('http://www.clarin.com/rss/politica/')
            self.actualizar_xml('http://www.clarin.com/rss/mundo/')
            self.actualizar_xml('http://www.clarin.com/rss/sociedad/')
            self.actualizar_xml('http://www.clarin.com/rss/extrashow/cine/')
            time.sleep(minutos * 60)


class Pagina_12(object):

    def guardar_xml(self, url):

        req = urllib.request.Request(url, data=None, headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
    })
        with urllib.request.urlopen(req) as rss:
            datos = (rss.read())

            root = ET.fromstring(datos)[0]
            titulo = root[0].text + ".xml"
            titulo = titulo.replace("/"," ")

            archivo = open(titulo, 'wb')
            archivo.write(datos)
            archivo.close()


    def actualizar_xml(self, url):
        try:
            req = urllib.request.Request(url, data=None, headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
            })
            with urllib.request.urlopen(req) as rss:
                datos = (rss.read())

                nuevo_xml = ET.fromstring(datos)[0]
                titulo = nuevo_xml[0].text+".xml"
                titulo = titulo.replace("/", " ")
                viejo_archivo = ET.parse(titulo)
                viejo_xml = viejo_archivo.getroot()[0]

                id_referencia = viejo_xml[13][1].text

                for i in range(12,len(nuevo_xml)):
                    id_actual = nuevo_xml[i][1].text
                    indice = len(nuevo_xml) - 1
                    if id_actual == id_referencia:
                        indice = i
                        break

                for i in range(indice-1, 11, -1):
                    entrada = copy.deepcopy(nuevo_xml[i])
                    viejo_xml.insert(12, entrada)
                    texto = ET.tostring(viejo_xml, pretty_print=True, encoding ="utf-8", method="xml").decode("utf-8")
                    archivo = open(titulo, 'w')
                    archivo.write(texto)
                    archivo.close()

        except:
            return "No se pudo guardar"


    def leer_xml(self, minutos):
        while True:
            self.actualizar_xml('http://www.pagina12.com.ar/diario/rss/ultimas_noticias.xml')
            self.actualizar_xml('http://www.pagina12.com.ar/diario/rss/espectaculos.xml')
            self.actualizar_xml('http://www.pagina12.com.ar/diario/rss/cash.xml')
            self.actualizar_xml('http://www.pagina12.com.ar/diario/rss/radar.xml')
            self.actualizar_xml('http://www.pagina12.com.ar/diario/rss/turismo.xml')
            time.sleep(minutos * 60)



l = La_Nacion()
l.actualizar_xml('http://contenidos.lanacion.com.ar/herramientas/rss-categoria_id=30')
l.actualizar_xml('http://contenidos.lanacion.com.ar/herramientas/rss-categoria_id=272')
l.actualizar_xml('http://contenidos.lanacion.com.ar/herramientas/rss-categoria_id=7773')
l.actualizar_xml('http://contenidos.lanacion.com.ar/herramientas/rss-categoria_id=7')
l.actualizar_xml('http://contenidos.lanacion.com.ar/herramientas/rss-origen=2')
l.actualizar_xml('http://contenidos.lanacion.com.ar/herramientas/rss-categoria_id=120')
'''p = Pagina_12()
p.guardar_xml('http://www.pagina12.com.ar/diario/rss/ultimas_noticias.xml')
p.guardar_xml('http://www.pagina12.com.ar/diario/rss/espectaculos.xml')
p.guardar_xml('http://www.pagina12.com.ar/diario/rss/cash.xml')
p.guardar_xml('http://www.pagina12.com.ar/diario/rss/radar.xml')
p.guardar_xml('http://www.pagina12.com.ar/diario/rss/turismo.xml')
c=Clarin()
c.guardar_xml('http://www.clarin.com/rss/lo-ultimo/')
c.guardar_xml('http://www.clarin.com/rss/politica/')
c.guardar_xml('http://www.clarin.com/rss/sociedad/')
c.guardar_xml('http://www.clarin.com/rss/extrashow/cine/')
t = Telam()
t.guardar_xml('http://www.telam.com.ar/rss2/economia.xml')
t.guardar_xml('http://www.telam.com.ar/rss2/espectaculos.xml')
t.guardar_xml('http://www.telam.com.ar/rss2/ultimasnoticias.xml')
t.guardar_xml('http://www.telam.com.ar/rss2/politica.xml')
t.guardar_xml('http://www.telam.com.ar/rss2/sociedad.xml')
t.guardar_xml('http://www.telam.com.ar/rss2/internacional.xml')'''