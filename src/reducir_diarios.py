import os
import re
import pickle

def reducir(archivo):
    palabras = open(archivo,'r')
    dic = {}
    for linea in palabras:
        palabra = linea.split(',')[0]
        letra = palabra[0]
        if letra not in dic:
            dic[letra] = [palabra]
        else:
            dic[letra].append(palabra)
    palabras.close()
    return dic

def separar(dic):
    for letra in dic:
        script_dir = os.path.dirname(__file__)
        rel_path = 'letras/'+letra+'.txt'
        abs_file_path = os.path.join(script_dir, rel_path)
        temp = open(abs_file_path,'w')
        lista = sorted(list(set(dic[letra])))

        for palabra in lista:
            temp.write(str(len(palabra))+palabra)

def indice_invertido():
    archivos = get_listado_letras()
    palabras = get_string_palabras(archivos)
    largo = open("largo.txt", "w")
    largo.write(palabras)
    largo.close()
    intermedio = '\n'+open('salida.txt','r').read()
    print(palabras)
    lista = re.split(r'\d+', palabras)
    lista = lista[1:]
    estructura = []
    for idx in range(len(lista)):
        palabra = lista[idx]
        freq_t = len(re.findall(r'\n'+palabra+'\, \d{5}1', intermedio))
        freq_d = len(re.findall(r'\n'+palabra+'\, \d{5}2', intermedio))
        docus = list(set(re.findall(r'\n'+palabra+'\, (\d+)', intermedio)))
        
        if idx % 10 == 0:
            estructura.append([(freq_t,freq_d),docus,palabras.index(palabra) - len(str(len(palabra)))])
        else:
            estructura.append([(freq_t,freq_d),docus,None])
    pickle.dump(estructura,open('estructura.p','wb'))
    print(estructura)
    return estructura

def get_listado_letras():
    listado = []
    script_dir = os.path.dirname(__file__)

    abs_file_path = os.path.join(script_dir, 'letras')

    for file in os.listdir(abs_file_path):
        if file.endswith(".txt"):
            listado.append(file)
    return listado

def get_string_palabras(archivos):
    palabras = ''
    filenames = archivos
    script_dir = os.path.dirname(__file__)
    abs_file_path = os.path.join(script_dir, 'letras')

    for fname in filenames:
        directorio = os.path.join(abs_file_path, fname)
        with open(directorio) as infile:
            palabras = palabras + infile.read()

    return palabras



indice_invertido()