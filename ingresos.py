item = ''
conti = False
lista = []


def finalizar(lis):
    global item
    item = ''
    return lis, True


def menu_ing():
    global item
    item = ''
    menu = ("↘ Ingresos\n"
            "\n"
            "Seleccione la consulta\n"
            "\n"
            "A. Se ingresó mal un remito\n"
            "B. Se concilió mal la mercadería\n"
            "C. Ubicación incorrecta de la mercadería\n"
            "D. Crear Orden de Traslado\n"
            "E. Menu Principal\n"
            "\n"
            'Recuerde puede escribir "Finalizar" en cualquier momento de la conversación para terminarla.'
            )
    return menu


def option_ubicar(text):
    global item

    if item == 'ubicar':
        if text == 'a' or 'completa' in text:
            exp = '‼ Es crucial enfatizar que *NUNCA* debe confirmar una Orden de Traslado sin haberla ejecutado ' \
                  'efectivamente. Esta acción podría provocar problemas operativos graves en su almacén. Recomendamos ' \
                  'encarecidamente que verifique la ejecución de la orden antes de confirmarla. '
            lista.append(exp)
            exp = "Para solucionar esto, debe dirigirse al almacén y generar un movimiento de mercadería interno.\n" \
                  "Para obtener más información al respecto, puede acceder a mi Menú Principal > Guía de Usuario, " \
                  "donde encontrará el paso a paso del proceso que debe seguir."

            lista.append(exp)
            return finalizar(lista)
        elif text == 'b' or 'pendiente' in text:
            exp = 'Para este caso, editar una orden requiere que identifique cuántos palets se van a editar, ' \
                  'ya que existen dos formas de hacerlo:'
            lista.append(exp)
            exp = '1️⃣ Si son pocos palets, diríjase al botón "Ver Orden" 👁️, donde encontrará el listado de palets a ' \
                  'ubicar junto con un ícono de reemplazo 🔁. Al hacer clic en él, podrá seleccionar la nueva ' \
                  'ubicación para el palet. '
            lista.append(exp)
            exp = '2️⃣ Si es una cantidad considerable de palets, le recomiendo dirigirse a "Editar Orden" ✏, donde verá ' \
                  'un listado de la mercadería seleccionada para el traslado. Puede ubicar esa mercadería dentro de ' \
                  '"Resultados de Búsqueda" para mover cierta cantidad de palets y dejar los demás en staging, ' \
                  'o mover todos. Luego, haga clic en "Siguiente" para ir a la pantalla donde seleccionará realmente ' \
                  'dónde ubicar los palets de su Orden de Traslado. '
            lista.append(exp)
            exp = "3️⃣ Como última opción, puedes anular la Orden de Traslado y luego crear una nueva. Selecciona " \
                  "'Nueva' y luego, en la pestaña que se abre, elige 'Orden de Ingreso'. Busca tu ingreso y vuelve a " \
                  "ubicar la mercancía en el almacén. "
            lista.append(exp)
            exp = 'Independientemente de los pasos que haya seguido, una vez aceptado, la orden estará editada y ' \
                  'lista para ser ubicada en el almacén '
            lista.append(exp)
            return finalizar(lista)
        elif text == 'c' or 'no la encuentro' in text:
            exp = 'Por favor, dentro de "Órdenes de Traslado", revise el filtro. Asegúrese de que esté configurado en ' \
                  '"Pendiente". Si la orden no se encuentra allí, cámbielo a "Completa" y verifique nuevamente.'
            lista.append(exp)
            exp = 'Si la Orden se encuentra en estado "Borrador" o "Anulada", puede crear una nueva haciendo clic en ' \
                  'el botón "Nuevo". Luego, puede buscar la mercadería por orden de ingreso. ' \
                  'Puede visualizar el proceso de creación de una Orden de Traslado en la Guía de Usuario ubicada en ' \
                  'mi Menú Principal. '
            lista.append(exp)
            exp = 'Le voy a volver a mandar las opciones en caso de que la haya encontrado a la Orden en Completa. ' \
                  'Recuerde que puede escribir "Finalizar" en cualquier momento para terminar esta conversación. ' \
                  'Muchas gracias. '
            lista.append(exp)
            texto = ('¿En que estado esta la Orden de Traslado?\n'
                     '\n'
                     'A. Completa\n'
                     'B. Pendiente\n'
                     'C. No la encuentro\n'
                     'D. Atrás')
            lista.append(texto)
            return lista, False
        elif text == 'd' or 'atras' in text:
            item = ''
            return 'menu ingresos', False
        else:
            return 'error', False


