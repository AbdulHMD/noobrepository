import vk_api
import time
from time import gmtime, strftime

token = "efb4ce312e0f49ec526bf607cc40d0181cbb758816e0e6c6315ea16b1d7f9f9d04c046ebd9e7f20bdba4b" # можно получить на vkhost.github.io

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
