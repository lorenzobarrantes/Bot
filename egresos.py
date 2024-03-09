item = ''
conti = False
lista = []


def finalizar(lis):
    global item
    item = ''
    return lis, True


def menu_egr():
    global item
    item = ''
    menu = ("↖️ Egresos\n"
            "\n"
            "Seleccione la consulta\n"
            "\n"
            "A. Orden de Traslado\n"
            "B. Orden de Pickeo\n"
            "C. Orden de Desconsolidado\n"
            ". Orden con distinta cantidad\n"
            ". Procesamiento incorrecto de mercadería\n"
            ". Mercadería en zona de expedición o portones\n"
            "E. \n"
            "\n"
            'Recuerde puede escribir "Finalizar" en cualquier momento de la conversación para terminarla.'
            )
    return menu


def opt_egr(text):
    global item
    global lista
    lista = []
    if "menu principal" in text or 'pdf' in text or 'menu egresos' in text:
        item = ''
        if 'menu principal' in text:
            return 'menu principal', False
        elif 'menu egresos' in text:
            return 'menu egresos', False
        else:
            return 'pdf', False
    elif item == '':
        if text == 'a':
            item = 'ot'
            exp = ''
            lista.append(exp)
            return lista, False
        if text == 'b':
            item = 'op'
            exp = ''
            lista.append(exp)
            return lista, False
        if text == 'c':
            item = 'od'
            exp = ''
            lista.append(exp)
            return lista, False
        else:
            return lista.append('No desarrollado'), True