def option_remito(text):
    global item

    def menu_remito():
        texto = ("En que dato se equivoco usted?\n"
                 "\n"
                 "A. Chofer\n"
                 "B. Vehiculo\n"
                 "C. Numero de Remito\n"
                 "D. Cantidad de mercadería\n"
                 "E. Atrás")
        lista.append(texto)

    if item == 'remito':
        if text == 'a' or 'completa' in text:
            item = 'remito - completa'
            exp = "Cuando se completa el ingreso, es importante tener en cuenta que no se puede realizar ninguna " \
                  "edición posterior, debido a que la orden de traslado esta confirmada. Por lo tanto, es crucial " \
                  "seguir un conjunto específico de pasos para corregir " \
                  "cualquier error. Ahora, por favor seleccione la opción que corresponda al error cometido: "
            lista.append(exp)
            menu_remito()
            return lista, False
        elif text == 'b' or text == 'c' or 'conciliacion' in text:
            item = 'remito - conciliacion'
            exp = 'En este caso, todavía tiene la oportunidad de editar el remito.'
            lista.append(exp)
            exp = 'Para editar: -Numero de Remito y Cantidad de mercadería, ' \
                  'simplemente diríjase ' \
                  'a *Operaciones > Ingresos > Ordenes de ingreso*, identifique la orden ingresada y haga clic en el ' \
                  'ícono de lápiz para editar. Se abrirá una ventana donde verá el/los remitos cargados y tendrá la ' \
                  'posibilidad de editarlos según sea necesario.'
            lista.append(exp)
            exp = 'Para editar: Chofer o Vehiculo,\n' \
                  'Anule la orden de ingreso e ingrese nuevamente el chofer y vehiculo correcto.\n' \
                  'Recuerde anular tambien el ingreso del incorrecto desde *Operaciones > Arribos y partidas > ' \
                  'Dashboard arribos y partidas*, buscar el ingreso incorrecto y anularlo '
            lista.append(exp)
            return finalizar(lista)
        elif text == 'd' or 'menu' in text or "atras" in text:
            item = ''
            return 'menu ingresos', False
        else:
            item = ''
            return 'error', False


    elif item == 'remito - completa':
        # responde a menu_remito()
        if text == 'a' or 'chofer' in text or text == 'b' or 'vehiculo' in text or text == 'c' or 'remito' in text:
            exp = 'Actualmente, no contamos con la capacidad de modificar dicho dato asignado en un remito ya ' \
                  'confirmado. Sin embargo, ' \
                  'le tranquilizará saber que este aspecto solo influye en la trazabilidad y no afecta de manera ' \
                  'alguna a nuestras operaciones. '
            lista.append(exp)
            exp = 'En caso de necesitar algún cambio, podrá acceder a nuestro menú principal y solicitar el ' \
                  'formulario para reportar errores. Este reporte entra en la categoría: *Importante* y sera atendido ' \
                  'cuanto antes. Muchas gracias. '
            lista.append(exp)
            return finalizar(lista)
        elif text == 'd' or 'mercaderia' in text:
            exp = 'Actualmente, no contamos con la capacidad para modificar la cantidad de mercancía cargada en un ' \
                  'remito Confirmado. '
            lista.append(exp)
            exp = 'Sin embargo, si ha cargado *más mercancía de la indicada en el remito*, \n' \
                  'Ubique correctamente y confirme la orden de traslado en el almacén y ' \
                  'le recomiendo que visite el ' \
                  'almacén y realice una baja manual de la cantidad excedente. '
            lista.append(exp)
            exp = 'Para aprender cómo realizar una baja manual, puede dirigirse a mi Menú Principal > Consultas > ' \
                  'Inventario > Alta y Baja manual. '
            lista.append(exp)
            exp = 'Si, por el contrario, ha ingresado menos mercancía de la indicada en el remito, le sugiero que ' \
                  'confirme la orden de traslado al almacén y ' \
                  'realice un ingreso adicional con un número de remito diferenciado agregando "-1". A partir de ahí, ' \
                  'podrá agregar la mercancía faltante. Para luego confirmar la segunda Orden de Traslado y completar ' \
                  'el proceso de ingreso. '
            lista.append(exp)
            return finalizar(lista)
        elif text == 'e' or 'atras' in text:
            item = ''
            return option_ing('a')
        else:
            item = ''
            return 'error', False


