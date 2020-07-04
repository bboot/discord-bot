#!/usr/bin/env python3
import atexit
from datetime import datetime
import subprocess
import time

def exit_time():
    print('')
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%3s")
    print('{} ################### Bye!'.format(timestamp))
atexit.register(exit_time)

def execute(cmd):
    popen = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                             universal_newlines=True)
    for stdout_line in iter(popen.stdout.readline, ""):
        yield stdout_line
    popen.stdout.close()
    return_code = popen.wait()
    if return_code:
        raise subprocess.CalledProcessError(return_code, cmd)

def run_cmd(cmd):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%3s")
    print('{} ################### Launching BOT!!!'.format(timestamp))
    for output in execute(cmd):
        print(output, end='')

while True:
    try:
#        run_cmd(['node', 'bot.js'])
        run_cmd(['python3', 'bot.py'])
    except KeyboardInterrupt as e:
        break
    time.sleep(3)
