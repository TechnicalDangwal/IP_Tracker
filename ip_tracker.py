import requests
import json
import os
os.system("clear")
print('''\033[1;36;40m___         _____               _
|_ _|_ __   |_   _| __ __ _  ___| | _____ _ __
 | || '_ \    | || '__/ _` |/ __| |/ / _ \ '__|
 | || |_) |   | || | | (_| | (__|   <  __/ |
|___| .__/    |_||_|  \__,_|\___|_|\_\___|_|
    |_|\033[0m

		\033[1;34;40mcreated by\033[0m\033[1;33;40m Technical Dangwal\033[0m
''')
while True:
	user=input("\033[1;33;40mENTER TARGET IP : \033[0m \033[32;40m")
	r=requests.get("http://ip-api.com/json/"+user)
	j=json.loads(r.text)
	for i in j:
		print(f"\033[1;33;40m {i} : \033[0m \033[32;40m{j[i]}\033[0m ")
	break
