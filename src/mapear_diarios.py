#!/usr/bin/env python
# -*- coding: utf-8 -*-
# coding=utf-8

from nltk.stem.snowball import SnowballStemmer
import lxml.etree as ET
import re
from dateutil.parser import parse as parsear

#falta mapear para los diarios restantes
def mapear_clarin(archivos):

    for id_seccion in range(len(archivos)):
        xml = open(archivos[id_seccion],'r')
        tree = xml.read().encode('raw_unicode_escape')
        root = ET.fromstring(tree)
        titulo_clarin(root, id_seccion)
        descrip_clarin(root, id_seccion)
       
def titulo_clarin(root, id_seccion):
    salida = open("salida.txt", "a")
    
    for idx in range(7,len(root[0])):
        titulo = root[0][idx][0].text
        
        fecha = root[0][idx][4].text
        fecha = parsear(fecha)
        fecha = fecha.strftime('%y%m%d%H%M')
        
        idDocumento = '1'+str(id_seccion)+str(idx).zfill(3)+'1'+fecha
        
        lista = re.split(r'\W+',titulo)
        lista = lematizar(lista)
        
        for palabra in lista:
            salida.write((palabra+", "+idDocumento+"\n"))
            
    salida.close()
        

def descrip_clarin(root, id_seccion):
    salida = open("salida.txt", "a")
    
    for idx in range(7,len(root[0])):
        descrip = root[0][idx][2].text
        
        fecha = root[0][idx][4].text
        fecha = parsear(fecha)
        fecha = fecha.strftime('%y%m%d%H%M')
        
        idDocumento = '1'+str(id_seccion)+str(idx).zfill(3)+"2"+fecha
        
        lista = re.split(r'\W+',descrip)
        lista = lematizar(lista)
        
        for palabra in lista:
            salida.write((palabra+", "+idDocumento+"\n"))

    salida.close()

def lematizar(lista):
    stemmer = SnowballStemmer("spanish")
    recortada = []
    stopwords = ['él', 'ésta', 'éstas', 'éste', 'éstos', 'última', 'últimas', 'último', 'últimos', 'a', 'añadió', 'aún', 'actualmente', 'adelante', 'además', 'afirmó', 'agregó', 'ahí', 'ahora', 'al', 'algún', 'algo', 'alguna', 'algunas', 'alguno', 'algunos', 'alrededor', 'ambos', 'ante', 'anterior', 'antes', 'apenas', 'aproximadamente', 'aquí', 'así', 'aseguró', 'aunque', 'ayer', 'bajo', 'bien', 'buen', 'buena', 'buenas', 'bueno', 'buenos', 'cómo', 'cada', 'casi', 'cerca', 'cierto', 'cinco', 'comentó', 'como', 'con', 'conocer', 'consideró', 'considera', 'contra', 'cosas', 'creo', 'cual', 'cuales', 'cualquier', 'cuando', 'cuanto', 'cuatro', 'cuenta', 'da', 'dado', 'dan', 'dar', 'de', 'debe', 'deben', 'debido', 'decir', 'dejó', 'del', 'demás', 'dentro', 'desde', 'después', 'dice', 'dicen', 'dicho', 'dieron', 'diferente', 'diferentes', 'dijeron', 'dijo', 'dio', 'donde', 'dos', 'durante', 'e', 'ejemplo', 'el', 'ella', 'ellas', 'ello', 'ellos', 'embargo', 'en', 'encuentra', 'entonces', 'entre', 'era', 'eran', 'es', 'esa', 'esas', 'ese', 'eso', 'esos', 'está', 'están', 'esta', 'estaba', 'estaban', 'estamos', 'estar', 'estará', 'estas', 'este', 'esto', 'estos', 'estoy', 'estuvo', 'ex', 'existe', 'existen', 'explicó', 'expresó', 'fin', 'fue', 'fuera', 'fueron', 'gran', 'grandes', 'ha', 'había', 'habían', 'haber', 'habrá', 'hace', 'hacen', 'hacer', 'hacerlo', 'hacia', 'haciendo', 'han', 'hasta', 'hay', 'haya', 'he', 'hecho', 'hemos', 'hicieron', 'hizo', 'hoy', 'hubo', 'igual', 'incluso', 'indicó', 'informó', 'junto', 'la', 'lado', 'las', 'le', 'les', 'llegó', 'lleva', 'llevar', 'lo', 'los', 'luego', 'lugar', 'más', 'manera', 'manifestó', 'mayor', 'me', 'mediante', 'mejor', 'mencionó', 'menos', 'mi', 'mientras', 'misma', 'mismas', 'mismo', 'mismos', 'momento', 'mucha', 'muchas', 'mucho', 'muchos', 'muy', 'nada', 'nadie', 'ni', 'ningún', 'ninguna', 'ningunas', 'ninguno', 'ningunos', 'no', 'nos', 'nosotras', 'nosotros', 'nuestra', 'nuestras', 'nuestro', 'nuestros', 'nueva', 'nuevas', 'nuevo', 'nuevos', 'nunca', 'o', 'ocho', 'otra', 'otras', 'otro', 'otros', 'para', 'parece', 'parte', 'partir', 'pasada', 'pasado', 'pero', 'pesar', 'poca', 'pocas', 'poco', 'pocos', 'podemos', 'podrá', 'podrán', 'podría', 'podrían', 'poner', 'por', 'porque', 'posible', 'próximo', 'próximos', 'primer', 'primera', 'primero', 'primeros', 'principalmente', 'propia', 'propias', 'propio', 'propios', 'pudo', 'pueda', 'puede', 'pueden', 'pues', 'qué', 'que', 'quedó', 'queremos', 'quién', 'quien', 'quienes', 'quiere', 'realizó', 'realizado', 'realizar', 'respecto', 'sí', 'sólo', 'se', 'señaló', 'sea', 'sean', 'según', 'segunda', 'segundo', 'seis', 'ser', 'será', 'serán', 'sería', 'si', 'sido', 'siempre', 'siendo', 'siete', 'sigue', 'siguiente', 'sin', 'sino', 'sobre', 'sola', 'solamente', 'solas', 'solo', 'solos', 'son', 'su', 'sus', 'tal', 'también', 'tampoco', 'tan', 'tanto', 'tenía', 'tendrá', 'tendrán', 'tenemos', 'tener', 'tenga', 'tengo', 'tenido', 'tercera', 'tiene', 'tienen', 'toda', 'todas', 'todavía', 'todo', 'todos', 'total', 'tras', 'trata', 'través', 'tres', 'tuvo', 'un', 'una', 'unas', 'uno', 'unos', 'usted', 'va', 'vamos', 'van', 'varias', 'varios', 'veces', 'ver', 'vez', 'y', 'ya', 'yo']

    for idx in range(len(lista)):
        lista[idx] = lista[idx].lower()
        
        if len(lista[idx]) >= 4 and lista[idx][0] not in ['1','2','3','4','5','6','7','8','9','0'] and lista[idx] not in stopwords:
            lista[idx] = stemmer.stem(lista[idx])
            lista[idx] = desacentuar(lista[idx])
            recortada.append(lista[idx])
            
    return recortada

def desacentuar(palabra):
    palabra = re.sub(r'á', 'a', palabra)
    palabra = re.sub(r'é', 'e', palabra)
    palabra = re.sub(r'í', 'i', palabra)
    palabra = re.sub(r'ó', 'o', palabra)
    palabra = re.sub(r'ú', 'u', palabra)
    return palabra

mapear_clarin(["Clarin.com - Cine.xml"])
