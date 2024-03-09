import random

import requests

import datos
import egresos
import implementacion
import ingresos
import inventario
import mobile
import sett
import json
import time
from datetime import datetime, timedelta

ultimo_msj = ""
ultimo_tiempo = datetime.now()
time_inactive = {}
est_conv = {}
msj_bot = ""
menuIng = ingresos.menu_ing()
saludos = ['hola', 'buenas', 'hol', 'hoola', 'holaa', 'buen dia', 'buen']
sugerencia = []


def obtain_Msj_whatsapp(message, number):
    if 'type' not in message:
        text = 'mensaje no reconocido'
        return text

    typeMessage = message['type']
    if typeMessage == 'text':
        text = message['text']['body']
    elif typeMessage == 'button':
        text = message['button']['text']
    elif typeMessage == 'interactive' and message['interactive']['type'] == 'list_reply':
        text = message['interactive']['list_reply']['title']
    elif typeMessage == 'interactive' and message['interactive']['type'] == 'button_reply':
        text = message['interactive']['button_reply']['title']
    elif typeMessage == 'image':
        send(number, "Por favor, no envie imagenes.")
        text = ''
    elif typeMessage == 'audio':
        send(number, 'Por favor, no envie audios')
        text = ''
    elif typeMessage == 'sticker':
        text = 'sticker'

    else:
        text = 'mensaje no procesado'

    return text


def send_Msj_whatsapp(data):
    try:
        whatsapp_token = sett.whatsapp_token
        whatsapp_url = sett.whatsapp_url
        headers = {'Content-Type': 'application/json',
                   'Authorization': 'Bearer ' + whatsapp_token}
        print("se envia ", data)
        response = requests.post(whatsapp_url,
                                 headers=headers,
                                 data=data)

        if response.status_code == 200:
            return 'mensaje enviado', 200
        else:
            return 'error al enviar mensaje', response.status_code
    except Exception as e:
        return e, 403


def text_Message(number, text):
    data = json.dumps(
        {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": number,
            "type": "text",
            "text": {
                "body": text
            }
        }
    )
    return data


def buttonReply_Message(number, options, body, footer, seed, messageId):
    buttons = []
    for i, option in enumerate(options):
        buttons.append(
            {
                "type": "reply",
                "reply": {
                    "id": seed + "_btn_" + str(i + 1),
                    "title": option
                }
            }
        )

    data = json.dumps(
        {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": number,
            "type": "interactive",
            "interactive": {
                "type": "button",
                "body": {
                    "text": body
                },
                "footer": {
                    "text": footer
                },
                "action": {
                    "buttons": buttons
                }
            }
        }
    )
    return data


def listReply_Message(number, options, body, footer, seed, messageId):
    rows = []
    for i, option in enumerate(options):
        rows.append(
            {
                "id": seed + "_row_" + str(i + 1),
                "title": option,
                "description": ""
            }
        )

    data = json.dumps(
        {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": number,
            "type": "interactive",
            "interactive": {
                "type": "list",
                "body": {
                    "text": body
                },
                "footer": {
                    "text": footer
                },
                "action": {
                    "button": "Ver Opciones",
                    "sections": [
                        {
                            "title": "Secciones",
                            "rows": rows
                        }
                    ]
                }
            }
        }
    )
    return data


def document_Message(number, url, caption, filename):
    data = json.dumps(
        {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": number,
            "type": "document",
            "document": {
                "link": url,
                "caption": caption,
                "filename": filename
            }
        }
    )
    return data


def image_Message(number, url, caption):
    data = json.dumps(
        {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": number,
            "type": "image",
            "image": {
                "link": url,
                "caption": caption
            }
        }
    )
    return data


def sticker_Message(number, sticker_id):
    data = json.dumps(
        {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": number,
            "type": "sticker",
            "sticker": {
                "link": sticker_id
            }
        }
    )
    return data


