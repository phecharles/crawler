import requests
import re
from bs4 import BeautifulSoup

DOMINIO = "https://django-anuncios.solyd.com.br"
URL_AUTOMOVEIS = "https://django-anuncios.solyd.com.br/automoveis/"

def requisicao(url):
    try:
        resposta = requests.get(url)
        if resposta.status_code == 200:
            return resposta.text
        else:
            print("Erro ao fazer requisição")
    except Exception as error:
        print("Erro ao fazer requisição")
        print(error)

def parsing(resposta):
    try:
        soup = BeautifulSoup(resposta, 'html.parser')
        return soup
    except Exception as error:
        print("Erro ao fazer o parsing HTML")
        print(error)


def encontrar_links(soup):
    try:
        cards_pai = soup.find("div", class_="ui three doubling link cards")
        cards = cards_pai.find_all("a")
    except:
        print("Erro ao encontrar links")
        return None

    links = []
    for card in cards:
        try:
            link = card["href"]
            links.append(link)
        except:
            pass

    return links

def encontrar_telefone(soup):
    try:
        descricao = soup.find_all("div", class_="sixteen wide column")[2].p.get_text().strip()
    except:
        print("Erro ao encontrar descrição")
        return None

    regex = re.findall(r"\(?0?([1-9]{2})[ \-\.\)]{0,2}(9[ \-\.]?\d{4})[ \-\.]?(\d{4})", descricao)
    if regex:
        return regex

resposta = requisicao(URL_AUTOMOVEIS)
if resposta:
    soup_busca = parsing(resposta)
    if soup_busca:
        links = encontrar_links(soup_busca)
        i=0
        for link in links:
            i = i + 1
            resposta_anuncio = requisicao(DOMINIO + link)
            if resposta_anuncio:
                soup_anuncio = parsing(resposta_anuncio)
                if soup_anuncio:
                    print("{}º Anúncio: {}".format(i, encontrar_telefone(soup_anuncio)))

