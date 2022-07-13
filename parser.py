import requests
from bs4 import BeautifulSoup


def parsing(path):
    alph_animal_dict = {}
    with open(path, 'r', encoding='utf-8') as file:
        for line in file:
            link = line.strip()[1:-1]
            try:
                inquiry = requests.get(link)
                soup_first_page = BeautifulSoup(inquiry.text, 'html.parser')
                dataset = soup_first_page.find_all('li')
                for el in dataset:
                    if 'class' not in str(el) and 'span' not in str(el) and 'id' not in str(el) \
                            and 'Категория' not in str(el):
                        title = str(el)[str(el).find('title="') + 7: str(el).find('">')]
                        sign = title[0]
                        if sign != 'A' and sign != 'H':
                            if sign not in alph_animal_dict:
                                alph_animal_dict[sign] = 1
                            else:
                                alph_animal_dict[sign] += 1
            except:
                print(link)
                continue
    return alph_animal_dict


d = parsing('data.txt')
for key in sorted(d.keys()):
    print(f'{key}: {d[key]}')
