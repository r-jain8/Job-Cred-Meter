import os, random
import nltk
import csv
import re
import pprint
from nltk import word_tokenize, WordNetLemmatizer
from nltk.corpus import stopwords
import spamham as sf

def find(text):
    lemmatizer = WordNetLemmatizer()
    text1=[lemmatizer.lemmatize(word.lower()) for word in word_tokenize(unicode(text, errors='ignore'))]
    #text1=nltk.word_tokenize(text)
    ans=nltk.pos_tag(text1)
    flag=0
    #print ans
    for s in ans:
        if 'stipend' in s in ans:
            #print 'ooops'
            flag=1
            break
        elif 'searching' in s in ans:
            #print 'ok'
            flag=1
            break
        elif 'looking' in s in ans:
            #print 'ok'
            flag=1
            break
        elif 'hiring' in s in ans:
            #print 'ok'
            flag=1
            break
        elif 'salary' in s in ans:
            #print 'huh'
            flag=1
            break;
        elif 'location' in s in ans:
            #print 'has'
            flag=1
            break
        elif 'startup' in s in ans:
            #print 'has'
            flag=1
            break
        elif 'interested' in s in ans:
            #print 'has'
            flag=1
            break
        elif 'INR' in s in ans:
            #print 'has'
            flag=1
            break
        elif 'apply' in s in ans:
            #print 'ok'
            flag=1
            break
        elif 'interns' in s in ans:
            #print 'ok'
            flag=1
            break
        elif 'work' in s in ans:
            #print 'ok'
            flag=1
            break
        elif 'earn' in s in ans:
            #print 'ok'
            flag=1
            break
        elif 'opportunity' in s in ans:
            #print 'ok'
            flag=1
            break
        elif 'contact' in s in ans:
            #print 'okay'
            flag=1
            break
        elif 'Rs' in s in ans:
            #print 'okay'
            flag=1
            break
    return flag       
    

def text_cleaning(text):
        text = text.encode('ascii', 'ignore')
        return text

def myfunction(text):
    try:
        text = unicode(text, 'utf-8')
        return text
    except TypeError:
        return text

def run_online(classifier, setting):
    while True:
      features = sf.get_features(raw_input('Your new post: '), setting)
      if (len(features) == 0):
         break
      print (classifier.classify(features))

def detect_spam(wb, classifier, setting):
    for line in wb:
          cells=line.split(";")
          x=text_cleaning(cells[1])
          features=sf.get_features(x,setting)
          val=classifier.classify(features)
          if val=='ham':
              ans=find(x)
              if ans==0:
                  val='spam'
          outfile.write(cells[0]+";"+x+";"+val)
          outfile.write("\n")

          
#run_online(classifier, "")   
if __name__=="__main__":     
    wb1=open("spam.csv","r")
    wb2=open("ham.csv","r")
    wb3=open("feed.csv","r")

    spam = sf.init_lists(wb1)
    ham = sf.init_lists(wb2)
    all_emails = [(email, 'spam') for email in spam]
    all_emails += [(email, 'ham') for email in ham]
    random.shuffle(all_emails)
    print ('Corpus size = ' + str(len(all_emails)) + ' posts')
    all_features = [(sf.get_features(email, ''), label) for (email, label) in all_emails]
    train_set, test_set, classifier = sf.train(all_features, 1.0)
    sf.evaluate(train_set, test_set, classifier)
#classify your new post


          
    outfile=open("filtered.csv","w")
    detect_spam(wb3, classifier, "")
    
    outfile.close()
    wb1.close()
    wb2.close()
    wb3.close()
    
    outfile1=open("ham.csv","a")
    outfile2=open("spam.csv","a")
    f = open( 'filtered.csv', "r" ) 
    for line in f:
        cells = line.split( ";" )
        x=cells[1]
        y=cells[2]
        #print (y)
        
        if len(y)==4:
            outfile1.write(cells[0]+";"+text_cleaning(x))
            outfile1.write("\n")
            
        elif len(y)==5:
            outfile2.write(cells[0]+";"+text_cleaning(x))
            outfile2.write("\n")
           

    f.close() 
