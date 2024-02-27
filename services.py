import requests
import sett
import json
import time
from datetime import datetime, timedelta

ultimo_mensaje = ""
ultimo_tiempo = datetime.now()
tiempo_inactividad = {}
estado_conversaciones = {}
msje_boti = ""
saludo = ['hola', 'buenas', 'holaa', 'ayuda']
opciones = ['✅ consultas', '📎 guia de usuario']


def obtener_Mensaje_whatsapp(message):
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


def enviar_Mensaje_whatsapp(data):
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


def buttonReply_Message(number, options, body, footer, sedd, messageId):
    buttons = []
    for i, option in enumerate(options):
        buttons.append(
            {
                "type": "reply",
                "reply": {
                    "id": sedd + "_btn_" + str(i + 1),
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


def listReply_Message(number, options, body, footer, sedd, messageId):
    rows = []
    for i, option in enumerate(options):
        rows.append(
            {
                "id": sedd + "_row_" + str(i + 1),
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
    elif media_type == "image":
        media_id = sett.images.get(media_name, None)
    elif media_type == "video":
        media_id = sett.videos.get(media_name, None)
    elif media_type == "audio":
        media_id = sett.audio.get(media_name, None)
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


def registro(number, nombre, text):
    hora_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Crear el mensaje a registrar
    mensaje_registro = f"{hora_actual} - {nombre}: {text}\n"

    # Guardar el mensaje en un archivo de texto
    with open(f"conversacion_{number}.txt", "a", encoding="utf-8") as archivo:
        archivo.write(mensaje_registro)
    archivo.close()

def administrar_chatbot(text, number, messageId, name):
    global ultimo_mensaje
    global ultimo_tiempo
    global estado_conversaciones
    global msje_boti

    registro(number, name, text)

    text = text.lower()  # mensaje que envio el usuario
    list = []
    print("mensaje del usuario: ", text)

    markRead = markRead_Message(messageId)
    list.append(markRead)
    time.sleep(2)

    # Actualizar el tiempo y el mensaje más reciente
    ultimo_mensaje = text

    revisar_inactividad(number)

    if estado_conversaciones[number] == 'inicio' or text in saludo:
        body = "¡Hola! 👋 Bienvenido a WMS Logifleet. ¿Cómo podemos ayudarle hoy?"
        footer = "Quadrant"
        options = ["✅ Consultas", "📎 Reportar Error"]
        msje_boti = body

        replyButtonData = buttonReply_Message(number, options, body, footer, "sed1", messageId)
        # replyReaction = replyReaction_Message(number, messageId, "🫡")
        # list.append(replyReaction)
        list.append(replyButtonData)
        estado_conversaciones[number] = 'en curso'

    elif estado_conversaciones[number] == 'en curso' or text in opciones:
        if "consultas" in text:
            body = "Tenemos varias áreas de consulta para elegir. ¿Cuál de estos servicios le gustaría explorar?"
            footer = "Quadrant"
            options = ["Ingresos", "Egresos", "Inventario", "Datos"]

            listReplyData = listReply_Message(number, options, body, footer, "sed2", messageId)
            # sticker = sticker_Message(number, get_media_id("perro_traje", "sticker"))
            msje_boti = body
            list.append(listReplyData)

        elif "reportar error" in text:
            # sticker = sticker_Message(number, get_media_id("pelfet", "sticker"))
            textMessage = text_Message(number,
                                       "Gracias por reportar los errores. Por favor sigue los pasos detallados en el siguiente documento")

            # enviar_Mensaje_whatsapp(sticker)
            msje_boti = textMessage
            enviar_Mensaje_whatsapp(textMessage)
            time.sleep(3)

            document = document_Message(number, sett.error_url, "", "Reporte de errores.pdf")
            enviar_Mensaje_whatsapp(document)
            time.sleep(3)
            estado_conversaciones[number] = 'inicio'


        elif "sí, envía el pdf" in text:
            # sticker = sticker_Message(number, get_media_id("pelfet", "sticker"))
            textMessage = text_Message(number, "Genial, por favor espera un momento.")

            # enviar_Mensaje_whatsapp(sticker)
            enviar_Mensaje_whatsapp(textMessage)
            time.sleep(3)
            msje_boti = 'Documento Guia Usuario.pdf'

            document = document_Message(number, sett.document_url, "Listo 👍🏻", "Guía de Usuario LogiFleet.pdf")
            enviar_Mensaje_whatsapp(document)
            time.sleep(3)
            estado_conversaciones[number] = 'inicio'

        elif "no, gracias" in text:
            textMessage = text_Message(number,
                                       "Perfecto! No dudes en contactarnos si tienes más preguntas. ¡Hasta luego!")
            list.append(textMessage)
            msje_boti = textMessage
            estado_conversaciones[number] = 'inicio'

        else:
            options = ["✅ Sí, envía el PDF.", "⛔ No, gracias"]
            body = "No tenemos contemplada su consulta, le podemos ofrecer la guia de usuario la cual tendra todo lo " \
                   "que necesita para resolverla. "
            footer = "Quadrant"
            msje_boti = body
            replyButtonData = buttonReply_Message(number, options, body, footer, "sed3", messageId)
            list.append(replyButtonData)
            
    registro(number, 'Botifleet', msje_boti)

    for item in list:
        enviar_Mensaje_whatsapp(item)
        ultimo_tiempo = datetime.now()
        # msje_boti = json.loads(item.split("Mensaje: ")[1])
        tiempo_inactividad[number] = ultimo_tiempo


def revisar_inactividad(number):
    global ultimo_tiempo
    global estado_conversaciones
    global tiempo_inactividad

    if number not in estado_conversaciones:
        estado_conversaciones[number] = "inicio"
        print('inicio')
        return

    tiempo_actual = datetime.now()
    print(tiempo_actual)
    tiempo_inactivo = tiempo_actual - tiempo_inactividad[number]
    print(tiempo_inactivo)
    print(estado_conversaciones)
    # Si el tiempo de inactividad es mayor a 30 minutos, reiniciar la conversación
    if tiempo_inactivo > timedelta(minutes=30):
        estado_conversaciones[number] = "inicio"
        print(estado_conversaciones)


# este codigo soluciona el agregado del 9 en Argentina
def replace_start(s):
    st = str(s)
    number = st[3:]
    if st.startswith("549"):
        newst = "54" + number
        return newst
    else:
        return st
    return s

administrar_chatbot('hola', 113234556, 2134123123, 'lb')