import pyfiglet 
import sys 
import socket 
from datetime import datetime 

ascii_banner = pyfiglet.figlet_format("PORT SCANNER") 
print(ascii_banner) 

# Definição de alvo
if len(sys.argv) == 2: 
	
	
	target = socket.gethostbyname(sys.argv[1]) 
else: 
	print("Invalid ammount of Argument") 

#Banner 
print("-" * 50) 
print("Escaneando Alvo: " + target) 
print("Scan inicializado:" + str(datetime.now())) 
print("-" * 50) 

try: 
	
	# range de portas
	for port in range(3301,3309): 
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
		socket.setdefaulttimeout(1) 
		
		# caso de erro retorna 
		result = s.connect_ex((target,port)) 
		if result ==0: 
			print("Port {} esta aberta!".format(port)) 
		s.close() 
		
except KeyboardInterrupt: 
		print("\n Saindo Do  Programa !!!!") 
		sys.exit() 
except socket.gaierror: 
		print("\n Nome ou ip do Servidor não pode ser econtrado !!!!") 
		sys.exit() 
except socket.error: 
		print(" Servidor não está respondendo!!!!") 
		sys.exit() 
