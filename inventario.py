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
            exp = "Para realizar un alta o baja manual de mercancía, por favor diríjase a la pestaña 'Almacén'. Allí, " \
                  "busque la posición exacta de la mercancía y al hacer clic, le aparecerá algo similar a esto: "
            lista.append(exp)
            texto = 'img_0.jpeg'
            lista.append(texto)
            exp = 'A partir de ahí, si cuenta con los permisos necesarios, podrá realizar una baja o alta manual de ' \
                  'un palet. '
            lista.append(exp)
            exp = 'Para verificar si tienes los permisos necesarios, ve a *Configuración > Permisos* y verifica que ' \
                  'tengas habilitadas las opciones de "Alta Manual de Mercadería" y "Baja Manual de Mercadería".'
            lista.append(exp)
            return finalizar(lista)

        elif text == 'b' or '' in text:
            pass

        elif text == 'c' or 'ubique mal la mercaderia' in text:
            pass
        elif text == 'd' or 'atras' in text or 'menu principal' in text or "atrás" in text:
            return 'menu principal', False
        else:
            return 'error', False
