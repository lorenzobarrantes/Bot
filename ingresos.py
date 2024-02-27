item = ''
conti = False


def menu_ing():
    global item
    item = ''
    menu = ("Ingresos\n"
            "Seleccione la consulta que tiene\n"
            "\n"
            "A. Ingrese mal un remito\n"
            "B. Concilie mal la mercaderia\n"
            "C. Ubique mal la mercaderia\n"
            "D. Ideas/Sugerencias\n"
            )
    return menu


def option_ing(text):
    global item

    if item == '':

        if text == 'a' or "ingrese mal un remito" in text:
            item = 'remito'
            texto = ('En que estado esta la orden de ingreso?\n'
                     '\n'
                     'A. Completa\n'
                     'B. En Conciliacion\n'
                     'C. Pendiente de conciliacion\n'
                     'D. Atras')
            return texto, conti

        elif text == 'b' or 'concilie mal la mercaderia' in text:
            pass
        elif text == 'c' or 'ubique mal la mercaderia' in text:
            pass
        elif text == 'd' or 'atras' in text or 'menu principal' in text:
            return 'menu principal', False
    elif item == 'remito':
        if text == 'a':
            return 'texto a desarrollar', True
        if text == 'b':
            return 'texto a desarrollar', True
        if text == 'c':
            return 'texto a desarrollar', True
        if text == 'd' or 'menu ingresos' in text or 'volver al menu' in text:
            item = ''
            return 'menu ingresos', False

    return text
