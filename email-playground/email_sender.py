#!/usr/bin/env python3

import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path 

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Kiki Sanni'
email['to'] = 'okikiolasanni00@gmail.com'
email['subject'] = 'You won 1,000,000 dollars!'

email.set_content(html.substitute({'name': 'Tim'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
  smtp.ehlo()
  smtp.starttls()
  smtp.login('pythonpractice29@gmail.com', 'udemypython')
  smtp.send_message(email)
  print('all good sis!')
  