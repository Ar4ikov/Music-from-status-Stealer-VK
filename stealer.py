	
#####################################################################
#####################################################################
##                                                                 ##
##						Когфигурация скрипта					   ##
##                                                                 ##		

access_token = "токен"

## Элемент выше - ваш ключ доступа к API Вконтакте (ОБЯЗАТЕЛЬНО)   ##
## Не печальтесь, если его у вас нет, а просто включите скрипт без ##
## него, вам будет выдана инструкция по его получению              ##		

your_id = 1

## ID пользователя, которому надо прислать сообщение о смене       ##
## (советую использовать ваш ID, ОБЯЗАТЕЛЬНА)                      ##
##                                                                 ##

check_updates = True

## Функция для проверки обновлений у данного скрипта               ##
## (НЕ ОБЯЗАТЕЛЬНА)                                                ##
##                                                                 ##
#####################################################################
#####################################################################



































############  /  ПРОШУ, НЕ ТРОГАЙТЕ, ЕСЛИ ВЫ НЕ ОПЫТНЫЙ ПОЛЬЗОВАТЕЛЬ  /  ###############

import vk
from time import sleep
import requests

kek = requests.get("https://api.vk.com/method/status.get?user_id="+str(your_id)+"&access_token="+str(access_token))
kek = kek.text
kek = eval(kek)
if kek.get("error"):
	kek_error_num = kek["error"]["error_code"]
	if kek_error_num == 5:
		print(" ")
		print(" ")
		print(" ")
		print(" ")
		print(" ")
		print(" ")
		print(" ")
		print(" ")
		print("##########################################")
		print("#                                        #")
		print("#      Нет ACCESS_TOKEN'а? НЕ БЕДА!      #")
		print("# Ниже написана ссылка, по которой тебе  #")
		print("# надо перейти, после чего, принять все  #")
		print("# условия, и из ссылки выбрать часть,    #")
		print("# которая начинается с \"access_token=\"   #")
		print("# Затем вставь в скрипт в нужном месте!  #")
		print("#                                        #")
		print("#                  ???                   #")
		print("#                PROFIT!                 #")
		print("#                                        #")
		print("#                                        #")
		print("#                                        #")
		print("#----------------------------------------#")
		print("#                                        #")
		print("#           vk.cc/что_то_будет           #")
		print("#                                        #")
		print("##########################################")
		print(" ")
		print(" ")
		print(" ")
		print(" ")
		print(" ")
		print(" ")
		print(" ")
		print(" ")
		exit()

session = vk.Session()
api = vk.API(session, access_token=access_token, v='5.62', lang='ru')

################
# FIRST STATUS #
################
print("Введите ID юзера ВК")
while True:
	user = input(" » ")
	try:
		user = int(user)
		break
	except:
		print("Введи мне ID юзера, а не твоё мыло ебаное!")
user_test = requests.get("https://api.vk.com/method/status.get?user_id="+str(user)+"&access_token="+str(access_token))
user_test = user_test.text
user_test = eval(user_test)
if user_test.get("error"):
	user_error_num = user_test["error"]["error_code"]
	if user_error_num == 15 or user_error_num == 18:
		print(" ")
		print(" ")
		print(" ")
		print(" ")
		print(" ")
		print(" ")
		print(" ")
		print("##########################################")
		print("#                                        #")
		print("#                                        #")
		print("#      Такого пользователя нет, либо     #")
		print("#        он был забанен или удалён       #")
		print("#                                        #")
		print("#                                        #")
		print("##########################################")
		print(" ")
		print(" ")
		print(" ")
		print(" ")
		print(" ")
		print(" ")
		print(" ")
		exit()

print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print("##########################################")
print("#                                        #")
print("#                                        #")
print("#           СЛЕЖКА ЗА МУЗЫКОЙ            #")
print("#             для ВКОНТАКТЕ              #")
print("#          Автор: vk.com/ar4ikov         #")
print("#                                        #")
print("#                                        #")
print("##########################################")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")


status11 = api.status.get(user_id=user)
status1 = status11["text"]
user_fn11 = api.users.get(user_id=user)
user_fn = user_fn11[0]["first_name"]
user_ln = user_fn11[0]["last_name"]
print("Слежка за: "+str(user_fn)+" "+str(user_ln))
print("Текущий статус: \""+str(status1)+"\"")

while True:
	sleep(3)
	status_now1 = api.status.get(user_id=user)
	status_now = status_now1["text"]
	if status_now == status1:
		pass
	else:
		sleep(1)
		if status_now1.get("audio"):
			owner = status_now1["audio"]["owner_id"]
			mid = status_now1["audio"]["id"]
			api.messages.send(user_id=your_id, message="Статус пользователя vk.com/id"+str(user)+" ("+str(user_fn)+" "+str(user_ln)+") изменён!\r\n\r\nБыл: \""+str(status1)+"\"\r\nСтал: \""+str(status_now)+"\"", attachment="audio"+str(owner)+"_"+str(mid))
			print("У юзера vk.com/id"+str(user)+" ("+str(user_fn)+" "+str(user_ln)+") сменился статус на: \""+str(status_now)+"\" с музыкой в статусе!")
			status11 = api.status.get(user_id=user)
			status1 = status11["text"]
		else:
			api.messages.send(user_id=your_id, message="Статус пользователя vk.com/id"+str(user)+" ("+str(user_fn)+" "+str(user_ln)+") изменён!\r\n\r\nБыл: \""+str(status1)+"\"\r\nСтал: \""+str(status_now)+"\"")
			print("У юзера vk.com/id"+str(user)+" ("+str(user_fn)+" "+str(user_ln)+") сменился статус на: \""+str(status_now)+"\"")
			status11 = api.status.get(user_id=user)
			status1 = status11["text"]
