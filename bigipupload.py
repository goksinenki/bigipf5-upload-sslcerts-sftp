#!/usr/bin/python
# -*- coding: UTF-8 -*-
# A script to ssh into a cisco device, set the terminal length
# such that paging is turned off, then run commands.
# the results go into 'resp', then are displayed.
# Tweak to your hearts content!

import paramiko
from paramiko import SSHClient
from scp import SCPClient
import cmd
import time
import sys
import requests, json
import pathlib



def scpdosyagonderimi(IP):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(IP, username='root', password='yourpassword')
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    file_names = open('filenames.txt', 'rb')
    for line in file_names:
        l = [i.strip() for i in line.decode().split(' ')]
        filename = l[0]
        #print (filename)
        #print (IP)
        #dosyauzantilari = (filename.split('.'))
        dosyauzantisi = pathlib.Path(f'{filename}').suffix
        #print (dosyauzantisi)
        if dosyauzantisi == ".crt":
            with SCPClient(ssh.get_transport()) as scp:
                scp.put(f'{filename}', recursive=False, remote_path=f'/config/ssl/ssl.crt/{filename}')
        elif dosyauzantisi == ".key":
            with SCPClient(ssh.get_transport()) as scp:
                scp.put(f'{filename}', recursive=False, remote_path=f'/config/ssl/ssl.key/{filename}')
    ssh.close()
    file_names.close()



my_file = open('bigipf5ips.txt', 'rb')
for line in my_file:
    l = [i.strip() for i in line.decode().split(' ')]
    IP = l[0]
    scpdosyagonderimi(IP)
my_file.close()

