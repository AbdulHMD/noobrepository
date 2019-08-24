import vk_api
import time
from time import gmtime, strftime

token = "a80b07e102995f2bd20c2eed1e7ee45b1276b41847f53dc93c65de7d8cf4019be731884a9276a66705e11" # можно получить на vkhost.github.io

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
