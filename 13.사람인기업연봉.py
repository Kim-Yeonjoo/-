import requests
from bs4 import BeautifulSoup

url = 'https://www.saramin.co.kr/zf_user/salaries/total-salary/list'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')
soup

#기업명
#salary_list > ul > li:nth-child(1) > div.company_info > strong > a
company_name = soup.find_all('a', class_='link_tit', title=True)
company_names = [tag.text for tag in company_name]

# for 기업명 in company_names:
#     print(기업명)


#평균값

#salary_list > ul > li:nth-child(1) > div.graph_info > span.wrap_graph.color01 > span > span > span
avg = soup.find_all('span', class_='txt_g txt_avg')
avg_values = [value.text for value in avg]

# for 평균 in avg:
#     평균값 = 평균.text
#     print(f'{평균값}만원')

#최저값

#salary_list > ul > li:nth-child(1) > div.graph_info > span.wrap_graph.color02 > span > span > span
min = soup.select('span.wrap_graph.color02 span.txt_g')
min_salary = [value.text for value in min]

# for 최저 in min:
#     최저값 = 최저.text
#     print(f'{최저값}만원')


#최고값
max = soup.select('span.wrap_graph.color03 span.txt_g')
max_salary = [value.text for value in max]

# for 최고 in max:
#     최고값 = 최고.text
#     print(f'{최고값}만원')


salary_list = []

for name, average, minimum, maximum in zip(company_names, avg_values, min_salary, max_salary):
    salary_list.append([name, average, minimum, maximum])

salary_list



import pandas as pd

df_salary = pd.DataFrame(salary_list, columns=['name', 'average', 'maximum', 'minimum'])

df_salary.to_csv('salary_list.csv', index=False, encoding='utf-8-sig')