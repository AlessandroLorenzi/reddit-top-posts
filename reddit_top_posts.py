#!/usr/bin/env python3

import os

from mailer import SendViaMail
from topposts import TopPosts, BeautifyTopPosts

if __name__ == '__main__':
    SUBS = os.environ.get('SUBS', '').split(',')
    TO_ADDR = os.environ.get('TO_ADDR', '')
    FROM_ADDR = os.environ.get('FROM_ADDR', '')
    SMTP = {
        'host': os.environ['SMTP_HOST'],
        'port': os.environ['SMTP_PORT'],
        'user': os.environ['SMTP_USER'],
        'password': os.environ['SMTP_PASSWORD'],
    }

    MESSAGE = "# Reddit top Posts \n"

    SUB = None
    for SUB in SUBS:
        tp = TopPosts(SUB)
        bp = BeautifyTopPosts(SUB, tp.top_posts)
        MESSAGE = MESSAGE + bp.markdown()

    # print(message)
    SendViaMail(
        from_addr=FROM_ADDR,
        to_addr=TO_ADDR,
        subj="Reddit Top Posts",
        message_text=MESSAGE,
        smtp=SMTP
    )
