from bs4 import *
import re
import numpy as np
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
#chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")

q_term = input("Please input your search term:\n")

driver = webdriver.Chrome(options=chrome_options)


driver.get(f"https://scholar.google.com/scholar?start=0&q={q_term}&hl=en&num=20&as_sdt=0,5")

while "Our systems have detected unusual traffic from your computer network." in driver.page_source:
    time.sleep(1)

page_source = driver.page_source
soup = BeautifulSoup(page_source, "html.parser")
pretty_soup = soup.prettify()
    

#get paper titles
paper_tag = soup.select('[data-lid]')
paper_names = []
for tag in paper_tag:
    paper_names.append(tag.select('h3')[0].get_text())
for i in range(len(paper_names)):
    paper_names[i] = paper_names[i].replace("[HTML][HTML] ", "")
    paper_names[i].strip("[PDF][B][BOOK]")


#get citation numbers
pattern = r'Cited by (\d+)'
cite_count = re.findall(pattern, pretty_soup)


#get paper links
link_tag = soup.find_all('h3',{"class" : "gs_rt"})
link_array = []
for i in range(len(link_tag)):
    link_array.append(link_tag[i].a["href"])

driver.quit()


merged_array = np.column_stack([cite_count, paper_names, link_array])
sort_indices = np.argsort(merged_array[:, 0])[::-1]
merged_array_sorted = merged_array[sort_indices]


j = 0

for i in merged_array_sorted:
    print("Index: {} | Paper: {} | Citations: {} | Link: {}".format(j, merged_array_sorted[j, 1], merged_array_sorted[j, 0], merged_array_sorted[j, 2]))
    j = j + 1










