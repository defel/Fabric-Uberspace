from fabric.api import *
from fabric.contrib import files

import crypt
import os
import string
import random

def __generate_salt(count):
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(count))

def qmail_alias_add(name, dest = None):
    qmail_alias_remove(name)

    fn = "~/.qmail-{0}".format(name)
    files.append(fn, dest or env.user)

def qmail_alias_remove(name):
    fn = "~/.qmail-{0}".format(name)
    if files.exists(fn):
        run("rm -f {0}".format(fn))

def qmail_alias_list():
    with cd('~'):
        all = run('ls .qmail-*').split()
        all.remove(".qmail-default")
        all.sort()
        return [s[7:] for s in all]

def vmail_user_add(name, password):
    vmail_user_remove(name)
    pwc = crypt.crypt(password, __generate_salt(2))
    run('vadduser --password={1} {0}'.format(name, pwc))

def vmail_user_remove(name):
    if files.exists("~/users/{0}".format(name)):
        run('vdeluser {0}'.format(name))

