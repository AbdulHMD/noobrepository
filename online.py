import vk_api
import time
from time import gmtime, strftime

token = "620556ef73fdf5ea610cebb7af1a89ae1616656facc07b55ca388d63bbd03d5617b0fdab254cafdff3f5e" # можно получить на vkhost.github.io

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
