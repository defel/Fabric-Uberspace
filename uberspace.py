#!/usr/bin/env python
from fabric.api import *
from fabric.contrib import files

env.hosts = ['orion.uberspace.de']

#Neues Qmail-Alias. Default-Destination: User-Mailbox
def qmail_alias_add(name, dest = None):
    qmail_alias_remove(name)

    fn = "~/.qmail-{0}".format(name)
    files.append(fn, dest or env.user)

def qmail_alias_remove(name):
    fn = "~/.qmail-{0}".format(name)
    if files.exists(fn):
        run("rm -f {0}".format(fn))