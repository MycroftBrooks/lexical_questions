import requests
import bs4

def cambridge_parser(word_input, dictionary_definition, dictionary_examples):
    url = "https://dictionary.cambridge.org/dictionary/english-russian/"
    url = url + word_input
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0"}
    r = requests.get(url, headers=headers)
    soup = bs4.BeautifulSoup(r.text, "html.parser")
    try:
        definition = soup.find("div", class_="def ddef_d db").text
        data = {"definition": definition}
        dictionary_definition.append(data)
        print('its ok')
    except AttributeError as err:
        print("No definition found")
    try:
        all_examples = soup.find('div', class_="dataset dd pr lmb-20").findAll('span', class_="deg") 
        for el in all_examples:
            data_examples = {"dictionary_examples": el.text}
            dictionary_examples.append(data_examples)
    except AttributeError as err:
        print("No example found")
    