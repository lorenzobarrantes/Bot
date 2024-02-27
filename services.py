import requests

import ingresos
import sett
import json
import time
from datetime import datetime, timedelta

ultimo_msj = ""
ultimo_tiempo = datetime.now()
time_inactive = {}
est_conv = {}
msj_bot = ""
menuIng = ("Ingresos\n"
           "Seleccione la consulta que tiene\n"
           "\n"
           "A. Ingrese mal un remito\n"
           "B. Concilie mal la mercaderia\n"
           "C. Ubique mal la mercaderia\n"
           "D. Menu Principal\n"
           )


def obtain_Msj_whatsapp(message):
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


def sticker_Message(number, sticker_id):
    data = json.dumps(
        {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": number,
            "type": "sticker",
            "sticker": {
                "id": sticker_id
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
                           "Escribe la opción que estas buscando.\n"
                           "\n"
                           "A. Consultas\n"
                           "B. Reporte de Error\n"
                           "C. Guía de Usuario\n"
                           "D. Ideas/Sugerencias\n"
    # "E. \n"
    # "F. \n"
    # "G. \n"
    # "H. \n"
    # "I. \n"
    # "J. \n"
                           )):
    text = text_Message(number, menu)
    registerChat(number, 'Botifleet', menu)
    send_Msj_whatsapp(text)


def cont_conv(number, name, messageId):
    time.sleep(5)
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

    registerChat(number, name, text)

    text = text.lower()  # mensaje que envio el usuario
    lista = []
    print("mensaje del usuario: ", text)

    markRead = markRead_Message(messageId)
    lista.append(markRead)
    time.sleep(2)

    # Actualizar el tiempo y el mensaje más reciente
    ultimo_msj = text

    review_time(number)

    if est_conv[number] == 'inicio':
        with open(f"chat_{number}.txt", "a", encoding="utf-8") as archivo:
            archivo.write('\n')
        archivo.close()
        first_text = text_Message(number, f"¡Hola, {name.split()[0]}! 👋 Bienvenido a WMS Logifleet by Quadrant")
        send_Msj_whatsapp(first_text)
        time.sleep(2)

        sendMenu(number)

        # body = f"¡Hola, {name.split()[0]}! 👋 Bienvenido a WMS Logifleet. ¿Cómo podemos ayudarle hoy?"
        # footer = "Quadrant"
        #
        # options = ["✅ Consultas", "🔍 Menu Principal"]
        # msj_bot = body
        #
        # replyButtonData = buttonReply_Message(number, options, body, footer, "sed1", messageId)
        # # replyReaction = replyReaction_Message(number, messageId, "🫡")
        # # list.append(replyReaction)
        # lista.append(replyButtonData)
        est_conv[number] = 'en curso'

    elif est_conv[number] == 'en curso':
        if "consultas" in text or text == 'a':
            body = "Tenemos varias áreas de consulta para elegir. ¿Cuál de estos servicios le gustaría explorar?"
            footer = "Quadrant"
            options = ["Ingresos", "Egresos", "Inventario", "Maestro de Datos", "Atras"]

            listReplyData = listReply_Message(number, options, body, footer, "sed2", messageId)
            # sticker = sticker_Message(number, get_media_id("perro_traje", "sticker"))
            msj_bot = body
            lista.append(listReplyData)

        elif (text == 'b') or ("reportar error" in text):
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

        elif "sí, envía el pdf" in text or text == 'c':
            # sticker = sticker_Message(number, get_media_id("pelfet", "sticker"))
            send(number, "Perfecto, por favor espera un momento.")
            msj_bot = 'Documento Guia Usuario.pdf'
            document = document_Message(number, sett.document_url, "Listo 👍🏻", "Guía de Usuario LogiFleet.pdf")
            send_Msj_whatsapp(document)
            replyButtonData = cont_conv(number, name, messageId)
            msj_bot = 'Guia de usuario'
            lista.append(replyButtonData)

        elif "ingresos" in text or 'menu ingresos' in text:
            est_conv[number] = 'consulta - ingreso'

            sendMenu(number, menuIng)

        elif "no, gracias" in text:
            replyButtonData = cont_conv(number, name, messageId)
            msj_bot = 'Continuar Conversacion?'
            lista.append(replyButtonData)

        elif 'finalizar' in text:
            textMessage = text_Message(number,
                                       "Perfecto! No dudes en contactarnos si tienes más preguntas. ¡Hasta luego!")
            lista.append(textMessage)
            msj_bot = 'Conversacion Finalizada\n' \
                      '********************************************'
            est_conv[number] = 'inicio'
        elif "menu principal" in text or "atras" in text:
            est_conv[number] = 'en curso'
            sendMenu(number)

        else:
            options = ["✅ Sí, envía el PDF.", "🏡 Menu Principal"]
            body = "No tenemos contemplada su consulta, le podemos ofrecer la guia de usuario la cual tendra todo lo " \
                   "que necesita para resolverla, o si quiere puede volver al menu principal "
            footer = "Quadrant"
            msj_bot = body
            replyButtonData = buttonReply_Message(number, options, body, footer, "sed3", messageId)
            lista.append(replyButtonData)

    elif est_conv[number] == 'consulta - ingreso':
        resp, continua = ingresos.option_ing(text)
        if resp == 'menu ingresos':
            sendMenu(number, menuIng)
            continua = False
        elif resp == 'menu principal':
            est_conv[number] = 'en curso'
            sendMenu(number)
            continua = False
        else:
            send(number, resp)

        if continua:
            est_conv[number] = 'en curso'
            options = ["✅ Menu Ingresos", "🏡 Menu Principal"]
            body = "Espero que esto haya resolvido su consulta\n" \
                   "por favor indique si quiere volver a un menu o escriba 'Finalizar' para terminar esta " \
                   "conversacion, gracias. "
            footer = "Quadrant"
            msj_bot = body
            replyButtonData = buttonReply_Message(number, options, body, footer, "sed3", messageId)
            lista.append(replyButtonData)

    if msj_bot != '':
        registerChat(number, 'Botifleet', msj_bot)
        msj_bot = ''
    feedback()

    for item in lista:
        send_Msj_whatsapp(item)
        ultimo_tiempo = datetime.now()
        time_inactive[number] = ultimo_tiempo


def send(number, text):
    textMessage = text_Message(number, text)
    if msj_bot != '':
        registerChat(number, 'Botifleet', text)
    send_Msj_whatsapp(textMessage)
    time.sleep(3)


def feedback():
    pass


def review_time(number):
    global ultimo_tiempo
    global est_conv
    global time_inactive

    if number not in est_conv:
        est_conv[number] = 'inicio'
        return

    tiempo_actual = datetime.now()
    inactive_real = tiempo_actual - time_inactive[number]
    # Si el tiempo de inactividad es mayor a 60 minutos, reiniciar la conversación
    if inactive_real > timedelta(minutes=60):
        est_conv[number] = "inicio"


# este codigo soluciona el agregado del 9 en Argentina
def replace_start(s):
    st = str(s)
    number = st[3:]
    if st.startswith("549"):
        newest = "54" + number
        return newest
    else:
        return st
