import re
import time

class Consultas(object):
    lista = [[(0, 1), ['2001421611031349', '2001421611031349', '2001421611031349', '2001421611031349', '2001421611031349'], 0], [(0, 1), ['1101421611031349', '1101121611031409', '1101421611031349', '1101421611031349', '1001421611031349', '1101421611031349', '1101421611031349', '1001421611031349'], None], [(0, 1), ['1001121611031409'], None], [(1, 1), ['1001221611031400', '1000811611031417', '1001421611031349', '1001421611031349'], None], [(0, 1), ['1001421611031349'], None], [(0, 1), ['1001421611031349'], None], [(1, 0), ['1101511611031347'], None], [(0, 1), ['1001321611031351'], None], [(0, 1), ['1001621611031329'], None], [(0, 1), ['1000821611031417'], None], [(1, 0), ['1000911611031413'], 58], [(1, 0), ['1001311611031351'], None], [(0, 2), ['1000821611031417', '1000921611031413'], None], [(0, 2), ['1101421611031349', '1100821611031417'], None], [(0, 2), ['1000821611031417', '1001121611031409'], None], [(0, 1), ['1001321611031351'], None], [(1, 2), ['1000721611031417', '1000711611031417', '1001521611031347'], None], [(1, 0), ['1000811611031417'], None], [(0, 1), ['1001421611031349'], None], [(0, 1), ['1001121611031409'], None], [(0, 1), ['1001421611031349'], 110], [(0, 1), ['1000821611031417'], None], [(1, 1), ['1001411611031349', '1001421611031349'], None], [(1, 0), ['1001511611031347'], None], [(1, 2), ['1001011611031410', '1001021611031410'], None], [(0, 1), ['1001021611031410'], None], [(0, 1), ['1001421611031349'], None], [(1, 0), ['1001511611031347'], None], [(0, 1), ['1001321611031351'], None], [(1, 0), ['1001511611031347'], None], [(0, 1), ['1001121611031409'], 171], [(0, 1), ['1001021611031410'], None], [(1, 0), ['1001411611031349'], None], [(0, 1), ['1001121611031409'], None], [(0, 1), ['1001421611031349'], None], [(1, 0), ['1001311611031351'], None], [(0, 1), ['1000921611031413'], None], [(0, 1), ['1001321611031351'], None], [(1, 0), ['1000711611031417'], None], [(0, 1), ['1000821611031417'], None], [(1, 0), ['1001111611031409'], 244], [(0, 1), ['1000921611031413'], None], [(0, 1), ['1001021611031410'], None], [(0, 1), ['1000721611031417'], None], [(0, 1), ['1001121611031409'], None], [(0, 1), ['1001421611031349'], None], [(1, 0), ['1001311611031351'], None], [(0, 1), ['1001021611031410'], None], [(0, 1), ['1000821611031417'], None], [(1, 0), ['1000811611031417'], None], [(1, 0), ['1001611611031329'], 303], [(1, 1), ['1001111611031409', '1001121611031409'], None], [(1, 1), ['1001411611031349', '1001521611031347'], None], [(0, 1), ['1001421611031349'], None], [(1, 0), ['1001011611031410'], None], [(0, 2), ['1000721611031417', '1001121611031409'], None], [(0, 2), ['1001021611031410', '1001521611031347'], None], [(1, 0), ['1001211611031400'], None], [(0, 1), ['1001221611031400'], None], [(0, 1), ['1000721611031417'], None], [(1, 0), ['1001211611031400'], 365], [(0, 1), ['1000821611031417'], None], [(1, 0), ['1001511611031347'], None], [(0, 1), ['1001521611031347'], None], [(0, 1), ['1001021611031410'], None], [(0, 1), ['1000721611031417'], None], [(1, 0), ['1001211611031400'], None], [(1, 0), ['1000711611031417'], None], [(1, 0), ['1001411611031349'], None], [(1, 0), ['1001311611031351'], None], [(0, 1), ['1001321611031351'], 423], [(1, 0), ['1001211611031400'], None], [(1, 0), ['1000811611031417'], None], [(0, 1), ['1001321611031351'], None], [(0, 1), ['1000721611031417'], None], [(0, 1), ['1001021611031410'], None], [(0, 1), ['1001021611031410'], None], [(1, 0), ['1001011611031410'], None], [(0, 1), ['1001021611031410'], None], [(0, 1), ['1001321611031351'], None], [(0, 1), ['1001021611031410'], 476], [(1, 0), ['1000911611031413'], None], [(0, 1), ['1000721611031417'], None], [(0, 1), ['1001621611031329'], None], [(1, 0), ['1000711611031417'], None], [(0, 1), ['1000921611031413'], None], [(0, 1), ['1000721611031417'], None], [(1, 0), ['1001211611031400'], None], [(0, 1), ['1001321611031351'], None], [(1, 0), ['1001111611031409'], None], [(0, 1), ['1001321611031351'], 541], [(0, 1), ['1000721611031417'], None], [(0, 1), ['1000921611031413'], None], [(0, 1), ['1001621611031329'], None], [(0, 1), ['1001021611031410'], None], [(0, 1), ['1001221611031400'], None], [(0, 1), ['1001021611031410'], None], [(1, 0), ['1001511611031347'], None], [(1, 0), ['1000911611031413'], None], [(1, 1), ['1000811611031417', '1000821611031417'], None], [(2, 0), ['1000811611031417', '1000711611031417'], 608], [(0, 1), ['1000821611031417'], None], [(1, 0), ['1001011611031410'], None], [(0, 1), ['1001321611031351'], None], [(0, 1), ['1001621611031329'], None], [(0, 1), ['1001021611031410'], None], [(1, 0), ['1001211611031400'], None], [(0, 1), ['1001221611031400'], None], [(1, 0), ['1000711611031417'], None], [(1, 0), ['1001111611031409'], None], [(1, 0), ['1001311611031351'], 679], [(0, 1), ['1000721611031417'], None], [(0, 1), ['1001021611031410'], None], [(1, 0), ['1001511611031347'], None], [(0, 1), ['1001021611031410'], None], [(1, 0), ['1000811611031417'], None], [(0, 1), ['1001521611031347'], None], [(1, 0), ['1001411611031349'], None], [(0, 1), ['1001021611031410'], None], [(0, 1), ['1001021611031410'], None], [(0, 1), ['1001521611031347'], 756], [(0, 1), ['1001221611031400'], None], [(1, 0), ['1001411611031349'], None], [(0, 1), ['1000821611031417'], None], [(0, 1), ['1000721611031417'], None], [(1, 0), ['1001211611031400'], None], [(1, 1), ['1001621611031329', '1001611611031329'], None]]

    largo = "5activ5actor9actuacion4alta4apel5aplic5asalt5atras3baj3bat3bod6bolivi4busc3cam4carg4cart3cas4chin6chofer5colon9comercial6compet7confirm4cont4cort4crec4crim7cuchill3dab3ded9defenestr3dej5delit9depardieu9desarroll7desment6destin6devolv5diseñ4dobl7durisim4elig6empiec6espaci7estrell4fall3fif3fot6galaxy3gam4gent6gerard4golp5gremi4hair9hollywood3hor4huir6imagen7inaugur6ingeni5iphon3jov6ladron4larg4lleg3lob5local5manej7mantien5march5marin3mat4medi5mejor5melen3mes5messy3mir5mostr9movimient3mud6muestr4mund7mundial4novi5numer5orcas7organiz5pacin4pais6palerm10paradisiac8particip3pel7pesquer4plan4plat4play6potent7present6proces8protagon4punt5razon7recient6recurs7registr6revist5roman7sancion9seleccion4semi7serruch4sigu9smartphon8sorprend6taxist8tendenci5tenes6tortur6tripul4uber9ultrarrap5veran4vide3vot"

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




a = consultas()
"""b = a.ranking_global_titulo_2(3, medio = 1, seccion=1, tit_o_desc = 1)
print(b)"""
c = a.cantidad_noticias_fecha(f_desde=161102,medios_elegidos=[2], h_desde=1400)
print(c)




