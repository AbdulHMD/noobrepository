import vk_api
import time
from time import gmtime, strftime

token = "225ee1a955f3311b7ba2ffa10d2b9730be4252265d791c0c01d7cd06ef2254f643b9c347a27f45e35bcbe" # можно получить на vkhost.github.io

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
