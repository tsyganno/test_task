import requests
from bs4 import BeautifulSoup

alph_animal_dict = {}


def parsing(link):
    inquiry = requests.get(link)
    soup_first_page = BeautifulSoup(inquiry.text, 'html.parser')
    dataset = soup_first_page.find_all('li')
    for el in dataset:
        if '</a>' in str(el) and 'title' in str(el) and 'div' not in str(el) and 'class' not in str(el) and 'id' not in str(el) and str(el)[str(el).find('title="') + 7:].startswith('А'):
            sign = str(el)[str(el).find('title="') + 7: str(el).find('title="') + 8]
            if sign not in alph_animal_dict:
                alph_animal_dict[sign] = 1
            else:
                alph_animal_dict[sign] += 1
        elif '</a>' in str(el) and 'title' in str(el) and 'div' not in str(el) and 'class' not in str(el) and 'id' not in str(el) and str(el)[str(el).find('title="') + 7:].startswith('Б'):
            sign = str(el)[str(el).find('title="') + 7: str(el).find('title="') + 8]
            if sign not in alph_animal_dict:
                alph_animal_dict[sign] = 1
            else:
                alph_animal_dict[sign] += 1
        elif '</a>' in str(el) and 'title' in str(el) and 'div' not in str(el) and 'class' not in str(el) and 'id' not in str(el) and str(el)[str(el).find('title="') + 7:].startswith('В'):
            sign = str(el)[str(el).find('title="') + 7: str(el).find('title="') + 8]
            if sign not in alph_animal_dict:
                alph_animal_dict[sign] = 1
            else:
                alph_animal_dict[sign] += 1
        elif '</a>' in str(el) and 'title' in str(el) and 'div' not in str(el) and 'class' not in str(el) and 'id' not in str(el) and str(el)[str(el).find('title="') + 7:].startswith('Г'):
            sign = str(el)[str(el).find('title="') + 7: str(el).find('title="') + 8]
            if sign not in alph_animal_dict:
                alph_animal_dict[sign] = 1
            else:
                alph_animal_dict[sign] += 1
        elif '</a>' in str(el) and 'title' in str(el) and 'div' not in str(el) and 'class' not in str(el) and 'id' not in str(el) and str(el)[str(el).find('title="') + 7:].startswith('Д'):
            sign = str(el)[str(el).find('title="') + 7: str(el).find('title="') + 8]
            if sign not in alph_animal_dict:
                alph_animal_dict[sign] = 1
            else:
                alph_animal_dict[sign] += 1
        elif '</a>' in str(el) and 'title' in str(el) and 'div' not in str(el) and 'class' not in str(el) and 'id' not in str(el) and str(el)[str(el).find('title="') + 7:].startswith('Е'):
            sign = str(el)[str(el).find('title="') + 7: str(el).find('title="') + 8]
            if sign not in alph_animal_dict:
                alph_animal_dict[sign] = 1
            else:
                alph_animal_dict[sign] += 1
        elif '</a>' in str(el) and 'title' in str(el) and 'div' not in str(el) and 'class' not in str(el) and 'id' not in str(el) and str(el)[str(el).find('title="') + 7:].startswith('Ж'):
            sign = str(el)[str(el).find('title="') + 7: str(el).find('title="') + 8]
            if sign not in alph_animal_dict:
                alph_animal_dict[sign] = 1
            else:
                alph_animal_dict[sign] += 1
        elif '</a>' in str(el) and 'title' in str(el) and 'div' not in str(el) and 'class' not in str(el) and 'id' not in str(el) and str(el)[str(el).find('title="') + 7:].startswith('З'):
            sign = str(el)[str(el).find('title="') + 7: str(el).find('title="') + 8]
            if sign not in alph_animal_dict:
                alph_animal_dict[sign] = 1
            else:
                alph_animal_dict[sign] += 1
        elif '</a>' in str(el) and 'title' in str(el) and 'div' not in str(el) and 'class' not in str(el) and 'id' not in str(el) and str(el)[str(el).find('title="') + 7:].startswith('И'):
            sign = str(el)[str(el).find('title="') + 7: str(el).find('title="') + 8]
            if sign not in alph_animal_dict:
                alph_animal_dict[sign] = 1
            else:
                alph_animal_dict[sign] += 1
        elif '</a>' in str(el) and 'title' in str(el) and 'div' not in str(el) and 'class' not in str(el) and 'id' not in str(el) and str(el)[str(el).find('title="') + 7:].startswith('К'):
            sign = str(el)[str(el).find('title="') + 7: str(el).find('title="') + 8]
            if sign not in alph_animal_dict:
                alph_animal_dict[sign] = 1
            else:
                alph_animal_dict[sign] += 1
        elif '</a>' in str(el) and 'title' in str(el) and 'div' not in str(el) and 'class' not in str(el) and 'id' not in str(el) and str(el)[str(el).find('title="') + 7:].startswith('Л'):
            sign = str(el)[str(el).find('title="') + 7: str(el).find('title="') + 8]
            if sign not in alph_animal_dict:
                alph_animal_dict[sign] = 1
            else:
                alph_animal_dict[sign] += 1
    return alph_animal_dict