def get_media_id(media_name, media_type):
    media_id = ""
    if media_type == "sticker":
        media_id = sett.stickers.get(media_name, None)
    # elif media_type == "image":
    #     media_id = sett.images.get(media_name, None)
    # elif media_type == "video":
    #     media_id = sett.videos.get(media_name, None)
    # elif media_type == "audio":
    #     media_id = sett.audio.get(media_name, None)
    return media_id


def replyReaction_Message(number, messageId, emoji):
    data = json.dumps(
        {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": number,
            "type": "reaction",
            "reaction": {
                "message_id": messageId,
                "emoji": emoji
            }
        }
    )
    return data


def replyText_Message(number, messageId, text):
    data = json.dumps(
        {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": number,
            "context": {"message_id": messageId},
            "type": "text",
            "text": {
                "body": text
            }
        }
    )
    return data


def markRead_Message(messageId):
    global ultimo_tiempo
    data = json.dumps(
        {
            "messaging_product": "whatsapp",
            "status": "read",
            "message_id": messageId
        }
    )

    return data


def registerChat(number, name, text):
    hora_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Crear el mensaje a registrar
    msj_registro = f"{hora_actual} - {name}: {text}\n"

    # Guardar el mensaje en un archivo de texto
    with open(f"chat_{number}.txt", "a", encoding="utf-8") as archivo:
        archivo.write(msj_registro)
    archivo.close()


def sendMenu(number, menu=("🏡 Menu Principal.\n"
                           "\n"
                           "Elija la opción que esta buscando.\n"
                           "\n"
                           "A. Consultas\n"
                           "B. Reporte de Error\n"
                           "C. Guía de Usuario\n"
                           "D. Ideas/Sugerencias\n"
                           "E. Primeros Pasos Implementación\n"
                           "F. Mobile\n"
                           "\n"
                           'Recuerde puede escribir "Finalizar" en cualquier momento de la conversación para '
                           'terminarla.'
                           )):
    text = text_Message(number, menu)
    registerChat(number, 'Botifleet', menu)
    send_Msj_whatsapp(text)


def cont_conv(number, name, messageId):
    time.sleep(3)
    body = f"{name.split()[0]}, podemos ayudarte en algo mas?"
    footer = "Quadrant"
    options = ["✅ Menu Principal", "❌ Finalizar"]

    replyButtonData = buttonReply_Message(number, options, body, footer, "sed1", messageId)
    return replyButtonData


