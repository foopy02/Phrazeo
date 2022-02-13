import json
import time
import requests
from bs4 import BeautifulSoup


database = json.load(open("C:/Users/Адиль/Desktop/AITU/russian/russian/database.json",encoding='utf8'))
counter = 0
for idiom in database:
    idiom['text'] = idiom['text'].lower().replace(',',' ').replace('.',' ')
    database[counter] = idiom
    counter =+ 1

json.dump(database,open("C:/Users/Адиль/Desktop/AITU/russian/russian/database.json",'w',encoding='utf-8'), indent=2, ensure_ascii=False)

class Idiom:
    def __init__(self, text, description=None, origin=None):
        self.text = text
        self.description = description
        self.origin = origin
        
def main():
    content = requests.get("https://moiposlovicy.ru/frazeologizmy/").content
    soup = BeautifulSoup(content, 'html.parser')
    idioms = soup.find_all('li',{"class":'col-md-4 col-sm-6'})
    counter_of_bags = 0
    print('main')
    for idiom in idioms:
        description, origin = None, None
        try:
            text = idiom.text
        except AttributeError:
            
            print("No explanation")
            continue
        try:
            soup_of_detail_info = BeautifulSoup(requests.get("https://moiposlovicy.ru"+idiom.find('a').get('href')).content, 'html.parser')
            whole_desc_origin = soup_of_detail_info.find_all('dd')
            text = whole_desc_origin[0].text
            description = whole_desc_origin[1].text
            origin = whole_desc_origin[2].text
            idiom_obj = Idiom(text, description, origin)
        except Exception as e:
            idiom_obj = Idiom(text=text)
            print("No explanation")
            pass
        database.append(idiom_obj.__dict__)
        counter_of_bags += 1
        print(counter_of_bags)
        json.dump(database,open("C:/Users/Адиль/Desktop/AITU/russian/russian/database.json",'w',encoding='utf-8'), indent=2, ensure_ascii=False)
        time.sleep(0.2)
    
            
    print(counter_of_bags)
    

if __name__ == "__main__":
    main()