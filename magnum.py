#! /usr/bin/env python

#----------------------------------------------------------------------------------
# Descripcion:
# Script para enviar un comandos Quartz al servidor magnum
# Modo de ejecucion:
#  $ magnum -c ".SV1,7"
# Fecha Modificacion: 11 NOV 2016
# Autor: JCRAMIREZ
#----------------------------------------------------------------------------------

import os, sys, time, select, traceback, smtplib, datetime, argparse, re, telnetlib, getpass

server="192.168.2.12"
port=5001
telnet_timeout = 1 
 
def connect(ipaddress,port):
	# Establece conexion via telnet sin autenticacion con un servidor usando el puerto indicado
	try:
		tn = telnetlib.Telnet(ipaddress, port)
        	return tn
    	except Exception, e:
        	print "Error connecting to " + ipaddress
        	print "Exception: %s" % str(e) 

def disconnect(tn):
	# Se desconecta la sesion telnet el apuntador indicado.
	try:
        	tn.close()
	except Exception, e:
        	print "Error: clossing the telnet"
        	print "Exception: %s" % str(e)
    	return True 

def send_command(ipaddress, port, cmd):
	# Envia el comando ingresado al servidor de Ip por el puerto indicado.
	tn = connect(ipaddress,port)
	try:
		tn.write(cmd + "\r\n")
		output = tn.read_until(".E",telnet_timeout)
	except Exception, e:
        	print "Error: sending the cmd to Magnum server "
        	print "Exception: %s" % str(e)
    	print output
	disconnect(tn)
			
def main():
	__author__ = 'jcramirez'
	parser = argparse.ArgumentParser(description='Script to send a cmd via telnet to a Magnum Server')
	parser.add_argument('-c','--cmd',help='Command to be summited', required=True)
	args = parser.parse_args()
	send_command(server, port, args.cmd)
   
#*****************************************************
#		MAIN 
#*****************************************************
if __name__ == "__main__":
    main ()