def admin_chatbot(text, number, messageId, name):
    global ultimo_msj
    global ultimo_tiempo
    global est_conv
    global msj_bot
    global menuIng
    global saludos
    global sugerencia

    markRead = markRead_Message(messageId)
    send_Msj_whatsapp(markRead)
    review_time(number)
    text = text.lower()  # mensaje que envio el usuario
    lista = []
    print("mensaje del usuario: ", text)
    time.sleep(0.5)
    # Actualizar el tiempo y el mensaje más reciente
    registerChat(number, name, text)
    ultimo_msj = text
    ultimo_tiempo = datetime.now()
    time_inactive[number] = ultimo_tiempo
    if text == '':
        return

    if 'finalizar' in text and not est_conv[number] == 'sugerencia':
        saludo = "Perfecto! No dudes en contactarnos si tienes más preguntas. ¡Hasta luego!"
        est_conv[number] = 'inicio'
        send(number, saludo)
        return

    if est_conv[number] == 'inicio' or text in saludos:
        replyReaction = replyReaction_Message(number, messageId, "👋")
        send_Msj_whatsapp(replyReaction)
        first_text = text_Message(number,
                                  f"Buenas {name.split()[0]}. Le doy la bienvenida a WMS Logifleet by Quadrant\n"
                                  f"\n"
                                  f"🤖 Mi nombre es Botifleet.\n"
                                  f"\n"
                                  f"¿En que puedo asistirle hoy?")
        send_Msj_whatsapp(first_text)
        time.sleep(1)
        sendMenu(number)
        est_conv[number] = 'en curso'
        return

    if text != 'sticker' and est_conv[number] != 'sugerencia':

        if est_conv[number] == 'en curso' or 'menu principal' in text:

            if "consultas" in text or text == 'a':
                body = "Tenemos varias áreas de consulta para elegir. ¿Cuál de estos servicios le gustaría explorar?"
                footer = "Quadrant"
                options = ["↘️ Ingresos", "↖️ Egresos", "📦 Inventario", "⚙ Maestro de Datos", "⏪ Atras"]

                listReplyData = listReply_Message(number, options, body, footer, "sed2", messageId)
                # sticker = sticker_Message(number, get_media_id("sticker1", "sticker"))
                msj_bot = body
                lista.append(listReplyData)
                est_conv[number] = 'consulta'

            elif (text == 'b') or ("error" in text):
                send(number, ("Gracias por reportar los errores. \n"
                              "En el siguiente documento encontraras una serie de pasos a seguir para el "
                              "reporte de errores, "
                              "dentro de este habra un boton para reportar via email. "
                              "Porfavor, llena los espacios solicitados para hacer un correcto seguimiento "
                              "de la solicitud."))
                document = document_Message(number, sett.error_url, "", "Reporte de errores.pdf")
                send_Msj_whatsapp(document)
                replyButtonData = cont_conv(number, name, messageId)
                msj_bot = 'Reporte errores'
                lista.append(replyButtonData)

            elif "guia" in text or text == 'c':
                send(number, "Perfecto, por favor espera un momento.")
                msj_bot = 'Documento Guia Usuario.pdf'
                document = document_Message(number, sett.document_url, "Listo 👍🏻", "Guía de Usuario LogiFleet.pdf")
                send_Msj_whatsapp(document)
                replyButtonData = cont_conv(number, name, messageId)
                lista.append(replyButtonData)

            elif 'idea' in text or text == 'd' or 'sugerencia' in text:
                mensaje = "¡Hola! Bienvenido a esta sección dedicada a tus ideas y sugerencias para mejorar nuestro WMS o " \
                          "mi funcionamiento. Por favor, comparte tus ideas a continuación para que podamos colaborar en " \
                          "su implementación juntos. \n Cuando hayas terminado, escribe 'Listo' para finalizar tu " \
                          "sugerencia. ¡Gracias por tu contribución! "
                est_conv[number] = 'sugerencia'
                send(number, mensaje)

            elif 'implementacion' in text or text == 'e':
                est_conv[number] = 'implementacion'
                sendMenu(number, implementacion.menu_imp())

            elif 'mobile' in text or text == 'f':
                send(number, "En este momento, no contamos con suficientes datos para procesar consultas relacionadas "
                             "con móviles. Si tiene alguna pregunta, por favor envíela después de este mensaje y "
                             "escribe 'Listo' cuando haya terminado. ¡Gracias por su paciencia y comprensión!")
                est_conv[number] = 'sugerencia'
                return
                # est_conv[number] = 'mobile'
                # sendMenu(number, mobile.menu_mob())

            elif "no, gracias" in text:
                replyButtonData = cont_conv(number, name, messageId)
                msj_bot = 'Continuar Conversacion?'
                lista.append(replyButtonData)

            elif "menu principal" in text or "atras" in text:
                est_conv[number] = 'en curso'
                sendMenu(number)

            else:
                error_general(number, messageId)
        ############################################################################################
        elif est_conv[number] == 'consulta':
            if "ingresos" in text or 'menu ingresos' in text or 'ingreso' in text:
                est_conv[number] = 'consulta - ingreso'
                sendMenu(number, menuIng)

            elif 'egresos' in text:
                est_conv[number] = 'consulta - egreso'
                send(number, egresos.menu_egr())

            elif 'inventario' in text:
                est_conv[number] = 'consulta - inventario'
                sendMenu(number, inventario.menu_inv())

            elif 'datos' in text:
                est_conv[number] = 'consulta - datos'
                sendMenu(number, datos.menu_dat())

            elif 'atras' in text:
                est_conv[number] = 'en curso'
                sendMenu(number)

            else:
                error_general(number, messageId)
        ############################################################################################
        elif est_conv[number] == 'consulta - ingreso':
            resp, continua = ingresos.option_ing(text)
            if resp == 'menu ingresos':
                sendMenu(number, menuIng)
                continua = False
            elif resp == 'menu principal':
                est_conv[number] = 'en curso'
                sendMenu(number)
                continua = False
            elif resp == 'pdf':
                est_conv[number] = 'en curso'
                admin_chatbot('pdf', number, messageId, name)
            elif resp == 'error':
                error_general(number, messageId)
            else:
                send_msj_list(number, resp, "ingresos")
            if continua:
                replyButtonData = continua_conv(number, messageId, "✅ Menu Ingresos")
                lista.append(replyButtonData)
        ############################################################################################

        elif est_conv[number] == 'consulta - egreso':
            resp, continua = egresos.opt_egr(text)
            if resp == 'menu egresos':
                sendMenu(number, egresos.menu_egr())
                continua = False
            elif resp == 'menu principal':
                est_conv[number] = 'en curso'
                sendMenu(number)
                continua = False
            elif resp == 'pdf':
                est_conv[number] = 'en curso'
                admin_chatbot('pdf', number, messageId, name)
            elif resp == 'error':
                error_general(number, messageId)
            else:
                send_msj_list(number, resp, "egresos")
            if continua:
                replyButtonData = continua_conv(number, messageId, "✅ Menu Egresos")
                lista.append(replyButtonData)
        ############################################################################################

        elif est_conv[number] == 'consulta - inventario':
            resp, continua = inventario.option_inv(text)
            if 'menu inventario' in resp:
                send(number, inventario.menu_inv())
            elif resp == 'menu principal':
                est_conv[number] = 'en curso'
                sendMenu(number)
                continua = False
            elif resp == 'pdf':
                est_conv[number] = 'en curso'
                admin_chatbot('pdf', number, messageId, name)
            elif resp == 'error':
                error_general(number, messageId)
            else:
                send_msj_list(number, resp, "inventario")
            if continua:
                replyButtonData = continua_conv(number, messageId, "✅ Menu Inventario")
                lista.append(replyButtonData)
        ############################################################################################
        elif est_conv[number] == 'consulta - datos':
            resp, continua = inventario.option_inv(text)
            if 'menu datos' in resp:
                sendMenu(number, datos.menu_dat())
                continua = False
            elif resp == 'menu principal':
                est_conv[number] = 'en curso'
                sendMenu(number)
                continua = False
            elif resp == 'pdf':
                est_conv[number] = 'en curso'
                admin_chatbot('pdf', number, messageId, name)
            elif resp == 'error':
                error_general(number, messageId)
            else:
                send_msj_list(number, resp, "datos")
            if continua:
                replyButtonData = continua_conv(number, messageId, "✅ Menu Datos")
                lista.append(replyButtonData)
        ############################################################################################

        elif est_conv[number] == 'implementacion':
            pass
        ############################################################################################

        elif est_conv[number] == 'mobile':
            pass
            # resp, continua = mobile.option_mob(text)
            # if resp == 'menu mobile':
            #     sendMenu(number, mobile.menu_mob())
            #     continua = False
            # elif resp == 'menu principal':
            #     est_conv[number] = 'en curso'
            #     sendMenu(number)
            #     continua = False
            # elif resp == 'pdf':
            #     send(number, "Perfecto, por favor espera un momento.")
            #     msj_bot = 'Documento Guia Usuario App.pdf'
            #     document = document_Message(number, sett.mobile_url, "Listo 👍🏻", "Guía de Usuario LogiFleet App.pdf")
            #     send_Msj_whatsapp(document)
            #     replyButtonData = cont_conv(number, name, messageId)
            #     lista.append(replyButtonData)
            # elif resp == 'error':
            #     error_general(number, messageId)
            # else:
            #     for msj in resp:
            #         send(number, msj)
            #
            # if continua:
            #     replyButtonData = continua_conv(number, messageId, "✅ Menu Mobile")
            #     lista.append(replyButtonData)
        ############################################################################################

    if est_conv[number] == 'sugerencia':
        if 'listo' in text or 'terminar' in text or 'finalizar' in text:
            texto_sugerencia = "\n".join(sugerencia)
            send("541136383382", f"Nuevo mensaje de: {name}\n"
                                 f"Numero de telefono: {number}\n"
                                 f"Sugerencia:\n"
                                 f"{texto_sugerencia}")
            send(number, 'Gracias por darnos la sugerencia, la estaremos revisando en cuanto ')
            est_conv[number] = 'en curso'
            replyButtonData = cont_conv(number, name, messageId)
            lista.append(replyButtonData)
            sugerencia = []
        sugerencia.append(text)

    elif text == 'sticker':
        i = random.randint(0, 5)
        sticker = sticker_Message(number, f"https://www.quadrant.com.ar/sticker/sticker_{i}.webp")
        send_Msj_whatsapp(sticker)
        registerChat(number, 'Botifleet', 'sticker')
        return

    if msj_bot != '':
        registerChat(number, 'Botifleet', msj_bot)
        msj_bot = ''
    feedback()

    for item in lista:
        send_Msj_whatsapp(item)


