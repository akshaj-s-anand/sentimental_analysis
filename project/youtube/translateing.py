import pandas as pd
import requests

API_KEY = 'your_api_key_here'

def translate_cell(cell, lang):
    url = f'https://translate.yandex.net/api/v1.5/tr.json/translate?key={API_KEY}&text={cell}&lang={lang}-en'
    response = requests.get(url)
    translation = response.json()['text'][0]
    return translation

# Read in the CSV file
df = pd.read_csv('comments.csv')

# Choose the source language and create a language code (e.g., 'es' for Spanish)
source_lang = 'fr'
lang_code = f'{source_lang}-en'

# Apply the translation function to each cell in the DataFrame
df = df.applymap(lambda x: translate_cell(x, lang_code))

# Overwrite the original CSV file with the translated DataFrame
df.to_csv('comments.csv', index=False)
