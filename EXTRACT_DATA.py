from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from unidecode import unidecode
import pyodbc
import json




driver = webdriver.Chrome()
def sofa_squard(url):
        global df12
        print("Extracting squard details")
        global df10
        #url='https://www.sofascore.com/team/football/atletico-madrid/2836'
        driver.get(url)
        driver.maximize_window()
        time.sleep(10)

        lv='/html/body/div[1]/main/div[2]/div/div[2]/div[1]/div[5]/div[1]/div[3]/span'
            
            
        select=driver.find_element(By.XPATH,lv)
        driver.execute_script("arguments[0].scrollIntoView();", select)
        driver.execute_script("arguments[0].click();", select)

        ppath='/html/body/div[1]/main/div[2]/div/div[2]/div[1]/div[5]/div[1]/div[4]/div/table/tr[1]/td[1]/a/div/span'
        jpath='/html/body/div[1]/main/div[2]/div/div[2]/div[1]/div[5]/div[1]/div[4]/div/table/tr[1]/td[1]/a/div/div/div'
        pname=[]
        jno=[]
        row=len(driver.find_elements(By.XPATH,'/html/body/div[1]/main/div[2]/div/div[2]/div[1]/div[5]/div[1]/div[4]/div/table/tr'))
        for i in range(1,row+1):
                ppath='/html/body/div[1]/main/div[2]/div/div[2]/div[1]/div[5]/div[1]/div[4]/div/table/tr[{}]/td[1]/a/div/span'.format(i)
                jpath='/html/body/div[1]/main/div[2]/div/div[2]/div[1]/div[5]/div[1]/div[4]/div/table/tr[{}]/td[1]/a/div/div/div'.format(i)
                pname.append(driver.find_element(By.XPATH,ppath).text)
                jno.append(driver.find_element(By.XPATH,jpath).text)
        ss=dict(Jno=jno,Player_name=pname)
        df12=pd.DataFrame.from_dict(ss)
        #print(df12.head(5))

def sofa_rating(url):
        print("Extracting rating")
        global df10,df_inner
        
        #url='https://www.sofascore.com/team/football/atletico-madrid/2836'
        driver.get(url)
        driver.maximize_window()
        time.sleep(10)
        pname=[]
        rating=[]
        sm='/html/body/div[1]/main/div[2]/div/div[2]/div[2]/div[3]/div[2]/div/button/div/span'
        select=driver.find_element(By.XPATH,sm)
        driver.execute_script("arguments[0].scrollIntoView();", select)
        driver.execute_script("arguments[0].click();", select)
        row=len(driver.find_elements(By.XPATH,'/html/body/div[1]/main/div[2]/div/div[2]/div[2]/div[3]/div[2]/a'))
        for i in range(1,row+1):
                npath='/html/body/div[1]/main/div[2]/div/div[2]/div[2]/div[3]/div[2]/a[{}]/div/div[2]/span'.format(i)
                rpath='/html/body/div[1]/main/div[2]/div/div[2]/div[2]/div[3]/div[2]/a[{}]/div/span[2]/div/span'.format(i)
                pname.append(driver.find_element(By.XPATH,npath).text)
                rating.append(driver.find_element(By.XPATH,rpath).text)
        
        sofascore=dict(Player_name=pname,Ratings=rating)
        df10=pd.DataFrame.from_dict(sofascore)

        df_inner = pd.merge(df10, df12, on='Player_name', how='inner')
        df_inner =df_inner.drop(['Player_name'],axis=1)
        #print(df_inner.head(2))
        
