import requests
from bs4 import BeautifulSoup
import re


def obter_conteudo_do_artigo(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Erro ao obter conteúdo do artigo: {e}")
        return None

    return response.content

def extrair_texto(content):
    soup = BeautifulSoup(content, 'html.parser')

    article_element = soup.find('main') or soup.find('article')
    
    if article_element:
        return article_element.get_text()
    else:
        print("Elemento principal do artigo não encontrado.")
        return None

def limpar_texto(text):
    text = re.sub(r'<[^>]*>', '', text)
    text = re.sub(r'<script.*?</script>', '', text)
    text = re.sub(r'<style.*?</style>', '', text)
    text = re.sub(r'<noscript.*?</noscript>', '', text)
    text = re.sub(r'<header.*?</header>', '', text)
    text = re.sub(r'<footer.*?</footer>', '', text)
    text = re.sub(r'<aside.*?</aside>', '', text)
    text = re.sub(r'<nav.*?</nav>', '', text)

    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)

    text = ' '.join(text.split())

    return text

def obter_conteudo_do_artigo_processado(url):
    content = obter_conteudo_do_artigo(url)
    if content:
        text = extrair_texto(content)
        if text:
            return limpar_texto(text)
        else:
            print("Falha ao extrair texto do artigo.")
    else:
        print("Falha ao obter conteúdo do artigo.")
    return None
