#!flask/bin/python
from flask import Flask, jsonify
import requests
import json
import subprocess
from datetime import date



ip=subprocess.check_output(['hostname','-I'])
ipfinal=ip.decode()

fecha=date.today()

nombrearchivo=str(ipfinal)+'_'+str(fecha)

if __name__ == "__main__":
	print("Hola")
	url='http://localhost:5000/apimeli/api/v1.0/'
	response=requests.get(url)
	print(response)
	if response.status_code==200:
		print(response.content)
	content=response.content
	file=open(nombrearchivo+'.json','wb')
	file.write(content)
	file.close()

