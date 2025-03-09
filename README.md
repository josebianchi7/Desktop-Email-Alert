# Desktop-Email-Alert

#### Microservice that accepts event messages and sends a desktop notification and email. This microservice will also send event messages to a log database for record keeping.


## Authors

- [@josebianchi7](https://github.com/josebianchi7)


## Deployment

To deploy this project, the following is required:

1. Install the following necessary Python libraries (if not already installed):

    For HTTP request handeling of JSON object:
    ```bash
      $ pip install flask
    ```
    ```bash
      $ pip install requests
    ```
    ```bash
      $ pip install json
    ```
    
    For desktop notifications:
    ```bash
      $ pip install plyer
    ```

    For email notifications
    ```bash
      $ pip install smtplib
    ```

2. Create credentials file, credentials.py, and include the following data in string format:
  
    1. url_post = URL to post to a database. Ensure JSON keys match what database is expecting.

    2. email login and recipient data. Recommend creating new email for this program. I used Gmail, enabled 2FA, and created an App password. See references for link about Gmail App passwords.

        from_address = your new email

        from_password = 16 character app password

        to_email = recipient email

    3. Additionaly, but not required, store IP and Port for Flask app in credentials.py as well.

        host_ip = unused IP on your network

        host_port = 3000



## References and Acknowledgements

[1] sanjuxdr, “Python Desktop Notifier Using Plyer Module,” GeeksforGeeks, Jul. 01, 2020. https://www.geeksforgeeks.org/python-desktop-notifier-using-plyer-module/ (accessed Mar. 07, 2025).

[2] D. Kontorskyy and V. Ristić, “Sending Emails in Python with Gmail 2023 Tutorial,” mailtrap.io, Dec. 29, 2022. https://mailtrap.io/blog/python-send-email-gmail/ (accessed Mar. 09, 2025).

[3] Google, “Sign in with App Passwords - Gmail Help,” support.google.com. https://support.google.com/mail/answer/185833?hl=en (accessed Mar. 09, 2025).


