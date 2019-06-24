#!/usr/bin/env python3

from mailer import SendViaMail
from topposts import TopPosts, BeautifyTopPosts
import os

if __name__ == '__main__':
    subs = os.environ.get('SUBS', '').split(',')
    to_addr = os.environ.get('TO_ADDR', '')
    from_addr = os.environ.get('FROM_ADDR', '')
    smtp = {
        'host': os.environ['SMTP_HOST'],
        'port': os.environ['SMTP_PORT'],
        'user': os.environ['SMTP_USER'],
        'password': os.environ['SMTP_PASSWORD'],
    }

    for sub in subs:
        tp = TopPosts(sub)
        bp = BeautifyTopPosts(sub, tp.top_posts)

        SendViaMail(
            from_addr = from_addr,
            to_addr = to_addr,
            subj =  "[%s] Reddit Top Posts" % sub,
            message_text= bp.markdown(),
            smtp = smtp
        )