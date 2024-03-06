item = ''
conti = False
lista = []


def finalizar(lis):
    global item
    item = ''
    return lis, True


def menu_mob():
    global item
    item = ''
    menu = ("📱 Mobile\n"
            "\n"
            "Seleccione la consulta\n"
            "\n"
            "A. Guia de Usuario\n"
            "B. Órdenes de Trabajo\n"
            "C. KPIs\n"
            "D. Stock\n"
            "E. Configuración\n"
            "F. Menu Principal\n"
            "\n"
            'Recuerde puede escribir "Finalizar" en cualquier momento de la conversación para terminarla.'
            )
    return menu


def option_mob(text):
    global item
    global lista
    lista = []
    if "menu principal" in text:
        item = ''
        return 'menu principal', False
    if item == '':

        if text == 'a' or "guia" in text:
            return 'pdf', False
        if text == 'b' or "ordenes" in text:
            item = 'ot'
            exp = ("Órdenes de Trabajo\n"
                   "\n"
                   "Seleccione la configuración\n"
                   "\n"
                   "A. Manual\n"
                   "B. QR\n"
                   "C. Atrás")
            lista.append(exp)
            return lista, False
        if text == 'c' or "kpi" in text:
            pass
        if text == 'd' or "stock" in text:
            pass
        if text == 'e' or "configuracion" in text:
            pass
    elif item == 'ot':
        if text == 'a' or 'manual' in text:
            pass
        elif text == 'b' or 'qr' in text:
            pass
        else:
            return 'error', False

