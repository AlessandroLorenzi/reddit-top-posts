import smtplib, ssl, datetime, os
from email.mime.text import MIMEText


class SendViaMail():
    def __init__(self, from_addr, to_addr, subj, message_text ):
        date = datetime.datetime.now().strftime( "%d/%m/%Y %H:%M" )

        
        msg = MIMEText(message_text)
        msg['Subject'] = subj
        msg['From'] = from_addr
        msg['To'] = to_addr
        
        smtp_server = self.create_smtp_server()
        smtp_server.sendmail(from_addr, to_addr, msg.as_string())
        smtp_server.quit()

    def create_smtp_server(self):
        smtp = {
            'host': os.environ['SMTP_HOST'],
            'port': os.environ['SMTP_PORT'],
            'user': os.environ['SMTP_USER'],
            'password': os.environ['SMTP_PASSWORD'],
        }
        
        _DEFAULT_CIPHERS = (
        'ECDH+AESGCM:DH+AESGCM:ECDH+AES256:DH+AES256:ECDH+AES128:DH+AES:ECDH+HIGH:'
        'DH+HIGH:ECDH+3DES:DH+3DES:RSA+AESGCM:RSA+AES:RSA+HIGH:RSA+3DES:!aNULL:'
        '!eNULL:!MD5')

        smtp_server = smtplib.SMTP(smtp['host'], port=smtp['port'])

        # only TLSv1 or higher
        context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
        context.options |= ssl.OP_NO_SSLv2
        context.options |= ssl.OP_NO_SSLv3

        context.set_ciphers(_DEFAULT_CIPHERS)
        context.set_default_verify_paths()
        context.verify_mode = ssl.CERT_REQUIRED

        if smtp_server.starttls(context=context)[0] != 220:
            raise Exception
        
        smtp_server.login(smtp['user'], smtp['password'])
        return smtp_server