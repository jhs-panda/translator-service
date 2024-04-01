from vertexai.language_models import ChatModel, InputOutputTextPair

chat_model = ChatModel.from_pretrained("chat-bison@001")
context = "Translate this following non-English text into English:\n" # TODO: Insert context

def get_translation(post: str) -> str:
    # ----------------- DO NOT MODIFY ------------------ #

    parameters = {
        "temperature": 0.7,  # Temperature controls the degree of randomness in token selection.
        "max_output_tokens": 256,  # Token limit determines the maximum amount of text output.
    }

     # ---------------- YOUR CODE HERE ---------------- #
    context = "Translate this following non-English text into English:\n"
    chat = chat_model.start_chat(context=context)
    response = chat.send_message(post, **parameters)
    return response.text

def get_language(post: str) -> str:
    # ----------------- DO NOT MODIFY ------------------ #

    parameters = {
        "temperature": 0.7,  # Temperature controls the degree of randomness in token selection.
        "max_output_tokens": 256,  # Token limit determines the maximum amount of text output.
    }

     # ---------------- YOUR CODE HERE ---------------- #
    context = "Return the language of this text:\n"
    chat = chat_model.start_chat(context=context)
    response = chat.send_message(post, **parameters)
    return response.text

def translate_content(content: str) -> tuple[bool, str]:
    if(content == ""):
        return (True, content)

    translation = get_translation(content)
    language = get_language(content)
    list = language.split()

    if (("can't" in translation and "translate" in translation) or (len(list) > 2)):
        return (True, content)

    is_en = False
    if 'english' in language.lower():
        is_en = True
    return (is_en, translation)