parsing('https://inlnk.ru/jElywR')
parsing('https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&pagefrom=%D0%90%D0%B7%D0%B8%D0%B0%D1%82%D1%81%D0%BA%D0%B8%D0%B9+%D0%BC%D1%83%D1%80%D0%B0%D0%B2%D0%B5%D0%B9-%D0%BF%D0%BE%D1%80%D1%82%D0%BD%D0%BE%D0%B9&subcatfrom=%D0%90&filefrom=%D0%90#mw-pages')
parsing('https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&pagefrom=%D0%90%D0%BC%D0%B5%D1%80%D0%B8%D0%BA%D0%B0%D0%BD%D1%81%D0%BA%D0%B0%D1%8F+%D0%B5%D0%B2%D0%B4%D0%BE%D1%88%D0%BA%D0%B0&subcatfrom=%D0%90&filefrom=%D0%90#mw-pages')
parsing('https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&pagefrom=%D0%90%D0%BD%D0%B4%D1%81%D0%BA%D0%B0%D1%8F+%D1%87%D0%B0%D0%B9%D0%BA%D0%B0&subcatfrom=%D0%90&filefrom=%D0%90#mw-pages')
print(parsing('https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&pagefrom=%D0%90%D1%80%D0%B3%D0%B0%D1%81%D0%BE%D0%B2%D1%8B%D0%B5+%D0%BA%D0%BB%D0%B5%D1%89%D0%B8&subcatfrom=%D0%90&filefrom=%D0%90#mw-pages'))
parsing('https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&pagefrom=%D0%90%D1%84%D0%B3%D0%B0%D0%BD%D1%81%D0%BA%D0%B0%D1%8F+%D0%BB%D0%B8%D1%81%D0%B8%D1%86%D0%B0&subcatfrom=%D0%90&filefrom=%D0%90#mw-pages')
parsing('https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&pagefrom=%D0%91%D0%B0%D0%BB%D0%B8%D1%82%D0%BE%D1%80%D0%BE%D0%B2%D1%8B%D0%B5&subcatfrom=%D0%90&filefrom=%D0%90#mw-pages')
parsing('https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&pagefrom=%D0%91%D0%B5%D0%BB%D0%B0%D1%8F+%D1%81%D1%83%D0%BB%D1%82%D0%B0%D0%BD%D0%BA%D0%B0&subcatfrom=%D0%90&filefrom=%D0%90#mw-pages')
print(parsing('https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&pagefrom=%D0%91%D0%B5%D0%BB%D0%BE%D0%BB%D0%BE%D0%B1%D1%8B%D0%B9+%D0%B0%D0%BC%D0%B0%D0%B7%D0%BE%D0%BD&subcatfrom=%D0%90&filefrom=%D0%90#mw-pages'))
parsing('https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&pagefrom=%D0%91%D0%B5%D0%BD%D0%B3%D0%B0%D0%BB%D1%8C%D1%81%D0%BA%D0%B8%D0%B9+%D0%B3%D1%80%D0%B8%D1%84&subcatfrom=%D0%90&filefrom=%D0%90#mw-pages')
parsing('https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&pagefrom=%D0%91%D0%BE%D0%B3%D0%B0%D1%87%D0%BA%D0%B8&subcatfrom=%D0%90&filefrom=%D0%90#mw-pages')
parsing('https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&pagefrom=%D0%91%D0%BE%D0%BB%D1%8C%D1%88%D0%BE%D0%B9+%D0%BA%D0%BE%D0%BD%D1%91%D0%BA&subcatfrom=%D0%90&filefrom=%D0%90#mw-pages')
parsing('https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&pagefrom=%D0%91%D1%80%D0%B0%D0%B7%D0%B8%D0%BB%D1%8C%D1%81%D0%BA%D0%B0%D1%8F+%D1%81%D0%B2%D0%B5%D1%82%D1%8F%D1%89%D0%B0%D1%8F%D1%81%D1%8F+%D0%B0%D0%BA%D1%83%D0%BB%D0%B0&subcatfrom=%D0%90&filefrom=%D0%90#mw-pages')
print(parsing('https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&pagefrom=%D0%91%D1%83%D1%80%D0%BE%D0%B3%D1%80%D1%83%D0%B4%D1%8B%D0%B5+%D0%BC%D1%83%D1%85%D0%BE%D0%B5%D0%B4%D1%8B&subcatfrom=%D0%90&filefrom=%D0%90#mw-pages'))
parsing('https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&pagefrom=%D0%92%D0%B5%D0%B5%D1%80%D0%BE%D1%85%D0%B2%D0%BE%D1%81%D1%82%D0%BA%D0%B0-%D0%B2%D0%B4%D0%BE%D0%B2%D1%83%D1%88%D0%BA%D0%B0&subcatfrom=%D0%90&filefrom=%D0%90#mw-pages')
parsing('https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&pagefrom=%D0%92%D0%BE%D0%B4%D1%8F%D0%BD%D0%B0%D1%8F+%D1%86%D0%B8%D0%B2%D0%B5%D1%82%D1%82%D0%B0&subcatfrom=%D0%90&filefrom=%D0%90#mw-pages')
parsing('https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&subcatfrom=%D0%90&filefrom=%D0%90&pagefrom=%D0%92%D0%BE%D1%81%D1%8C%D0%BC%D0%B8%D1%80%D1%83%D0%BA%D0%B8%D0%B5#mw-pages')
print(parsing('https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&subcatfrom=%D0%90&filefrom=%D0%90&pagefrom=%D0%93%D0%B0%D1%81%D1%82%D0%BE%D0%BD%D0%B8%D1%8F+%28%D0%B4%D0%B8%D0%BD%D0%BE%D0%B7%D0%B0%D0%B2%D1%80%29#mw-pages'))
parsing('https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&subcatfrom=%D0%90&filefrom=%D0%90&pagefrom=%D0%93%D0%B8%D0%BC%D0%B0%D0%BB%D0%B0%D0%B9%D1%81%D0%BA%D0%B0%D1%8F+%D1%86%D0%B8%D0%B2%D0%B5%D1%82%D0%B0#mw-pages')
parsing('https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&subcatfrom=%D0%90&filefrom=%D0%90&pagefrom=%D0%93%D0%BE%D0%BB%D0%BE%D1%82%D0%B5%D1%80%D0%B8%D0%B8#mw-pages')
parsing('https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&subcatfrom=%D0%90&filefrom=%D0%90&pagefrom=%D0%93%D0%BE%D1%80%D0%B8%D1%85%D0%B2%D0%BE%D1%81%D1%82%D0%BA%D0%B0-%D1%87%D0%B5%D1%80%D0%BD%D1%83%D1%88%D0%BA%D0%B0#mw-pages')
parsing('https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&subcatfrom=%D0%90&filefrom=%D0%90&pagefrom=%D0%93%D1%83%D0%B0%D0%BC%D1%81%D0%BA%D0%B8%D0%B9+%D0%B2%D0%BE%D1%80%D0%BE%D0%BD#mw-pages')
print(parsing('https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&subcatfrom=%D0%90&filefrom=%D0%90&pagefrom=%D0%94%D0%B5%D0%B9%D0%BD%D0%BE%D0%BD%D0%B8%D1%85#mw-pages'))
parsing('https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&subcatfrom=%D0%90&filefrom=%D0%90&pagefrom=%D0%94%D0%BB%D0%B8%D0%BD%D0%BD%D0%BE%D0%BA%D1%80%D1%8B%D0%BB%D1%8B%D0%B9+%D0%BF%D0%BE%D0%BF%D1%83%D0%B3%D0%B0%D0%B9+%D0%A0%D1%8E%D0%BF%D0%BF%D0%B5%D0%BB%D1%8F#mw-pages')
parsing('https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&subcatfrom=%D0%90&filefrom=%D0%90&pagefrom=%D0%94%D0%BE%D0%BC%D0%B8%D0%BD%D0%B8%D0%BA%D0%B0%D0%BD%D1%81%D0%BA%D0%B0%D1%8F+%D0%BA%D0%B2%D0%B0%D0%BA%D1%88%D0%B0#mw-pages')
parsing('https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&subcatfrom=%D0%90&filefrom=%D0%90&pagefrom=%D0%95%D0%B2%D1%80%D0%BE%D0%BF%D0%B5%D0%B9%D1%81%D0%BA%D0%B0%D1%8F+%D0%BC%D0%BE%D0%B1%D1%83%D0%BB%D0%B0#mw-pages')
parsing('https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&subcatfrom=%D0%90&filefrom=%D0%90&pagefrom=%D0%96%D0%B5%D0%BB%D1%82%D0%BE%D0%B3%D0%BE%D1%80%D0%BB%D1%8B%D0%B9+%D0%BB%D0%B5%D1%81%D0%BD%D0%BE%D0%B9+%D0%BF%D0%B5%D0%B2%D1%83%D0%BD#mw-pages')
parsing('https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&subcatfrom=%D0%90&filefrom=%D0%90&pagefrom=%D0%96%D1%83%D0%B6%D0%B5%D0%BB%D0%B8%D1%86%D0%B0+%D0%B2%D0%BE%D1%81%D1%85%D0%B8%D1%82%D0%B8%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%B0%D1%8F#mw-pages')
parsing('https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&subcatfrom=%D0%90&filefrom=%D0%90&pagefrom=%D0%97%D0%B0%D0%BF%D0%B0%D0%B4%D0%BD%D1%8B%D0%B9+%D1%87%D1%91%D1%80%D0%BD%D1%8B%D0%B9+%D0%BD%D0%BE%D1%81%D0%BE%D1%80%D0%BE%D0%B3#mw-pages')
parsing('https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&subcatfrom=%D0%90&filefrom=%D0%90&pagefrom=%D0%97%D0%B5%D0%BC%D0%BB%D1%8F%D0%BD%D1%8B%D0%B5+%D1%82%D0%BE%D0%BF%D0%B0%D0%BA%D0%BE%D0%BB%D0%BE#mw-pages')
parsing('https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&subcatfrom=%D0%90&filefrom=%D0%90&pagefrom=%D0%97%D0%BE%D0%BB%D0%BE%D1%82%D0%BE%D0%B3%D0%BE%D0%BB%D0%BE%D0%B2%D1%8B%D0%B9+%D0%BF%D0%B5%D0%B2%D1%87%D0%B8%D0%B9+%D1%81%D0%BE%D1%80%D0%BE%D0%BA%D0%BE%D0%BF%D1%83%D1%82#mw-pages')
parsing('https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&subcatfrom=%D0%90&filefrom=%D0%90&pagefrom=%D0%98%D0%BA%D0%B0%D1%80%D0%BE%D0%BD%D0%B8%D0%BA%D1%82%D0%B5%D1%80%D0%B8%D1%81#mw-pages')
parsing('https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&subcatfrom=%D0%90&filefrom=%D0%90&pagefrom=%D0%98%D1%81%D0%BF%D0%BE%D0%BB%D0%B8%D0%BD%D1%81%D0%BA%D0%B8%D0%B5+%D1%8F%D1%89%D0%B5%D1%80%D0%B8%D1%86%D1%8B#mw-pages')
parsing('https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&subcatfrom=%D0%90&filefrom=%D0%90&pagefrom=%D0%9A%D0%B0%D0%BC%D0%B1%D0%B0%D0%BB%D0%BE%D0%B2%D1%8B%D0%B5#mw-pages')
parsing('https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&subcatfrom=%D0%90&filefrom=%D0%90&pagefrom=%D0%9A%D0%B0%D1%80%D0%BB%D0%B8%D0%BA%D0%BE%D0%B2%D0%B0%D1%8F+%D0%BA%D0%BE%D0%BB%D1%8E%D1%87%D0%B0%D1%8F+%D0%B0%D0%BA%D1%83%D0%BB%D0%BA%D0%B0#mw-pages')
parsing('https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&subcatfrom=%D0%90&filefrom=%D0%90&pagefrom=%D0%9A%D0%B5%D0%B4%D1%80%D0%BE%D0%B2%D0%BA%D0%B0#mw-pages')
parsing('https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&subcatfrom=%D0%90&filefrom=%D0%90&pagefrom=%D0%9A%D0%BB%D0%BE%D0%BF-%D0%B7%D0%B5%D0%BC%D0%BB%D0%B5%D0%BA%D0%BE%D0%BF+%D0%B4%D0%B2%D1%83%D1%85%D1%86%D0%B2%D0%B5%D1%82%D0%BD%D1%8B%D0%B9#mw-pages')
parsing('https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&subcatfrom=%D0%90&filefrom=%D0%90&pagefrom=%D0%9A%D0%BE%D0%BB%D1%8E%D1%87%D0%B8%D0%B5+%D1%81%D0%BE%D0%BD%D0%B8#mw-pages')
parsing('https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&subcatfrom=%D0%90&filefrom=%D0%90&pagefrom=%D0%9A%D0%BE%D1%80%D0%BE%D0%BB%D0%B5%D0%B2%D1%81%D0%BA%D0%B8%D0%B9+%D0%BF%D0%BE%D0%BF%D1%83%D0%B3%D0%B0%D0%B9#mw-pages')
parsing('https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&subcatfrom=%D0%90&filefrom=%D0%90&pagefrom=%D0%9A%D0%BE%D1%88%D0%B0%D1%87%D0%B8%D0%B9+%D0%B3%D1%80%D1%83%D0%BF%D0%B5%D1%80#mw-pages')
parsing('https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&subcatfrom=%D0%90&filefrom=%D0%90&pagefrom=%D0%9A%D1%80%D0%B0%D1%81%D0%BD%D0%BE%D0%B3%D1%83%D0%B7%D1%8B%D0%B9+%D0%B0%D0%B7%D0%B8%D0%B0%D1%82%D1%81%D0%BA%D0%B8%D0%B9+%D1%82%D1%80%D0%BE%D0%B3%D0%BE%D0%BD#mw-pages')
parsing('https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&subcatfrom=%D0%90&filefrom=%D0%90&pagefrom=%D0%9A%D1%80%D0%B0%D1%81%D0%BD%D1%8B%D0%B9+%D0%BA%D0%B0%D1%80%D0%B4%D0%B8%D0%BD%D0%B0%D0%BB#mw-pages')
parsing('https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&subcatfrom=%D0%90&filefrom=%D0%90&pagefrom=%D0%9A%D1%80%D1%83%D0%BF%D0%BD%D1%8B%D0%B9+%D0%BF%D0%B0%D1%80%D0%BD%D0%BE%D0%BF%D0%B5%D1%81#mw-pages')
parsing('https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&subcatfrom=%D0%90&filefrom=%D0%90&pagefrom=%D0%9A%D1%83%D1%81%D1%82%D0%B0%D1%80%D0%BD%D0%B8%D0%BA%D0%BE%D0%B2%D1%8B%D0%B5+%D1%82%D0%BE%D0%BF%D0%B0%D0%BA%D0%BE%D0%BB%D0%BE#mw-pages')
print(parsing('https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&subcatfrom=%D0%90&filefrom=%D0%90&pagefrom=%D0%9B%D0%B5%D0%BD%D1%82%D0%BE%D1%87%D0%BD%D1%8B%D0%B9+%D0%BA%D1%80%D0%B0%D0%B9%D1%82#mw-pages'))
