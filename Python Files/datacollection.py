import requests
import json

access_token='EAAMcWZCJ7Ui4BALHXjXKkizZANG5AhQZAL9buUS5KR6fX8YurTosJLmxTfP4WoZBiP8DFe8eqbJ2NplRPGLsve2xYIwwsbERTnX5pvsiRIvJ0So1TZAHmOHlUPVnzZCBjPdZBhkm8CBnYTV0eNjAwQiBVkroQGnaqgZD'
outfile=open("list.csv","w")


def text_cleaning(text):
        text = text.encode('ascii', 'ignore').decode('ascii')
        #text=text.replace('\\','BSL')
        #text=text.replace('\'','SIC')
        #text=text.replace("'",'TLD')
        #text=text.replace('"','DIC')
        text=text.replace('\n','. ')
        #text=text.replace(')','CBR')
        #text=text.replace('(','OBR')
        text=text.replace(';',', ')
        #text=text.replace(',','COM')
        return text



def search(group_name):
    base_url = 'https://graph.facebook.com/search?limit=1000&type=group&q='+group_name+'&access_token='+access_token
    results=requests.get(base_url)
    results_text=results.text
    results_json=json.loads(results_text)
    for item in results_json['data']:
         if item['privacy']=='OPEN':
             try:
                 #print item['name']
                 outfile.write(item['id']+";"+item['name'])
                 outfile.write("\n")
                 #print ''
             except:
                pass
    base_url = 'https://graph.facebook.com/search?limit=1000&type=page&q='+group_name+'&access_token='+access_token
    results=requests.get(base_url)
    results_text=results.text
    results_json=json.loads(results_text)
    for item in results_json['data']:
             try:
                 #print item['name']
                 outfile.write(item['id']+";"+item['name'])
                 outfile.write("\n")
                 #print ''
             except:
                pass    
search('internships')
search('startup')
search('jobs')
outfile.close()
infile=open("list.csv","r")
outfile=open("feed.csv","w")
for line in infile:
    print line.split(';')[0]
    base_url='https://graph.facebook.com/v2.6/'+line.split(';')[0]+'/feed?access_token='+access_token
    results=requests.get(base_url)
    results_text=results.text
    results_json=json.loads(results_text)
    #while(True):
        #try:
    for item in results_json['data']:
              if 'message' in item:
                 print text_cleaning(item['message'])
                 print ''
                 if 'updated_time' in item:
                     outfile.write(item['id']+";"+text_cleaning(item['message'])+";"+item['updated_time'])
                     outfile.write("\n")
                 else:
                     outfile.write(item['id']+";"+text_cleaning(item['message'])+";"+item['created_time'])
                     outfile.write("\n")
          #base_url=results_json['paging']['next']
          #results=requests.get(base_url)
          #results_text=results.text
          #results_json=json.loads(results_text)
        #except KeyError:
                #break

outfile.close()
infile.close()



        
        
    
