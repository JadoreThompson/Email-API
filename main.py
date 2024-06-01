import uvicorn
from fastapi import FastAPI,  HTTPException
from pydantic import BaseModel

import smtplib
import ssl
from email.message import EmailMessage

import os
from dotenv import load_dotenv


app = FastAPI()

class Email(BaseModel):
    recipient: str
    subject: str
    body: str

load_dotenv('.env')
email_sender = os.getenv('EMAIL_SENDER')
email_password = os.getenv('EMAIL_PASSWORD')

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post('/send_email')
def send_email(email: Email):
    try:
        em = EmailMessage()
        em['From'] = email_sender
        em['To'] = email.recipient
        em['Subject'] = email.subject
        em.set_content(email.body)

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
            server.login(email_sender, email_password)
            server.sendmail(email_sender, email.recipient, em.as_string())

        return {"message": "Email sent successfully"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


    return {"Email": email}



if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)