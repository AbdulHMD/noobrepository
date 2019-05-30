import vk_api
import time
from time import gmtime, strftime

token = "a498d887f797a852d9b7e2fcd928d0124d5c99a38a41e459bafc34793d37ca83712c5ba89783a187d0584" # можно получить на vkhost.github.io

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
