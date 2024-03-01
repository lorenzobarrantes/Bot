import os
from dotenv import load_dotenv

load_dotenv()

token = os.getenv("token")

whatsapp_token = os.getenv("whatsapp_token")

whatsapp_url = os.getenv("whatsapp_url")

whatsapp_id_number = os.getenv("whatsapp_id_number")

whatsapp_id = os.getenv("whatsapp_id")

openai_id = os.getenv("openai_id")

mail_pass = os.getenv("mail_pass")

stickers = {
    "sticker_1": "https://www.quadrant.com.ar/sticker.webp",
    "sticker_2": "https://www.quadrant.com.ar/sticker.webp",
    "sticker_3": "https://www.quadrant.com.ar/sticker.webp",
    "sticker_4": "https://www.quadrant.com.ar/sticker.webp",
}

document_url = "https://www.quadrant.com.ar/documentoimplementacionlogifleet.pdf"
error_url = "https://www.quadrant.coom.ar/reporteerroreslogifleet.pdf"
