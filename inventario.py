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
            "B. Descartar Mercadería\n"
            "C. Bloqueo Ubicación vs Mercadería\n"
            "D. Movimientos Internos\n"
            "E. Dividir Palet\n"
            "F. Menu Principal"
            "\n"
            'Recuerde puede escribir "Finalizar" en cualquier momento de la conversación para terminarla.'
            )
    return menu


def option_inv(text):
    global item
    global lista
    lista = []
    print(item)
    if "menu principal" in text or 'pdf' in text or 'menu inventario' in text:
        item = ''
        if 'menu principal' in text:
            return 'menu principal', False
        elif 'menu inventario' in text:
            return 'menu inventario', False
        else:
            return 'pdf', False
    elif item == '':

        if text == 'a' or "manual" in text:
            item = 'ayb-manual'
            exp = "Para realizar un alta o baja manual de mercadería, por favor diríjase a la pestaña 'Almacén'. " \
                  "Allí, busque la posición exacta de la mercadería y al hacer clic, le aparecerá algo similar a esto: "

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

        elif text == 'b' or 'descartar' in text:
            item = 'descartar'
            exp = "Para realizar un descarte de mercadería, por favor diríjase a la pestaña 'Almacén'. Allí, " \
                  "busque la posición exacta de la mercadería y al hacer clic, le aparecerá algo similar a esto: "
            lista.append(exp)
            img = 'img_0.jpeg'
            lista.append(img)
            exp = 'A partir de ahí, tiene dos opciones:\n' \
                  '1. Descartar\n' \
                  '2. Enviar a cuarentena'
            lista.append(exp)
            exp = '1. Para descartar la mercadería, simplemente click en "Descartar" y elija la zona de scrap ' \
                  'correspondiente, luego podrá elegir la cantidad de piezas deseadas para descartar. '
            lista.append(exp)
            img = 'img_1.png'
            lista.append(img)
            exp = '2. Para enviar a cuarentena la mercadería, simplemente click en "Enviar a Cuarentena" y elija la ' \
                  'zona de scrap correspondiente, luego podrá elegir la cantidad de piezas deseadas para descartar. '
            lista.append(exp)
            img = 'img_2.png'
            lista.append(img)
            return finalizar(lista)

        elif text == 'c' or 'bloqueo' in text:
            item = 'bloqueo'
            exp = "Para realizar un bloqueo de mercadería, por favor diríjase a la pestaña 'Almacén'. Allí, " \
                  "busque la posición exacta de la mercadería y al hacer clic, le aparecerá algo similar a esto: "
            lista.append(exp)
            texto = 'img_0.jpeg'
            lista.append(texto)
            exp = 'A partir de ahí, tiene dos opciones:\n' \
                  '1. Bloquear mercadería\n' \
                  '2. Bloquear ubicación'
            lista.append(exp)
            exp = '1. Si bloquea la mercadería, esta estará imposibilitada de realizar movimientos dentro del ' \
                  'almacén. Sin embargo, la posición estará desbloqueada, lo que permitirá el flujo de mercadería ' \
                  'dentro de ella. '
            lista.append(exp)
            exp = '2. Si *bloquea la ubicación*, esto implicará que dicha ubicación no permitirá el flujo de' \
                  'mercadería (in/out). En consecuencia, la mercadería dentro de esta ubicación también estará ' \
                  'bloqueada. '
            lista.append(exp)
            return finalizar(lista)

        elif text == 'd' or 'movimiento' in text:
            item = 'movimiento'
            exp = "Para realizar un movimiento interno dentro del almacén, por favor diríjase a la pestaña 'Almacén'. " \
                  "Allí, " \
                  "busque la posición exacta de la mercadería y al hacer clic, le aparecerá algo similar a esto: "
            lista.append(exp)
            img = 'img_0.jpeg'
            lista.append(img)
            exp = 'A partir de ahí, haga click en "Mover".'
            lista.append(exp)
            exp = 'Al llegar a esta etapa, verá la siguiente imagen. Deberá seleccionar la nueva ubicación (escríbala ' \
                  'y presione enter para seleccionarla) y luego indicar la cantidad que desea mover. En caso de tener ' \
                  'palets, tiene la opción de dividirlos en esta instancia. Después, haga clic en "Mover" y se ' \
                  'generará una orden de traslado dentro de Inventario > Órdenes de Traslado, donde podrá visualizar ' \
                  'la orden y aceptarla. '
            lista.append(exp)
            img = 'img_3.png'
            lista.append(img)
            return finalizar(lista)

        elif text == 'e' or 'dividir' in text:
            item = 'dividir'
            exp = "Para realizar una división de palet, por favor diríjase a la pestaña 'Almacén'. " \
                  "Allí, " \
                  "busque la posición exacta de la mercadería y al hacer clic, le aparecerá algo similar a esto: "
            lista.append(exp)
            img = 'img_0.jpeg'
            lista.append(img)
            exp = 'A partir de ahí, haga click en "Dividir Palet".'
            lista.append(exp)
            exp = 'Al llegar a esta etapa, verá la siguiente imagen. Esta se utilizará para dividir un pallet en dos ' \
                  'o más pallets. Deberá agregar la cantidad de bultos del primer pallet mientras que el resto ' \
                  'formará el segundo pallet. Esta acción deberá realizarse haciendo clic en la opción "Subdividir", ' \
                  'y debe hacerlo de la misma manera si decide formar más de dos pallets. ' \
                  'Luego haga click en "Aceptar" para finalizar la operación de división.'
            lista.append(exp)
            img = 'img_4.png'
            lista.append(img)
            return finalizar(lista)

        elif text == 'f' or 'atras' in text or 'menu principal' in text or "atrás" in text:
            return 'menu principal', False
        else:
            return 'error', False
