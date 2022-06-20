from bs4 import *
import requests
import re
import numpy as np
import time 
import webbrowser

q_term = input("Please input your search term\n")

page = requests.get(f"https://scholar.google.com/scholar?q{q_term}&hl=en&num=20&as_sdt=0,5")
soup = BeautifulSoup(page.content, "html.parser")
pretty_soup = soup.prettify()
    

#get paper titles
paper_tag = soup.select('[data-lid]')
paper_names = []
for tag in paper_tag:
    paper_names.append(tag.select('h3')[0].get_text())
for i in range(len(paper_names)):
    paper_names[i] = paper_names[i].replace("[HTML][HTML] ", "")

#get citation numbers
cite_tag = soup.find_all(lambda tag: tag.name == 'a')
cite_count = []
pattern = re.compile("\">Cited by [0-9]+</a>")


#get paper links
link_tag = soup.find_all('h3',{"class" : "gs_rt"})
link_array = []
for i in range(len(link_tag)):
    link_array.append(link_tag[i].a["href"])

#testing cite output
print (cite_tag)
print(type(cite_count))

merged_array = np.column_stack([paper_names, cite_count])
merged_array_sorted = np.sort(merged_array, axis= -1)

j = 0

for i in merged_array_sorted:
    print("Index: {}\tPaper: {}\tCitations: {}".format(j, merged_array_sorted[j, 0], merged_array_sorted[j, 1]))
    j = j + 1











