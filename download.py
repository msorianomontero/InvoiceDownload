# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 10:02:16 2020

@author: Miguel

IMPORTANTE PARA QUE JALE HAY QUE HABILITAR EL ACCESO A APLICACIONES NO SEGURAS EN GOOGLE
YA NO ES NECESARIO HABILITAR ACCESO A APLICACIONES NO SEGURAS, YA SE TIENE UN APP PASSWORD
"""

import imaplib
import os
import email
import chardet

email_user = "yourEmail@gmail.com"
email_pass = "passProvidedByGoogle"


mail = imaplib.IMAP4_SSL("imap.gmail.com",993)

mail.login(email_user, email_pass)

mail.select('[Gmail]/directoryWhereInvoicesAreStored')

#type, data = mail.search(None, 'FROM facturaelectronica@wal-mart.com')
type, data = mail.search(None, 'ALL')
#type, data = mail.search(None, "(SENTBEFORE 23-Mar-2020)")
mail_ids = data[0]
id_list = mail_ids.split()

ruta = 'D:/yourDestinationDirectory/'
archivoLog = ruta + 'download.log'
logfile = open(archivoLog, 'w')

for num in data[0].split():
    typ, data = mail.fetch(num, '(RFC822)' )
    raw_email = data[0][1]
    

# converts byte literal to string removing b''
    try:
        raw_email_string = raw_email.decode('utf-8')
        print("encodificado: utf8")
    except UnicodeError:
        encoding = chardet.detect(raw_email)
        encodificado = encoding['encoding']
        print("encodificado:", encodificado)
        raw_email_string = raw_email.decode(encodificado)
        
    email_message = email.message_from_string(raw_email_string)
    print(email_message['Subject'])
    print(email_message['From'])
    logfile.write(email_message['From'] + '@' + email_message['Subject'] +'\n')

# downloading attachments
    for part in email_message.walk():
        # this part comes from the snipped I don't understand yet... 
        if part.get_content_maintype() == 'multipart':
            continue
        if part.get('Content-Disposition') is None:
            continue
        fileName = part.get_filename()
        print("Intentando guardar archivo:", fileName)
        if bool(fileName):
            filePath = os.path.join('D:/yourDestinationDirectory', fileName)
            print("Filepath es:", filePath, "\n")
            if not os.path.isfile(filePath) :
                fp = open(filePath, 'wb')
                fp.write(part.get_payload(decode=True))
                fp.close()
            subject = str(email_message).split("Subject: ", 1)[1].split("\nTo:", 1)[0]
            #print('Downloaded "{file}" from email titled "{subject}" with UID {uid}.'.format(file=fileName, subject=subject, 1))
            #print("Downloaded ", fileName,"from email titled", subject ," with UID ")

logfile.close()
