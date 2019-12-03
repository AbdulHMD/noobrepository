import vk_api
import time
from time import gmtime, strftime

token = "09c668c3c6f6a709851d71db122d9246260955274561f85bc1ffcbdb02bb1612c2d9901066315681738ea" # можно получить на vkhost.github.io

vk_session = vk_api.VkApi(token=token)
vk = vk_session.get_api()

user = vk.users.get()
name = user[0]["first_name"]
lastname = user[0]["last_name"]

while True:
	try:
		print(strftime("%H:%M") + f" - Установлен статус Online для пользователя {name} {lastname}.")
		vk.account.setOnline()
		time.sleep(300)

	except Exception as e:
		print(e)
