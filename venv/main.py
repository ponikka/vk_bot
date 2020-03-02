import vk_api
import requests
from vk_api.bot_longpoll import VkBotEventType, VkBotLongPoll

vk_session = vk_api.VkApi(token='2de7829484de82515fcffc6d3cfec6f34a912a910df204976a48eaacd25d2d7b29d101abc78e09a1975de')
vk = vk_session.get_api()
longpoll = VkBotLongPoll(vk_session, '192569675')
for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW:
        if event.obj.text != '':
            if event.from_user:
                vk.messages.send(
                    user_id=event.obj.from_id,
                    random_id=get_random_id(),
                    message=event.obj.text)