def send_msj_list(number, lista, folder):
    for msj in lista:
        if 'img_' in msj:
            img = image_Message(number, f"https://www.quadrant.com.ar/bot/{folder}/{msj}", '👆')
            send_Msj_whatsapp(img)
            time.sleep(1)
        else:
            send(number, msj)

def continua_conv(number, messageId, option):
    options = [option, "🏡 Menu Principal"]
    body = "Espero que esto haya resuelto su consulta\n" \
           "por favor indique si quiere volver a un menu o escriba 'Finalizar' para terminar esta " \
           "conversación, gracias. "
    footer = "Quadrant"
    registerChat(number, "Botifleet", body)
    return buttonReply_Message(number, options, body, footer, "sed3", messageId)


def error_general(number, messageId):
    global ultimo_tiempo

    options = ["✅ Sí, envía el PDF.", "🏡 Menu Principal"]
    body = "No tenemos contemplada su consulta, le podemos ofrecer la guia de usuario la cual tendrá todo lo " \
           "que necesita para resolverla, o si quiere puede volver al menu principal.\n" \
           "Tiene la opción de volver a intentar seleccionar una opción. " \
           "(Recuerde seleccionarla como A, B, etc.)\n" \
           'Recuerde puede escribir "Finalizar" en cualquier momento de la conversación para terminarla.'
    footer = "Quadrant"
    registerChat(number, 'Botifleet', body)
    replyButtonData = buttonReply_Message(number, options, body, footer, "sed3", messageId)
    send_Msj_whatsapp(replyButtonData)


