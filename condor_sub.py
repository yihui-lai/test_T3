#!/bin/env python
"""Executes arbitrary command on condor. Adds $(ProcId) to arguments.
Edit BASEDIR, DATESTR"""
import sys
import subprocess
from string import Template
import time
import os # path, makedirs

def execute(args):
    """Wrapper function to execute arbitrary shell commands"""
    print '################################'
    print 'args: ', args
    p = subprocess.Popen(args, shell=True, executable='/bin/bash')
    # p = subprocess.call(args, shell=True, executable='/bin/bash')
    p.wait()
    return p
    print '################################'

print sys.argv
queue = int(sys.argv[1])
command = sys.argv[2]

command_list = command.split()
BASEDIR = "/data/users/yihuilai/test_T3/condor/"
DATESTR = time.strftime("%Y-%m-%d-%H")
DIRECTORY = os.path.join(BASEDIR, DATESTR) # DIRECTORY = BASEDIR/YY-MM-DD
if not os.path.exists(DIRECTORY):
    os.makedirs(DIRECTORY)
kw_dict = {}
kw_dict['DIRECTORY'] = DIRECTORY
kw_dict['EXECUTABLE'] = command_list[0]
kw_dict['ARGUMENTS']  = " ".join(command_list[1:])
kw_dict['QUEUE']  = "%d" % queue
kw_dict['DATE'] = time.strftime("%Y-%m-%d-%H")

jdl_template ="""
universe = vanilla
Executable = ${EXECUTABLE}
should_transfer_files = NO
Requirements = TARGET.FileSystemDomain == "privnet"
# && machine == "r510-0-6.privnet"
output                = ${DIRECTORY}/condor_test.$(ClusterId).$(ProcId).out
error                 = ${DIRECTORY}/condor_test.$(ClusterId).$(ProcId).err
log                   = ${DIRECTORY}/condor_test.$(ClusterId).log
arguments             = ${ARGUMENTS} $(ProcId)
Queue ${QUEUE}
"""

t = Template(jdl_template)
jdl = t.safe_substitute(kw_dict)

jdlfile = open('test.jdl', 'w')
jdlfile.write(jdl)
jdlfile.close()

execute("condor_submit  getenv=True test.jdl")

