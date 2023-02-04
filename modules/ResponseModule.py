import va
import numpy as np
from load_talk_db import Data as DB

def parse_command(context):
    # print("RESPONSE MODULE >>>", "Contexto >>>>:", context)
    if context == 'aprendizado':
        start_learn_list = DB().get_response(context)
        for index, sentence in enumerate(start_learn_list):
            start_learn_list[index] = sentence[0]
        
        start_learn_resp0 = np.random.choice(start_learn_list)
        va.speak(start_learn_resp0)
        va.speak("Vamos começar com o que você vai me dizer?")
        new_command = va.listen_for_resp()
        va.speak("Agora, pode me dizer o contexto?")
        new_context = va.listen_for_resp()
        va.speak("Por último, qual será uma das minhas novas respostas?")
        new_anwser = va.listen_for_resp()

        check_learn = DB().finish_basic_learn(new_command, new_context, new_anwser)

        if len(check_learn) > 1:
            va.speak(check_learn)
            parse_command("aprendizado")
            return None
        
        else:
            confirmation = DB().get_response('confirmação')
            for index, conf in enumerate(confirmation):
                confirmation[index] = conf[0]

            final_conf = np.random.choice(confirmation)
            va.speak(final_conf)
            return None

    else:
        responses = DB().get_response(context)
        for index, anwser in enumerate(responses):
            responses[index] = anwser[0]

        final_response = np.random.choice(responses)
        # print("RESPONSES >>>", responses)
        # print("SELECTED RESPONSE >>>>", final_response)
    return va.speak(final_response)