def send(number, text):
    global ultimo_tiempo
    textMessage = text_Message(number, text)
    registerChat(number, 'Botifleet', text)
    send_Msj_whatsapp(textMessage)
    time.sleep(0.5)


def feedback():
    pass


def review_time(number):
    global ultimo_tiempo
    global est_conv
    global time_inactive

    if number not in est_conv:
        est_conv[number] = 'inicio'
        espaciado(number)
        return

    tiempo_actual = datetime.now()
    inactive_real = tiempo_actual - time_inactive[number]
    # Si el tiempo de inactividad es mayor a 60 minutos, reiniciar la conversación
    if inactive_real > timedelta(minutes=60):
        est_conv[number] = "inicio"
        espaciado(number)
    print(est_conv[number])


def espaciado(number):
    with open(f"chat_{number}.txt", "a", encoding="utf-8") as archivo:
        archivo.write('\n')
    archivo.close()


# este codigo soluciona el agregado del 9 en Argentina
def replace_start(s):
    st = str(s)
    number = st[3:]
    if st.startswith("549"):
        newest = "54" + number
        return newest
    else:
        return st

# admin_chatbot('hola', '541150375327', random.randint(0,1000), 'lorenzo')
# admin_chatbot('a', '541150375327', random.randint(0,1000), 'lorenzo')
# admin_chatbot('inventario', '541150375327', random.randint(0,1000), 'lorenzo')
# admin_chatbot('a', '541150375327', random.randint(0,1000), 'lorenzo')
# admin_chatbot('menu inventario', '541150375327', random.randint(0,1000), 'lorenzo')
