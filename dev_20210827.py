import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

#html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Ameet Mund'
email['to'] = 'ameetmund@gmail.com'
email['subject'] = 'Hello Ameet!!! How are you'

#email.set_content(html.substitute({'name': 'TinTin'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
  smtp.ehlo()
  smtp.starttls()
  smtp.ehlo()
  smtp.login('ameetmund@gmail.com', 'System#001')
  smtp.send_message(email)
  print('all good boss!')