def option_ing(text):
    global item
    global lista
    lista = []
    if "menu principal" in text or 'pdf' in text or 'menu ingresos' in text:
        item = ''
        if 'menu principal' in text:
            return 'menu principal', False
        elif 'menu ingresos' in text:
            return 'menu ingresos', False
        else:
            return 'pdf', False
    elif item == '':

        if text == 'a' or "ingrese mal un remito" in text:
            item = 'remito'
            exp = "En caso de ingresar incorrectamente un remito, ya sea la cantidad de mercancía o su número, " \
                  "es importante seguir un procedimiento específico para corregirlo. Primero, diríjase a la sección " \
                  "de *Operaciones > Ingresos > Ordenes de Ingreso* en el sistema. Desde allí, identifique y visualice " \
                  "el estado de la orden de ingreso correspondiente al remito incorrecto. "
            lista.append(exp)
            texto = ('¿En que estado esta la Orden de Ingreso?\n'
                     '\n'
                     'A. Completa\n'
                     'B. En Conciliación\n'
                     'C. Pendiente de conciliación\n'
                     'D. Atrás')
            lista.append(texto)
            return lista, conti

        elif text == 'b' or 'concilie mal la mercaderia' in text:
            item = 'conciliar'
            exp = "Si ha realizado una conciliación incorrecta, puede corregirla siempre y cuando la " \
                  "orden de ingreso aún no haya sido confirmada. Para ello, diríjase a *Operaciones > Ingresos > " \
                  "Ordenes de Ingreso* y localice el botón de conciliación. Desde allí, podrá editar la conciliación " \
                  "según sea necesario."
            lista.append(exp)
            exp = "*Si encuentra discrepancias entre la cantidad de mercancía* registrada en la conciliación y la " \
                  "cantidad en el remito, es posible que haya faltantes o sobrantes. Le recomendamos revisar " \
                  "detenidamente ambos números (remito y conciliación) para asegurarse de que coincidan correctamente. "
            lista.append(exp)
            exp = "*En el caso de que la orden de ingreso este completa.*\n" \
                  "Para corregir la mercadería debera dar de baja manual la mercadería excedente desde el almacén\n" \
                  "Para aprender cómo realizar una baja manual, puede dirigirse a mi Menú Principal > Consultas >" \
                  "Inventario > Alta y Baja manual."
            lista.append(exp)
            exp = 'Si confirmo la orden con mercadería faltante, realice un ingreso adicional con un número de remito ' \
                  'diferenciado agregando "-1". A partir de ahí, podrá agregar la mercancía faltante.'
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

        elif text == 'd' or 'orden traslado' in text:
            item = 'ot'
            exp = "Para crear una Orden de Traslado, la Orden de Ingreso debe estar en estado 'Completa'. Esto " \
                  "significa que la orden ha sido conciliada y su descarga aceptada. En el almacén, la mercancía " \
                  "estaría en la zona de staging, ya verificada (etiquetada y con la planilla de control de ingreso " \
                  "completada) y lista para ser ubicada. \n" \
                  "*Aquí tienes dos formas de asignar la ubicación, ya sea de manera manual o automática.*"
            lista.append(exp)
            exp = "Para realizarlo de forma *automática*, sigue estos pasos: \n" \
                  "1. Desde la sección de 'Órdenes de ingreso', haz clic en la opción 'Ubicar automáticamente " \
                  "mercadería'. \n" \
                  "2. Al hacer clic en esta opción, aparecerá la siguiente ventana, donde seleccionando la Nave y " \
                  "aceptando, la orden sera creada. "
            lista.append(exp)
            img = 'img_0.png'
            lista.append(img)
            exp = "Para realizarlo de manera *manual*, sigue estos pasos:\n" \
                  "1. Ve a la sección de 'Órdenes de traslado' y haz clic en 'Nuevo'. Se abrirá el siguiente menú, " \
                  "donde deberás seleccionar 'Orden de ingreso', como se indica en la figura:\n "
            lista.append(exp)
            img = 'img_1.png'
            lista.append(img)
            exp = "2. Una vez dentro de 'Órdenes de ingreso', haz clic en 'Buscar' y selecciona la orden deseada (" \
                  "busca el número de orden con el que estabas trabajando). Luego, selecciona la orden y haz clic en " \
                  "'Aceptar'.\n" \
                  "Una vez aceptado le aparecerán los resultados de la búsqueda de la siguiente manera:"
            lista.append(exp)
            img = 'img_2.png'
            lista.append(img)
            exp = "3. Selecciona los productos deseados haciendo clic en ellos. Utiliza la flecha simple para enviar " \
                  "productos individuales o la flecha doble para enviar todos los productos desde la sección de " \
                  "'Resultados de Búsqueda' hacia la sección de 'Mercadería Seleccionada' para su traslado.\n" \
                  "4. Después de verificar que la mercancía es correcta, haz clic en 'Siguiente' en la esquina " \
                  "inferior derecha de la pantalla.\n" \
                  "5. Durante esta fase del proceso, se solicitará seleccionar los productos identificados y " \
                  "posteriormente asignarles una ubicación, seleccionándola en el almacén para luego ubicarla " \
                  "cliqueando el botón 'Agregar'. Una vez completada esta tarea, se deberá confirmar la acción " \
                  "haciendo clic en 'Aceptar', ubicado en la esquina inferior derecha de la pantalla."
            lista.append(exp)
            return finalizar(lista)

        elif text == 'e' or 'atras' in text or 'menu principal' in text:
            return 'menu principal', False
        else:
            return 'error', False

    elif item.startswith('remito'):
        return option_remito(text)
    elif item.startswith('ubicar'):
        return option_ubicar(text)
