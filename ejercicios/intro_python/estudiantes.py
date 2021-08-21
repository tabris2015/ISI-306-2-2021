estudiantes = [
    {
        'nombre': 'juan',
        'apellido': 'perez',
        'notas': {
            'MAT': 87,
            'QMC': 76,
            'FIS': 56,
            'LAB': 78
        },
        'extras': [2, 3, 1, 1, 1],
        'asistencia': 90
    },
    {
        'nombre': 'ana',
        'apellido': 'rivera',
        'notas': {
            'MAT': 90,
            'QMC': 56,
            'FIS': 88,
            'LAB': 70
        },
        'extras': [1, 1],
        'asistencia': 100
    }
]


class Evaluador:
    """Esta clase implementa diversas funciones para calcular promedios
    de una lista de estudiantes y obtener otros datos adicionales, ademas,
    tambien implementa una funcion para escribir un reporte de notas"""
    def __init__(self, lista_estudiantes, min_asistencia, max_extras):
        self.lista_estudiantes = lista_estudiantes
        self.min_asistencia = min_asistencia
        self.max_extras = max_extras

    def calcular_promedios(self):
        return [0 for estudiante in self.lista_estudiantes]

    def obtener_mejor_estudiante(self):
        return {'nombre completo': 'juan perez', 'promedio': 90}

    def salvar_datos(self, nombre_archivo):
        print('salvando datos')
        return


if __name__ == '__main__':
    evaluador = Evaluador(lista_estudiantes=estudiantes, min_asistencia=80, max_extras=5)
    notas = evaluador.calcular_promedios()
    print(f'Notas: {notas}')
    mejor = evaluador.obtener_mejor_estudiante()
    print(f'Mejor estudiante: {mejor}')
    evaluador.salvar_datos('ejemplo_notas.csv')
