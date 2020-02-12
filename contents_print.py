import sys

from khaiii import KhaiiiApi
import copy

def find_contents(contents_list,search_word):
    api = KhaiiiApi('./khaiii/khaiii/build/lib/libkhaiii.0.4.dylib', './khaiii/khaiii/build/share/khaiii')
    result = ""

    search_word_with_NLP = copy.deepcopy(search_word)

    for str_sword in search_word:
        for word in api.analyze(str_sword):
            for morph in word.morphs:
                if 'NN' in morph.tag:
                    search_word_with_NLP.append(morph.lex)



    search_word_with_NLP = tuple(search_word_with_NLP)

    for col in contents_list:
        title_line = col["title"].replace(' ','').split(',')
        if set(title_line) & set(search_word_with_NLP) != set():
            result += str(col["contents"])

    if result == "":
        return "Fail to Find"
    else:
        return result


def tuple_extract(argt):
    result = []
    for x_tuple in argt:
        if type(x_tuple) == type(""):
            result.append(x_tuple)  # 1st-dimension tuple
        else:
            for word in x_tuple: # 2nd-or high dimension tuple
                result.append(word)

    return result


'''
url = 'http://www.snuh.org/guide/convenience/internal/conveninList.do'
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome('./chrome/chromedriver_linux64/chromedriver', chrome_options=chrome_options)
driver.implicitly_wait(3)
driver.set_page_load_timeout(100)
driver.get(url)
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
parser = parsing.Tag_parser(soup)
'''
