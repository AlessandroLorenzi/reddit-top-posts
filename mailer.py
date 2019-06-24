import smtplib
import ssl
from email.mime.text import MIMEText

class SendViaMail():
    def __init__(self, from_addr, to_addr, subj, message_text, smtp):
        msg = MIMEText(message_text)
        msg['Subject'] = subj
        msg['From'] = from_addr
        msg['To'] = to_addr

        smtp_server = self.create_smtp_server(smtp)
        smtp_server.sendmail(from_addr, to_addr, msg.as_string())
        smtp_server.quit()

    @classmethod
    def create_smtp_server(cls, smtp):
        default_chipers = (
            'ECDH+AESGCM:DH+AESGCM:ECDH+AES256:DH+AES256:ECDH+AES128:DH+AES:ECDH+HIGH:'
            'DH+HIGH:ECDH+3DES:DH+3DES:RSA+AESGCM:RSA+AES:RSA+HIGH:RSA+3DES:!aNULL:'
            '!eNULL:!MD5')

        smtp_server = smtplib.SMTP(smtp['host'], port=smtp['port'])

        # only TLSv1 or higher
        context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
        context.options |= ssl.OP_NO_SSLv2
        context.options |= ssl.OP_NO_SSLv3

        context.set_ciphers(default_chipers)
        context.set_default_verify_paths()
        context.verify_mode = ssl.CERT_REQUIRED

        if smtp_server.starttls(context=context)[0] != 220:
            raise Exception

        smtp_server.login(smtp['user'], smtp['password'])
        return smtp_server