def squard_stats(url,club):
        global df4
        
        #print("Extracting Barca squard stats")
        driver.get(url)
        driver.maximize_window()
        time.sleep(20)
        
        row=len(driver.find_elements(By.XPATH,'/html/body/div[1]/div[6]/div[3]/div[3]/div/div[2]/div/table/tbody/tr'))
 
        name=[]
        jersey=[]
        mins=[]
        games=[]
        start=[]
        pos=[]
        yellow=[]
        red=[]
        sub=[]
        sub_off=[]
        two_y=[]
        goal=[]
        pen=[]
        og=[]
        gc=[]
        if(club=='REAL-MADRID'):
                row=32
                
        for i in range(1,row+1):
                if(club=='SEVILLA-FC' and i==29):
                        continue
                if(club=='RCD-MALLORCA' and (i==28 or i==30)):
                        continue
                if(club=='GETAFE-CF' and i==33):
                        continue
                npath='/html/body/div[1]/div[6]/div[3]/div[3]/div/div[2]/div/table/tbody/tr[{}]/td[4]/p'.format(i)
                num='/html/body/div[1]/div[6]/div[3]/div[3]/div/div[2]/div/table/tbody/tr[{}]/td[2]/p'.format(i)
                mipath='/html/body/div[1]/div[6]/div[3]/div[3]/div/div[2]/div/table/tbody/tr[{}]/td[5]/p'.format(i)
                gpath='/html/body/div[1]/div[6]/div[3]/div[3]/div/div[2]/div/table/tbody/tr[{}]/td[6]/p'.format(i)
                spath='/html/body/div[1]/div[6]/div[3]/div[3]/div/div[2]/div/table/tbody/tr[{}]/td[7]/p'.format(i)
                ppath='/html/body/div[1]/div[6]/div[3]/div[3]/div/div[2]/div/table/tbody/tr[{}]/td[3]/p'.format(i)
                ypath='/html/body/div[1]/div[6]/div[3]/div[3]/div/div[2]/div/table/tbody/tr[{}]/td[10]/p'.format(i)
                rpath='/html/body/div[1]/div[6]/div[3]/div[3]/div/div[2]/div/table/tbody/tr[{}]/td[11]/p'.format(i)
                supath='/html/body/div[1]/div[6]/div[3]/div[3]/div/div[2]/div/table/tbody/tr[{}]/td[8]/p'.format(i)
                suopath='/html/body/div[1]/div[6]/div[3]/div[3]/div/div[2]/div/table/tbody/tr[{}]/td[9]/p'.format(i)
                typath='/html/body/div[1]/div[6]/div[3]/div[3]/div/div[2]/div/table/tbody/tr[{}]/td[12]/p'.format(i)
                gopath='/html/body/div[1]/div[6]/div[3]/div[3]/div/div[2]/div/table/tbody/tr[{}]/td[13]/p'.format(i)
                penpath='/html/body/div[1]/div[6]/div[3]/div[3]/div/div[2]/div/table/tbody/tr[{}]/td[14]/p'.format(i)
                ogpath='/html/body/div[1]/div[6]/div[3]/div[3]/div/div[2]/div/table/tbody/tr[{}]/td[15]/p'.format(i)
                gcpath='/html/body/div[1]/div[6]/div[3]/div[3]/div/div[2]/div/table/tbody/tr[{}]/td[16]/p'.format(i)
                
                #if(driver.find_element(By.XPATH,ppath).text == 'Goalkeeper'):
                #        continue
        
                name.append(driver.find_element(By.XPATH,npath).text)
                jersey.append(driver.find_element(By.XPATH,num).text)
                mins.append(driver.find_element(By.XPATH,mipath).text)
                games.append(driver.find_element(By.XPATH,gpath).text)
                start.append(driver.find_element(By.XPATH,spath).text)
                pos.append(driver.find_element(By.XPATH,ppath).text)
                yellow.append(driver.find_element(By.XPATH,ypath).text)
                red.append(driver.find_element(By.XPATH,rpath).text)
                sub.append(driver.find_element(By.XPATH,supath).text)
                sub_off.append(driver.find_element(By.XPATH,suopath).text)
                two_y.append(driver.find_element(By.XPATH,typath).text)
                goal.append(driver.find_element(By.XPATH,gopath).text)
                pen.append(driver.find_element(By.XPATH,penpath).text)
                og.append(driver.find_element(By.XPATH,ogpath).text)
                gc.append(driver.find_element(By.XPATH,gcpath).text)
                

        squard_stat= dict(Jno=jersey,Name =name,Position=pos,Mins_played=mins,Matchs=games,Start=start,Yellow=yellow,Red=red,Substitute=sub,Subbed_off=sub_off,Two_yellow=two_y,Goals=goal,Penalty=pen,Own_goals=og,Goals_conceded=gc)
        df4 = pd.DataFrame.from_dict(squard_stat)
        #print(df4.head())




