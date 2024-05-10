import google.generativeai as genai

from src.config.model import model_name, generation_config, safety_settings
from src.config.const import api_key

genai.configure(api_key=api_key)

def analyse_search_results(search_results, prompt):
    context_text = '\n\nBaseado neste arquivo html com resultados de busca, '
    model = genai.GenerativeModel(model_name=model_name,
                              generation_config=generation_config,
                              safety_settings=safety_settings)
    convo = model.start_chat()
    full_prompt = search_results + context_text + prompt
    convo.send_message(full_prompt)
    return convo.last.text
