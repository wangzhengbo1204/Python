#-*- coding:utf-8 -*-
'''
Created on 2012-11-12 @author: GFTOwenWang
'''
import paramiko

def ssh_exec_comm(host, port, username, password, list_command):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    key_filename=ur"D:\GFT\NetWork\id_rsa"
    client.connect(host, port, username, password,key_filename=key_filename)
    for command in list_command:
        stdin, stdout, stderr = client.exec_command(command)
        list_line = []
        for line in stderr.readlines():
            list_line.append(line)
            
        if list_line:
            print list_line
            print "%s (fail.....!)" % command
            return False
        else:
            print "%s (Successful!)" % command
    
    client.close()
    return True


def main():
    #host="172.16.101.115"
    host="222.73.115.215"
    port=22
    username='root'
    password='dimelilo'
    list_command=['ls']
    ssh_exec_comm(host, port, username, password, list_command)
    
if __name__ == '__main__':
    main()
    
    
        