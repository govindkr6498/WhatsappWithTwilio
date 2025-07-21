from fastapi import FastAPI, Request
from fastapi.responses import Response
from twilio.twiml.messaging_response import MessagingResponse
from main import SalesRAGAgent

app = FastAPI()

# Initialize chatbot with the specific PDF
pdf_path = '/home/ubuntu/WhatsappWithTwilio/Emaar_FAQ.pdf'
chatbot = SalesRAGAgent(pdf_path)

@app.post("/webhook/whatsapp")
async def whatsapp_webhook(request: Request):
    form = await request.form()
    user_input = form.get('Body', '')
    
    # Use the correct method from SalesRAGAgent
    reply_text = chatbot.process(user_input)['response']

    # Twilio WhatsApp response
    twilio_resp = MessagingResponse()
    twilio_resp.message(reply_text)
    
    return Response(content=str(twilio_resp), media_type="application/xml")
