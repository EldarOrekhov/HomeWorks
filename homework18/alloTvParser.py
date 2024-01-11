import requests
import lxml
from bs4 import BeautifulSoup
import json

def get_data(url, params):
    response = requests.get(url=url, params=params)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "lxml")
        all_elems = soup.find_all("div", class_="product-card")
        data_list = []
        for elem in all_elems:
            title = elem.find('a', class_="product-card__title").text
            try:
                old_price = elem.find("div", class_="v-pb__old").text
                cur_price = elem.find("div", class_="v-pb__cur").text
                data_list.append({
                    "title": title,
                    "old_price": old_price,
                    "cur_price": cur_price
                })
            except:
                continue
        return data_list


print("Processing...")
params = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}
data = []
i = 1
while True:
    url = f"https://allo.ua/televizory/p-{i}"
    func_res = get_data(url, params)
    if not len(func_res):
        break
    data.extend(func_res)
    i += 1

output_file_path = 'data.json'
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    json.dump(data, output_file, indent=2, ensure_ascii=False)

print(f'Data saved to file: {output_file_path}')
