import requests



import urllib.request
import  datetime
import os.path


#initialize date
today = datetime.date.today()
today2 = today - datetime.timedelta(days=1)
yesterday = today2.strftime('%m-%d-%Y')
print("Today's date:", yesterday)
#initialize path repo
raw_repo ='https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/'
print('Beginning download files ...')
#check if yesterday file for greece exist
if os.path.isfile('C:/Users/spyros/Documents/GitHub/masternew/covid-19/project/greece/greece_data/'+yesterday+'.csv'):
    print("Greek Data File exist")
else:
    print("Greek Data File Download")
    greece_url = 'https://raw.githubusercontent.com/iMEdD-Lab/open-data/master/COVID-19/greece.csv'
    urllib.request.urlretrieve(greece_url,'C:/Users/spyros/Documents/GitHub/masternew/covid-19/project/greece/greece_data/' + yesterday + '.csv')


if os.path.isfile('C:/Users/spyros/Documents/GitHub/masternew/covid-19/project/greece/greece_data/'+yesterday+'.csv'):
    print("Johns Hopkins University File exist")
else:
    print("Johns Hopkins University File Download")
    url = raw_repo + str(yesterday) + '.csv'
    urllib.request.urlretrieve(url,'C:/Users/spyros/Documents/GitHub/masternew/covid-19/project/daily_report/' + yesterday + '.csv')








