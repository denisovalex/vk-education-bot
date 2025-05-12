import re

def handle_message(vk, event, faq_data):
    message = event.object['message']
    from_id = message['from_id']
    text = message['text'].lower()

    for entry in faq_data:
        if re.search(entry["pattern"], text):
            response_text = entry["response"]
            break
    else:
        response_text = "Извините, я не понял ваш вопрос. Попробуйте сформулировать иначе."

    vk.messages.send(
        user_id=from_id,
        message=response_text,
        random_id=0
    )