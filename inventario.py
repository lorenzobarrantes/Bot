item = ''
conti = False
lista = []


def finalizar(lis):
    global item
    item = ''
    return lis, True


def menu_inv():
    global item
    item = ''
    menu = ("📦 Inventario\n"
            "\n"
            "Seleccione la consulta\n"
            "\n"
            "A. Alta y Baja Manual\n"
            "B. \n"
            "C. \n"
            "D. Menu Principal\n"
            "\n"
            'Recuerde puede escribir "Finalizar" en cualquier momento de la conversación para terminarla.'
            )
    return menu


def option_inv(text):
    global item
    global lista
    lista = []
    print(item)
    if "menu principal" in text or 'pdf' in text:
        item = ''
        if 'menu principal' in text:
            return 'menu principal', False
        else:
            return 'pdf', False
    if item == '':

        if text == 'a' or "manual" in text:
            item = 'ayb-manual'
            exp = ""
            lista.append(exp)
            texto = ('¿En que estado esta la Orden de Ingreso?\n'
                     '\n'
                     'A. Completa\n'
                     'B. En Conciliación\n'
                     'C. Pendiente de conciliación\n'
                     'D. Atrás')
            lista.append(texto)
            return lista, conti

        elif text == 'b' or '' in text:
            item = ''
            exp = ""
            lista.append(exp)
            exp = ""
            lista.append(exp)
            return finalizar(lista)

        elif text == 'c' or 'ubique mal la mercaderia' in text:
            item = 'ubicar'
            exp = "Si ha ubicado incorrectamente la mercancía, le recomiendo dirigirse a *Operaciones > Ingreso > " \
                  "Ordenes de Traslado*, y comentarme. "
            lista.append(exp)
            texto = ('¿En que estado esta la Orden de Traslado?\n'
                     '\n'
                     'A. Completa\n'
                     'B. Pendiente\n'
                     'C. No la encuentro\n'
                     'D. Atrás')
            lista.append(texto)
            return lista, conti
        elif text == 'd' or 'atras' in text or 'menu principal' in text or "atrás" in text:
            return 'menu principal', False
        else:
            return 'error', False

    elif item.startswith('remito'):
        return
    elif item.startswith('ubicar'):
        return
