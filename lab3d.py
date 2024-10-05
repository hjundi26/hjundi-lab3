#!/usr/bin/env python3

#Author ID: hjundi


import subprocess

def free_space():
    storage = subprocess.Popen(["df -h | grep '/$' | awk '{print $4}'"], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    storage = storage.communicate()
    stdout = storage[0].decode('utf-8').strip()
    print(stdout)
    return stdout

free_space()
