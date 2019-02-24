#!/bin/bash

#( /root/update_email_aliases.py && grep '^[^#].*$' /etc/postfix/virtual_static ) > /etc/postfix/virtual
cd /opt/tbp-mailing
make update

