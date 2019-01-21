import vk_api
import time
from time import gmtime, strftime

token = "e90fb8b41b5f68f19755d9991549ff81b7f29e31b2ecdb844c68b82f4bb94c836bbc4a5e11e2c1b0c99f3" # можно получить на vkhost.github.io

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