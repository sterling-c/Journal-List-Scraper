import csv
import re
from bs4 import BeautifulSoup

#This project takes a HTML webpage consisting of book information and returns a list of them in a csv file based on the subject matter. 

in_F = open("ProQuestDocuments-2018-09-20.html", "r")
out_F = open("Results.csv", "w")

soup = BeautifulSoup(in_F, 'html.parser')
books = soup.find_all("div")
bookInfo = []
for item in books:
	title = ''
	author = ''
	pubYear = ''
	ISSN = ''
	attributes = item.find_all("p")
	title = attributes[1].getText()
	for para in attributes:
		if(re.search("Correspondence author", para.getText())):
			author = para.getText().replace("Correspondence author: ","")
		if(re.search("Publication year", para.getText())):
			pubYear = para.getText().replace("Publication year: ","")
		if(re.search("ISSN", para.getText())):
			ISSN = para.getText().replace("ISSN: ","")
	bookInfo.append([title, author, pubYear, ISSN])
listWriter = csv.writer(out_F, delimiter=',')
listWriter.writerow(['Title', 'Correspondence Author', 'Publication Year', 'ISSN'])
for book in bookInfo:
	listWriter.writerow([book[0], book[1], book[2], book[3]])
out_F.close()
in_F.close()