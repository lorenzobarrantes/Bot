item = ''
conti = False
lista = []


def finalizar(lis):
    global item
    item = ''
    return lis, True


def menu_dat():
    global item
    item = ''
    menu = ("⚙ Maestro de Datos\n"
            "\n"
            "Seleccione la consulta\n"
            "\n"
            "A. Carga de Datos\n"
            "B. \n"
            "C. \n"
            "D. \n"
            "\n"
            'Recuerde puede escribir "Finalizar" en cualquier momento de la conversación para terminarla.'
            )
    return menu


def option_dat(text):
    global item
    global lista
    lista = []
    if "menu principal" in text or 'pdf' in text or 'menu datos' in text:
        item = ''
        if 'menu principal' in text:
            return 'menu principal', False
        elif 'menu datos' in text:
            return 'menu datos', False
        else:
            return 'pdf', False
    elif item == '':

        if text == 'a' or "manual" in text:
            return finalizar(lista)
