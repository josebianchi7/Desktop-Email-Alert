# Author: Jose Bianchi 
# Description: Program to get event messages from a main program or other services, 
#   and send event details to database log, generate a desktop notification and email notification.

import requests
import json
from plyer import notification
from flask import Flask, request, jsonify
from credentials import host_ip
from credentials import host_port
from credentials import url_post
import smtplib
from email.message import EmailMessage
from credentials import from_password
from credentials import from_address
from credentials import to_email


def post_to_db_log(message):
    """
    HTTP Post function that sends message to db log.

    :param message: dictionary object, must include timestamp and eventDescription keys
        Ex:
        message = {
                "timestamp": datetime.now().strftime('%Y-%m-%dT%H:%M:%S'),
                "eventDescription": "event A has occured."
            }
    """
    # Convert the message to a JSON object for sending in HTTP Post
    json_data = json.dumps(message, indent=4)   
    
    # Send new data via POST request
    response = requests.post(
        url_post, 
        json_data, 
        headers={ "Content-Type": "application/json" }
        )

    # Check response from server
    if response.status_code == 200:
        print(f"\nDatabase Response: {response.json()}")
    else:
        print(f"Failed to log to database. Status code: {response.status_code}")
    
    return json_data


def send_email(subject, body):
    """
    Sends email to designated email. 

    :param subject: email subject
    :param body: email body
    """
    sender_email = from_address
    password = from_password
    receiver_email = to_email

    # Create the email message
    msg = EmailMessage()
    msg.set_content(body)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = receiver_email

    # Send the email
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(sender_email, password)
            server.send_message(msg)
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error: {e}")


app = Flask(__name__)

@app.route('/event', methods=['POST'])
def receive_message():
    if request.is_json:
        data = request.get_json()
        print(f"Received POST message successfully: {data}")

        # Format data for db log as needed
        if 'timestamp' in data and 'eventDescription' in data:
            event_msg = data.get('eventDescription')
            time = data.get('timestamp')
            post_to_db_log(data)      
            alert_title = "NETWORK ALERT"
            alert_message=f"Network Event: {event_msg}\nTimestamp: {time}"
            
            # Desktop notification 
            notification.notify(
                title=alert_title,
                message=alert_message,
                timeout=10,
                )

            if 'source' in data and data.get('source') != 'Bandwidth':
                print(alert_title)
                print(alert_message)
                # Email notification
                send_email(alert_title, alert_message)

        return jsonify({'response': 'Event data as JSON received'}), 200
    else:
        return jsonify({"error": "Request must be JSON"}), 400
    

if __name__ == '__main__':
    app.run(host=host_ip, port=host_port)

