import vk_api
import requests
from vk_api.bot_longpoll import VkBotEventType, VkBotLongPoll
from vk_api.utils import get_random_id

vk_session = vk_api.VkApi(token='token')
vk = vk_session.get_api()
longpoll = VkBotLongPoll(vk_session, group_id='id')

for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW:
        if event.obj.text != '':
            if event.from_user:
                vk.messages.send(
                    user_id=event.obj.from_id,
                    random_id=get_random_id(),
                    message=event.obj.text)