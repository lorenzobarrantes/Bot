
# Whatsapp Bot con Python

## Descarga el proyecto


```bash
git clone https://github.com/lorenzobarrantes/Bot.git
```
### Solicitar el archivo .env para el correcto funcionamiento
## Funcionalidades

- Enviar mensaje de texto
- Enviar menus como botones o listas
- Enviar stickers
- Marcar los mensajes como "visto"
- Reaccionar con emojis los mensajes del usuario
- Enviar documentos pdf


## Para probarlo localmente

1. Dirigete al directorio donde descargaste el proyecto

```bash
  cd chatbotwms
```
2. Crea un ambiente virtual con al menos la version de [python 3.10](https://www.python.org/downloads/)

Requiere pip y virtualenv
```commandline
pip install pip
pip install virtualenv
```
Crear carpeta .venv (si no esta en la clonacion)
```bash
  virtualenv .venv
```
3. Activa el ambiente virtual

Linux/Mac
```bash
  source .venv/bin/activate
```
Windows
```commandline
   .\.venv\Scripts\activate 
```
4. Instala las dependencias

```bash
  pip install -r requirements.txt
```

5. Corre la aplicacion

```bash
  python app.py
```
6. Checkear que este levantada http://127.0.0.1:5000/bienvenido

## Simular mensajes del usuario con postman

```javascript
Ingresar la URL
http://127.0.0.1:5000/webhook
Hacer un POST

en body, seleccionar "raw" y tipo "JSON", no olvidar agregar tu número
{
  "object": "whatsapp_business_account",
  "entry": [{
      "id": "WHATSAPP_BUSINESS_ACCOUNT_ID",
      "changes": [{
          "value": {
              "messaging_product": "whatsapp",
              "metadata": {
                  "display_phone_number": "PHONE_NUMBER",
                  "phone_number_id": "PHONE_NUMBER_ID"
              },
              "contacts": [{
                  "profile": {
                    "name": "NAME"
                  },
                  "wa_id": "PHONE_NUMBER"
                }],
              "messages": [{
                  "from": "agrega tu numero",
                  "id": "wamid.ID",
                  "timestamp": "TIMESTAMP",
                  "text": {
                    "body": "hola"
                  },
                  "type": "text"
                }]
          },
          "field": "messages"
        }]
  }]
}
```

