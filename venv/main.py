import vk_api
import requests
from vk_api.bot_longpoll import VkBotEventType, VkBotLongPoll
from vk_api.utils import get_random_id

vk_session = vk_api.VkApi(token='d7842cff18e3952270798bd8b35995b66ab08ed0b164c5ba0bbfb2e5f4845f87bdeec39d5519ac3815e22')
vk = vk_session.get_api()
longpoll = VkBotLongPoll(vk_session, '192612501')

for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW:
        if event.obj.text == 'Начать':
            if event.from_user:
                vk.messages.send(
                    user_id = event.user_id,
                    random_id = get_random_id(),
                    message = 'Salam'
                )