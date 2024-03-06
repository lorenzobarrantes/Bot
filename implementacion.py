item = ''
conti = False
lista = []


def finalizar(lis):
    global item
    item = ''
    return lis, True


def menu_imp():
    global item
    item = ''
    menu = ("🚦 Implementación\n"
            "\n"
            "Seleccione la consulta\n"
            "\n"
            "A. Creación de Centro de Distribución\n"
            "B. Carga de Datos\n"
            "C. Crear Usuarios y Permisos\n"
            "D. Menu Principal\n"
            "\n"
            'Recuerde puede escribir "Finalizar" en cualquier momento de la conversación para terminarla.'
            )
    return menu