def load_temp(club):
        col=list(df_final.columns)
        #print(col)
        #print(col)
        cnxn = pyodbc.connect('DRIVER={SQL Server};Server=GANESH-LAPTOP;Database=laliga_player_stats;')
        cursor = cnxn.cursor()
        i=0
        club=club.replace("-","_")
        dq="DROP TABLE IF EXISTS {}".format(club)
        cursor.execute(dq)
        cnxn.commit()
        
        cq="create table {} ({} int,{} varchar(30),{} varchar(30),{} int,{} int,{} int,{} int,{} int,{} int,{} int,{} int,{} int,{} int,{} int,{} int,{} float);".format(club,col[0],col[1],col[2],col[3],col[4],col[5],col[6],col[7],col[8],col[9],col[10],col[11],col[12],col[13],col[14],col[15])
        cursor.execute(cq)
        cnxn.commit()
        print("....success...")
        for index, row in df_final.iterrows():
                #print(row[col[1]])
                iq="insert into {} values({},'{}','{}',{},{},{},{},{},{},{},{},{},{},{},{},{})".format(club,row[col[0]],row[col[1]],row[col[2]],row[col[3]],row[col[4]],row[col[5]],row[col[6]],row[col[7]],row[col[8]],row[col[9]],row[col[10]],row[col[11]],row[col[12]],row[col[13]],row[col[14]],row[col[15]])
                cursor.execute(iq)
        cnxn.commit()
        print("......inserted.......")
        cursor.close()

def load():
        cnxn = pyodbc.connect('DRIVER={SQL Server};Server=GANESH-LAPTOP;Database=laliga_player_stats;')
        cursor = cnxn.cursor()
        sql_query=pd.read_sql("SELECT * FROM LALIGA_STATS",cnxn)
        df = pd.DataFrame(sql_query)
        df.to_csv("Laliga_stats.csv",index=False)
        

def extract_data():
        '''global df_final
        url5='https://www.laliga.com/en-GB/laliga-santander/standing'
        driver.get(url5)
        driver.maximize_window()
        time.sleep(10)
        #print("Extracting laliga team names")
        tname=[]
        
        tpath='/html/body/div[1]/div[6]/div[2]/div/div[3]/div[1]/div[1]/div/div[3]/div[1]/div/div/div[2]/div[2]/p'
        tname.append(driver.find_element(By.XPATH,tpath).text)
        row=len(driver.find_elements(By.XPATH,'/html/body/div[1]/div[6]/div[2]/div/div[3]/div[1]/div[1]/div/div'))
        for i in range(4,row+1):
                tpath='/html/body/div[1]/div[6]/div[2]/div/div[3]/div[1]/div[1]/div/div[{}]/div[1]/div/div/div[2]/div[2]/p'.format(i)
                tname.append(driver.find_element(By.XPATH,tpath).text)
                
                
        for i in tname:
                club=i.replace(" ","-")
                club=str(unidecode(club))
                #print(club)
                if(club.lower() !='granada-cf' and club.lower() !='ud-las-palmas' and club.lower() !='deportivo-alaves' and club.lower() !='ca-osasuna'):
                        url='https://www.laliga.com/en-GB/clubs/{}/stats'.format(club.lower())
                        print(url+" "+club)
                        squard_stats(url,club)
                        f = open('rating_link.json')
                        data=json.load(f)
                        url1=data[club]
                        sofa_squard(url1)
                        sofa_rating(url1)
                        df_final=pd.merge(df4,df_inner,on='Jno',how='inner')
                        #print(df_final.head(2))
                        load_temp(club)'''
        load()
                        
                
        
if(__name__=='__main__'):
        extract_data()
