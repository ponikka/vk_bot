import vk_api
import requests
from vk_api.bot_longpoll import VkBotEventType, VkBotLongPoll
from vk_api.utils import get_random_id
from parcer import weather, search_wiki



token = 'd7842cff18e3952270798bd8b35995b66ab08ed0b164c5ba0bbfb2e5f4845f87bdeec39d5519ac3815e22'
group_id = '192612501'
vk_session = vk_api.VkApi(token=token)
vk = vk_session.get_api()
longpoll = VkBotLongPoll(vk_session, group_id=group_id)
flag_from_wiki = False

for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW:
        if event.obj.text == 'Начать':
            if event.from_user:
                vk.messages.send(
                    user_id=event.obj.from_id,
                    random_id=get_random_id(),
                    message='Салам',)

        if event.obj.text == 'Погода':
            if event.from_user:
                vk.messages.send(
                    user_id=event.obj.from_id,
                    random_id=get_random_id(),
                    message=weather(),)

        if event.obj.text == 'Запрос':
            if event.from_user:
                vk.messages.send(
                    user_id=event.obj.from_id,
                    random_id=get_random_id(),
                    message="Что будем искать?",)
                flag_from_wiki = True

        if event.obj.text != 'Запрос' and flag_from_wiki == True:
            if event.from_user:
                flag_from_wiki = False
                vk.messages.send(
                    user_id = event.obj.from_id,
                    random_id = get_random_id(),
                    message = search_wiki(event.obj.text),
                    )