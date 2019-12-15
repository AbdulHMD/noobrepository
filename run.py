import vk_api
from vk_api.bot_longpoll import VkBotEventType, VkBotLongPoll
import json
import time

vk = vk_api.VkApi(token='5ffd8755d510036751d5b04dda9392039a488fa48b18f6170c6de394e87b10f26a98a1025bdf266f6fd6b')

vk._auth_token()

vk.get_api()

keyboard = {
    "one_time": True,
    "buttons": [
        [{
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"1\"}",
                    "label": "Ужасно"
                },
                "color": "negative"
            },
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"2\"}",
                    "label": "Плохо"
                },
                "color": "primary"
            },
            ],
            [
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"2\"}",
                    "label": "Нормально"
                },
                "color": "secondary"
            },
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"2\"}",
                    "label": "Хорошо"
                },
                "color": "positive"
            }
            ]
        ]
    
}

keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
keyboard = str(keyboard.decode('utf-8'))

longpoll = VkBotLongPoll(vk, 159365993)

while True:
    for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            if event.object.text.lower():
                vk.method("messages.send", {"peer_id": event.object.peer_id, "message": "Как ты?", "random_id": 0,
                                            "keyboard": keyboard})
                time.sleep(18000)
                #Каждые 5 часов