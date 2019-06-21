#!/usr/bin/env python3

from mailer import SendViaMail
from topposts import TopPosts, BeautifyTopPosts

if __name__ == '__main__':
    for sub in ['netsec', 'devops']:
        tp = TopPosts(sub)
        bp = BeautifyTopPosts(sub, tp.top_posts)
        SendViaMail(
            from_addr = "Reddit Top Posts <rtp@alorenzi.eu>",
            to_addr = "alorenzi@alorenzi.eu",
            subj =  "[%s] Reddit Top Posts" % sub,
            message_text= bp.markdown()
        )