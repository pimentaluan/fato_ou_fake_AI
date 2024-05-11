import google.generativeai as genai

genai.configure(api_key="SUA_API_KEY")

# Set up the model
generation_config = {
  "temperature": 0.5,
  "top_p": 0.95,
  "top_k": 0,
  "max_output_tokens": 8192,
}


safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

system_instruction = "Você trabalha em um grande portal e é responsável por analisar possíveis Fake News nas notícias com o máximo de precisão, analisando todos os pontos. Não leve em consideração a data para a avaliação. Sempre apresente os diferentes pontos de vista, indicando a possibilidade de ser Fake News ou não. No final, emita seu parecer e as chances de ser falso, destacando que existem possibilidades de erros. Recomenda-se verificar outras fontes para confirmar a veracidade da informação. "


model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                              generation_config=generation_config,
                              system_instruction=system_instruction,
                              safety_settings=safety_settings)

convo = model.start_chat(history=[
])

