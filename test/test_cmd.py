# -*- coding: UTF-8 -*-
import os
import subprocess
import shlex

from nose.tools import eq_

DIR = os.path.dirname(os.path.realpath(__file__))
TESTPLUGINS = os.path.join(DIR, "plugins")

# http://stackoverflow.com/a/13160748/42559
def sh(cmd):
     proc = subprocess.Popen(shlex.split(cmd), stdout=subprocess.PIPE)
     output = proc.communicate()[0].decode("utf8")
     ret = proc.returncode
     return output, ret

def test_cmd():
    msg = u"!echo Iñtërnâtiônàlizætiøn"
    out, res = sh(u"slask -c '{0}' --pluginpath {1}".format(msg, TESTPLUGINS).encode("utf8"))
    out = out.strip()
    eq_(out, msg)
    eq_(res, 0)
