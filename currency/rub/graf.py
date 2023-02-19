import requests 
from bs4 import BeautifulSoup
import time 
from time import gmtime, strftime
from fake_useragent import UserAgent
import pandas as pd 
from datetime import datetime 
import plotly.express as px

class Data:      
     
    #  headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}
     rum2 = "https://wise.com/gb/currency-converter/rub-to-amd-rate"
     

  
     # def __init__(self):
     #      self.current_converted_price = float(self.amd())

          

     ua = UserAgent()
     headers = {'User-Agent':ua.chrome}


     def time(self):
          d = datetime.now()
          data = d.strftime("%a %d %b %Y %H:%M:%S ")
          return data


     # def change(self):
     #     with open('data.csv') as f:
     #      #     last5 = (list(f)[-5:][2])
     #          last = pd.read_csv('data.csv',delimiter=',')
     #          lastF = last.pop('5')
     #      #     lasta =  list(map(str, last.split()))
     #      #     lastF = lasta[2]
              
     #     return  last


     def amd(self):

          full_page = requests.get(self.rum2)

          soup = BeautifulSoup(full_page.content, 'html.parser')

          convert = soup.findAll("span",{"class":"text-success"})

          return convert[0].text
          


     def data_w(self):
          writer = open('data.csv', 'a+')
          data = '\n'+self.time()+ ',' +self.amd() +','
          writer.write(data)
          time.sleep(3)
          self.data_w()


 
d = pd.read_csv('data.csv',delimiter=',')
d.pop('5')



def img():
     fig = px.line(d, x ='Date', y ='AMD', title='Курс рубль-драм')
     fig.write_image('currey.jpeg')
     time.sleep(3)
     img()



print(img())


# d.drop(1,axis=1)
# n=d.set_index('Date')
# n=data.amd()
# print(n)

data = Data()  
print(data.data_w())




