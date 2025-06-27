
import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_data_taligram(message):


    token = "7641994328:AAF5yHy2yReEVHxIh0nmGsnhHW7tNABmFGY"
    chat_id = "6375857077"
    # message = "🚀 Hello Pjpk! This is a test message from your Telegram bot."

    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message
    }

    requests.post(url, data=payload)
    CHAT_ID = "-1002478196930"


    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
    "chat_id": CHAT_ID,
    "text": message
    }

    response = requests.post(url, data=payload)

    if response.ok:
        pass
    else:
        print("❌ Error:", response.text)

    # Your Gmail
    sender_email = "robostemia@gmail.com"
    receiver_email = "robostemia@gmail.com"
    password = "noqq wbqx gfwt pbwt"  # 🔁 Replace with Gmail App Password

    # Email content
    subject = "Contract From Details  😃"
    body = message

    # Construct email message
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
        print("✅ Email sent successfully!")
    except Exception as e:
        print("❌ Error:", e)


def Order_detail_Send(message):

    token = "7641994328:AAF5yHy2yReEVHxIh0nmGsnhHW7tNABmFGY"  # 🔐 Don't reuse the old one
    chat_id = "-1002876010047"
    # message = "Hello, this is a test message from the bot."

    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {"chat_id": chat_id, "text": message}

    response = requests.post(url, data=payload)

    # Your Gmail
    sender_email = "robostemia@gmail.com"
    receiver_email = "robostemia@gmail.com"
    password = "noqq wbqx gfwt pbwt"  # 🔁 Replace with Gmail App Password

        # Email content
    subject = "Order Placed ❤️😎"
    body = message
    # Construct email message
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
        print("✅ Email sent successfully!")
    except Exception as e:
        print("❌ Error:", e)



# print(response.json())

# send_data_taligram()





# import requests

# token = "7641994328:AAF5yHy2yReEVHxIh0nmGsnhHW7tNABmFGY"
# url = f"https://api.telegram.org/bot{token}/deleteWebhook"

# response = requests.get(url)
# print(response.json())


# find taligram group id
# import requests
# import json

# token = "7641994328:AAF5yHy2yReEVHxIh0nmGsnhHW7tNABmFGY

# url = f"https://api.telegram.org/bot{token}/getUpdates"
# response = requests.get(url)
# print(response.json())