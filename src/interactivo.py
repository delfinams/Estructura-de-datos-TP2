import sys
from motor import *


class Menu(object):
    def __init__(self):
        self.consultas = Consultas()

    def menu_principal(self):
        opciones = '[1] RANKING TITULOS\n' \
                   '[2] RANKING CUERPOS\n' \
                   '[3] CANTIDAD DE NOTICIAS\n' \
                   '[4] BUSQUEDA\n' \
                   '[0] SALIR'

        while True:
            print('MENU PRINCIPAL\n---------------\n' + opciones + '\n')
            opcion = input('Ingrese una opción: ')
            if opcion == '1':
                self._menu_rank_titulos()
            elif opcion == '2':
                self._menu_rank_descripciones()
            elif opcion == '3':
                self._menu_cantidad_palabras()
            elif opcion == '4':
                self._menu_busqueda()
            elif opcion == '0':
                self._menu_salir()
            else:
                print('Opción incorrecta\n')

    def _menu_salir(self):

        valido = {"s": True, "S": True, "si": True, "Si": True, "SI": True,
                  "n": False, "N": False, "no": False, "No": False, "NO": False}

        while True:
            opcion = input('¿Seguro que desea salir[SI/NO]?: ')

            if opcion in valido:
                if valido[opcion]:
                    sys.exit()
                else:
                    self.menu_principal()

    def _menu_rank_titulos(self):
        print('\nRANKING DE TITULOS\n---------------')
        cant = int(input("Ingrese la cantidad de palabras para el ranking: "))
        medio_elegido = int(input("Ingrese el medio elegido \n1) Clarin\n2) La Nacion\n3) Telam\n4) Pagina 12\n5) Todos los medios\n"))
        seccion_elegida = int(input("Ingrese la seccion elegida\n1) Ultimas Noticias\n2) Politica\n3) Espectaculos\n4) Economia\n5) Internacional\n6) Todas las secciones\n"))

        resultado = self.consultas.ranking_global(cant, medio = medio_elegido, seccion = seccion_elegida-1, tit_o_desc = 1)
        print("\n")
        print(resultado)

    def _menu_rank_descripciones(self):
        print('\nRANKING DE DESCRIPCIONES\n---------------')
        cant = int(input("Ingrese la cantidad de palabras para el ranking: "))
        medio_elegido = int(
            input("Ingrese el medio elegido \n1) Clarin\n2) La Nacion\n3) Telam\n4) Pagina 12\n5) Todos los medios\n"))
        seccion_elegida = int(input(
            "Ingrese la seccion elegida\n1) Ultimas Noticias\n2) Politica\n3) Espectaculos\n4) Economia\n5) Internacional\n6) Todas las secciones\n"))

        resultado = self.consultas.ranking_global(cant, medio=medio_elegido, seccion=seccion_elegida - 1, tit_o_desc=2)
        print("\n")
        print(resultado)

    def _menu_cantidad_palabras(self):
        print('\nCANTIDAD DE NOTICIAS\n-----------------')
        fecha_desde = int(input("Ingrese una fecha desde (con el siguiente formato AAMMDD): "))
        fecha_hasta = int(input("Ingrese una fecha hasta (con el siguiente formato AAMMDD): "))
        hora_desde = int(input("Ingrese una hora desde (con el siguiente formato HHMM): "))
        hora_hasta = int(input("Ingrese una hora hasta (con el siguiente formato HHMM): "))
        medios = list(
            input("Ingrese los medios elegidos como una lista \n1) Clarin\n2) La Nacion\n3) Telam\n4) Pagina 12\n5) Todos los medios\n"))
        secciones = list(input(
            "Ingrese las secciones elegidas como una lista \n1) Ultimas Noticias\n2) Politica\n3) Espectaculos\n4) Economia\n5) Internacional\n6) Todas las secciones\n"))

        resultado = self.consultas.cantidad_noticias_fecha(f_desde=fecha_desde, f_hasta=fecha_hasta, h_desde=hora_desde, h_hasta=hora_hasta, medios_elegidos=medios, secciones_elegidas=secciones)
        print("\n")
        print(resultado)


    def _menu_busqueda(self):
        opciones = '[1] COMPARAR trayectos por DISTANCIA\n' \
                   '[2] COMPARAR trayectos por TIEMPO\n'
        print('\nCOMPARAR TRAYECTOS\n---------------\n' + opciones + '\n')

        opcion = ''
        while True:
            opcion = input('Ingrese una opción: ')
            if opcion == '1':
                self._menu_comparar_distancia()
                break
            elif opcion == '2':
                self._menu_comparar_tiempo()
                break
            else:
                print('Opción incorrecta\n')


if __name__ == "__main__":
    menu = Menu()
    menu.menu_principal()