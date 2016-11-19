#!/usr/bin/env python
# -*- coding: utf-8 -*-
# coding=utf-8
# coding: utf-8

import pickle
import re
import time
from nltk.stem.snowball import SnowballStemmer

class Consultas(object):
    lista = pickle.load(open('estructura.p','rb'))

    largo = open('largo.txt','r').read()

    fecha_actual = time.strftime("%y%m%d")


    def ranking_global(self, cantidad_palabras, medio = None, seccion = None, tit_o_desc = 1):
        indices_usados = []
        freqs = []

        medios = ['0','1','2','3','4']
        secciones = ['0','1','2','3','4','5']

        if(medio != None):
            medios = [str(medio)]

        if(seccion != None):
            secciones = [str(seccion)]

        medios_rx = "["+''.join(medios)+"]"
        secciones_rx = "["+''.join(secciones)+"]"

        reg_ex = r''+medios_rx+secciones_rx+"\d{3}"+str(tit_o_desc)+"\d{10}"



        while len(indices_usados) < cantidad_palabras:
            freq_max = 0
            idx_max = -1

            for idx in range(len(self.lista)):
                id_docus = ' '.join(self.lista[idx][1])
                freq = len(re.findall(reg_ex, id_docus))

                if (freq_max < freq and idx not in indices_usados):
                    freq_max = freq

                    idx_max = idx
            indices_usados.append(idx_max)
            freqs.append(freq_max)


        ranking = self.get_ranking(indices_usados, freqs)
        if len(freqs) != len(ranking):
            print("No hay suficentes palabras que cumplan con las condiciones\n")
        return ranking

    def cantidad_noticias_fecha(self, f_desde = int(fecha_actual), f_hasta = int(fecha_actual), h_desde = 0000, h_hasta = 2359, medios_elegidos = None, secciones_elegidas = None):
        indices_usados = []
        freqs = []

        medios = ['0','1','2','3','4']
        secciones = ['0','1','2','3','4','5']

        if(medios_elegidos != None):
            medios = [str(medio) for medio in medios_elegidos]

        if(secciones_elegidas != None):
            secciones = [str(seccion) for seccion in secciones_elegidas]

        medios_rx = "["+''.join(medios)+"]"
        secciones_rx = "["+''.join(secciones)+"]"

        reg_ex = r''+medios_rx+secciones_rx+"\d{14}"

        cantidad = 0



        for idx in range(len(self.lista)):
            id_docus = ' '.join(self.lista[idx][1])
            listado = re.findall(reg_ex, id_docus)

            for doc in listado:
                hora_doc = int(doc[-4:])
                fecha_doc = int(doc[-10:-4])

                if(f_desde <= fecha_doc and fecha_doc <= f_hasta) and (h_desde <= hora_doc and hora_doc <= h_hasta):
                    cantidad += 1

        return cantidad

    def get_ranking(self, indices_usados, freqs):
        lista = []
        i = 0
        for idx in indices_usados:
            freq_y_palabra = [0,'']
            freq_y_palabra[0] = freqs[i]
            puntero = self.lista[idx][2]
            indices_corridos = 0
            i += 1

            while(puntero == None):
                puntero = self.lista[idx - indices_corridos - 1][2]
                indices_corridos += 1

            largo_palabra = int((re.match("\d+", self.largo[puntero:])).group())
            digitos = len(str(largo_palabra))
            puntero += digitos
            palabra = self.largo[puntero:puntero+largo_palabra]

            while(indices_corridos > 0):
                puntero += largo_palabra
                largo_palabra = int((re.match("\d+", self.largo[puntero:])).group())
                digitos = len(str(largo_palabra))
                puntero += digitos
                palabra = self.largo[puntero:puntero + largo_palabra]
                indices_corridos -= 1

            freq_y_palabra[1] = palabra

            if freq_y_palabra[0] != 0:
                lista.append(freq_y_palabra)

        return lista


    def buscar_palabra(self, palabra_a_buscar):
        palabra_a_buscar = self.lematizar(palabra_a_buscar)
        first = [0, 0]
        last = [None, None]
        i = len(self.lista)
        while last[0] is None:
            i -= 1
            last[0] = self.lista[i][2]

        last[1] = i

        found = False

        while first[1] <= last[1] and not found:
            mid_index = int(round((first[1] + last[1]) / 2, -1))
            mid = [self.lista[mid_index][2], mid_index]

            first_palabra = self.get_palabra(first[0])
            mid_palabra = self.get_palabra(mid[0])
            last_palabra = self.get_palabra(last[0])

            if mid_palabra == palabra_a_buscar:
                found = True
            elif palabra_a_buscar < mid_palabra:
                last = mid

            else:
                first = mid

            if(first[1] + 10 == last[1]):
                diez_palabras = re.split(r'\d+', self.largo[first[0]:last[0]])

                if palabra_a_buscar not in diez_palabras:
                    return "No se encuentra la palabra: " + palabra_a_buscar

                corrimiento = diez_palabras.index(palabra_a_buscar) - 1
                indice = first[1] + corrimiento

                return self.lista[indice][1]

        return self.lista[mid[1]][1]

    def get_palabra(self, idx):
        largo_palabra = int((re.match("\d+", self.largo[idx:])).group())
        digitos = len(str(largo_palabra))
        idx += digitos
        palabra = self.largo[idx:idx + largo_palabra]
        return palabra

    def desacentuar(self, palabra):
        palabra = re.sub(r'á', 'a', palabra)
        palabra = re.sub(r'é', 'e', palabra)
        palabra = re.sub(r'í', 'i', palabra)
        palabra = re.sub(r'ó', 'o', palabra)
        palabra = re.sub(r'ú', 'u', palabra)
        return palabra

    def lematizar(self, x):
        stemmer = SnowballStemmer("spanish")
        lista = []
        lista.append(x)
        recortada = []
        stopwords = ['él', 'ésta', 'éstas', 'éste', 'éstos', 'última', 'últimas', 'último', 'últimos', 'a', 'añadió', 'aún',
                     'actualmente', 'adelante', 'además', 'afirmó', 'agregó', 'ahí', 'ahora', 'al', 'algún', 'algo',
                     'alguna', 'algunas', 'alguno', 'algunos', 'alrededor', 'ambos', 'ante', 'anterior', 'antes', 'apenas',
                     'aproximadamente', 'aquí', 'así', 'aseguró', 'aunque', 'ayer', 'bajo', 'bien', 'buen', 'buena',
                     'buenas', 'bueno', 'buenos', 'cómo', 'cada', 'casi', 'cerca', 'cierto', 'cinco', 'comentó', 'como',
                     'con', 'conocer', 'consideró', 'considera', 'contra', 'cosas', 'creo', 'cual', 'cuales', 'cualquier',
                     'cuando', 'cuanto', 'cuatro', 'cuenta', 'da', 'dado', 'dan', 'dar', 'de', 'debe', 'deben', 'debido',
                     'decir', 'dejó', 'del', 'demás', 'dentro', 'desde', 'después', 'dice', 'dicen', 'dicho', 'dieron',
                     'diferente', 'diferentes', 'dijeron', 'dijo', 'dio', 'donde', 'dos', 'durante', 'e', 'ejemplo', 'el',
                     'ella', 'ellas', 'ello', 'ellos', 'embargo', 'en', 'encuentra', 'entonces', 'entre', 'era', 'eran',
                     'es', 'esa', 'esas', 'ese', 'eso', 'esos', 'está', 'están', 'esta', 'estaba', 'estaban', 'estamos',
                     'estar', 'estará', 'estas', 'este', 'esto', 'estos', 'estoy', 'estuvo', 'ex', 'existe', 'existen',
                     'explicó', 'expresó', 'fin', 'fue', 'fuera', 'fueron', 'gran', 'grandes', 'ha', 'había', 'habían',
                     'haber', 'habrá', 'hace', 'hacen', 'hacer', 'hacerlo', 'hacia', 'haciendo', 'han', 'hasta', 'hay',
                     'haya', 'he', 'hecho', 'hemos', 'hicieron', 'hizo', 'hoy', 'hubo', 'igual', 'incluso', 'indicó',
                     'informó', 'junto', 'la', 'lado', 'las', 'le', 'les', 'llegó', 'lleva', 'llevar', 'lo', 'los', 'luego',
                     'lugar', 'más', 'manera', 'manifestó', 'mayor', 'me', 'mediante', 'mejor', 'mencionó', 'menos', 'mi',
                     'mientras', 'misma', 'mismas', 'mismo', 'mismos', 'momento', 'mucha', 'muchas', 'mucho', 'muchos',
                     'muy', 'nada', 'nadie', 'ni', 'ningún', 'ninguna', 'ningunas', 'ninguno', 'ningunos', 'no', 'nos',
                     'nosotras', 'nosotros', 'nuestra', 'nuestras', 'nuestro', 'nuestros', 'nueva', 'nuevas', 'nuevo',
                     'nuevos', 'nunca', 'o', 'ocho', 'otra', 'otras', 'otro', 'otros', 'para', 'parece', 'parte', 'partir',
                     'pasada', 'pasado', 'pero', 'pesar', 'poca', 'pocas', 'poco', 'pocos', 'podemos', 'podrá', 'podrán',
                     'podría', 'podrían', 'poner', 'por', 'porque', 'posible', 'próximo', 'próximos', 'primer', 'primera',
                     'primero', 'primeros', 'principalmente', 'propia', 'propias', 'propio', 'propios', 'pudo', 'pueda',
                     'puede', 'pueden', 'pues', 'qué', 'que', 'quedó', 'queremos', 'quién', 'quien', 'quienes', 'quiere',
                     'realizó', 'realizado', 'realizar', 'respecto', 'sí', 'sólo', 'se', 'señaló', 'sea', 'sean', 'según',
                     'segunda', 'segundo', 'seis', 'ser', 'será', 'serán', 'sería', 'si', 'sido', 'siempre', 'siendo',
                     'siete', 'sigue', 'siguiente', 'sin', 'sino', 'sobre', 'sola', 'solamente', 'solas', 'solo', 'solos',
                     'son', 'su', 'sus', 'tal', 'también', 'tampoco', 'tan', 'tanto', 'tenía', 'tendrá', 'tendrán',
                     'tenemos', 'tener', 'tenga', 'tengo', 'tenido', 'tercera', 'tiene', 'tienen', 'toda', 'todas',
                     'todavía', 'todo', 'todos', 'total', 'tras', 'trata', 'través', 'tres', 'tuvo', 'un', 'una', 'unas',
                     'uno', 'unos', 'usted', 'va', 'vamos', 'van', 'varias', 'varios', 'veces', 'ver', 'vez', 'y', 'ya',
                     'yo']

        for idx in range(len(lista)):
            lista[idx] = lista[idx].lower()

            if len(lista[idx]) >= 4 and lista[idx][0] not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'] and lista[
                idx] not in stopwords:
                lista[idx] = stemmer.stem(lista[idx])
                lista[idx] = self.desacentuar(lista[idx])
                recortada.append(lista[idx])

        return recortada[0]


