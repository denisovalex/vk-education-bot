import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

from config import GROUP_TOKEN, GROUP_ID
from bot.faq_data import faq_data
from bot.handlers import handle_message

def run_bot():
    vk_session = vk_api.VkApi(token=GROUP_TOKEN)
    longpoll = VkBotLongPoll(vk_session, GROUP_ID)
    vk = vk_session.get_api()

    for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            handle_message(vk, event, faq_data)