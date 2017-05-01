import numpy as np
import pandas as pd
import requests
import json
import matplotlib.pyplot as plt

#data=pandas.read_csv('ham.csv',sep=';',na_values='.')

f=open("hamfeed.csv","r")
g=open("list.csv","r")  #file with names and ids of pages and groups
list = {}  #dictionary to store names and count of posts of any group or page in hamfeed file.
array={}   #dictionary to store id and names of groups and pages
for line in f:
    cells=line.split(";")
    val=cells[0].split("_")
    #print val[0]
    if not val[0] in array:
        '''base_url="https://graph.facebook.com/v2.7/186737671408393?fields=fan_count&access_token="+access_token
        results=requests.get(base_url)
        results_text=results.text
        results_json=json.loads(results_text)'''   #ignore this commented part
        for line in g:
            name=line.split(";")
            if val[0]==name[0]:
                a=name[1]
                array[val[0]]=a
                list[a]=1
                break
    else:
        list[array[val[0]]]+=1
#print list

d={}
count=0
for w in sorted(list, key=list.get, reverse=True):
      if list[w]==25:
          print w, list[w]
          d[w]=list[w]
          count+=1
      else:
          break
print count  #displays the total no of such groups or pages

width=1/1.5
plt.bar(range(len(d)), d.values(), align='center', color="pink")
plt.xticks(range(len(d)), d.keys())
plt.xlabel('Groups or Pages')
plt.ylabel('Number of hams posted')
plt.title('Top 10 Most Efficient Facebook Groups or Pages')
plt.savefig("bar",dpi=150)
plt.show()

f.close()
g.close()
