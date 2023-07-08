import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import datetime
chrome_options = Options()
# chrome_options.headless = True
# chrome_options.add_argument("window-size=1536,864")
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument('--load-extension=C:\\Users\\imdec\\Desktop\\YASH\\Projects\\Extension')
if __name__ == '__main__':
    # 1: Nifty Moneycontrol
    st1=0
    # 2: Nifty Investing
    st2=0
    # 3: Bank Nifty Moneycontrol
    st3=1
    # 4: Bank Nifty Investing
    st4=1
    # 5: FII DII
    st5=1
    # 6: Dow Jones
    st6=1
    # 7: Oilprice
    st7=1
    # 8: Put Call Ratio
    st8=1
    # 9: Option Chain
    st9=1
    driver = uc.Chrome(options=chrome_options)
    driver.set_page_load_timeout(15)
    driver.get('chrome://version/')
    time.sleep(0.2)
    try:
        driver.switch_to.window(driver.window_handles[1])
        driver.close()
    except:
        pass
    time.sleep(0.2)

    try:
        driver.switch_to.window(driver.window_handles[1])
        driver.close()
    except:
        pass
    driver.switch_to.window(driver.window_handles[0])

    while st1:
        try:
            driver.get('https://www.moneycontrol.com/indian-indices/nifty-50-9.html')
            time.sleep(10)
            try:
                driver.find_element_by_xpath("/html/body/div[15]/div[2]/div[3]/button[1]").click()
            except:
                pass
            driver.find_element_by_xpath("/html/body/div[9]/div/div[2]").screenshot("C:\\Users\\imdec\\Desktop\\YASH\\Projects\\Resources\\1.png")
            try:
                driver.find_element_by_xpath("/html/body/div[15]/div[2]/div[3]/button[1]").click()
            except:
                pass
            time.sleep(0.2)
            driver.find_element_by_xpath("/html/body/div[9]/div/div[5]/div[1]/div[1]/div[1]/div[2]/div").screenshot("C:\\Users\\imdec\\Desktop\\YASH\\Projects\\Resources\\2.png")
            try:
                driver.find_element_by_xpath("/html/body/div[15]/div[2]/div[3]/button[1]").click()
            except:
                pass
            time.sleep(2)
            driver.find_element_by_xpath("/html/body/div[9]/div/div[5]/div[1]/div[1]/div[1]/div[4]").screenshot("C:\\Users\\imdec\\Desktop\\YASH\\Projects\\Resources\\3.png")
            time.sleep(0.2)
            driver.find_element_by_xpath("/html/body/div[9]/div/div[5]/div[1]/div[1]/div[1]/div[9]").screenshot("C:\\Users\\imdec\\Desktop\\YASH\\Projects\\Resources\\4.png")
            driver.execute_script("window.scrollTo(0,20);")
            driver.find_element_by_xpath("/html/body/div[9]/div/div[5]/div[1]/div[3]/div[1]/div[1]").screenshot("C:\\Users\\imdec\\Desktop\\YASH\\Projects\\Resources\\5.png")
            driver.execute_script("window.scrollTo(0,20);")
            driver.find_element_by_xpath("/html/body/div[9]/div/div[5]/div[1]/div[3]/div[2]/div[1]").screenshot("C:\\Users\\imdec\\Desktop\\YASH\\Projects\\Resources\\6.png")
            break
        except:
            pass

    while st2:
        try:
            driver.get('https://in.investing.com/indices/s-p-cnx-nifty-components')
            time.sleep(2)
            driver.find_element_by_xpath("/html/body/div/div[4]/section[2]/div/section[2]/section[2]/div[1]/div/table/thead/tr/th[8]").click()
            driver.execute_script("window.scrollTo(0,610);")
            driver.find_element_by_xpath("/html/body/div/div[4]/section[2]/div/section[2]/section[2]/div[1]/div/table").screenshot("C:\\Users\\imdec\\Desktop\\YASH\\Projects\\Resources\\7.png")
            driver.find_element_by_xpath("/html/body/div/div[4]/section[2]/div/section[2]/section[2]/div[1]/div/table/thead/tr/th[8]").click()
            driver.find_element_by_xpath("/html/body/div/div[4]/section[2]/div/section[2]/section[2]/div[1]/div/table").screenshot("C:\\Users\\imdec\\Desktop\\YASH\\Projects\\Resources\\8.png")
            break
        except:
            pass

    while st3:
        try:
            driver.get('https://www.moneycontrol.com/indian-indices/bank-nifty-23.html')
            time.sleep(5)
            try:
                driver.find_element_by_xpath("/html/body/div[15]/div[2]/div[3]/button[1]").click()
            except:
                pass
            driver.find_element_by_xpath("/html/body/div[9]/div/div[2]").screenshot("C:\\Users\\imdec\\Desktop\\YASH\\Projects\\Resources\\9.png")
            time.sleep(0.2)
            driver.find_element_by_xpath("/html/body/div[9]/div/div[5]/div[1]/div[1]/div[1]/div[2]/div").screenshot("C:\\Users\\imdec\\Desktop\\YASH\\Projects\\Resources\\10.png")
            time.sleep(2)
            driver.find_element_by_xpath("/html/body/div[9]/div/div[5]/div[1]/div[1]/div[1]/div[4]").screenshot("C:\\Users\\imdec\\Desktop\\YASH\\Projects\\Resources\\11.png")
            time.sleep(0.2)
            driver.find_element_by_xpath("/html/body/div[9]/div/div[5]/div[1]/div[1]/div[1]/div[9]").screenshot("C:\\Users\\imdec\\Desktop\\YASH\\Projects\\Resources\\12.png")
            break
        except:
            pass

    while st4:
        try:
            driver.get('https://in.investing.com/indices/bank-nifty-components')
            time.sleep(2)
            driver.find_element_by_xpath("/html/body/div/div[4]/section[2]/div/section[2]/section/div[1]/div/table/thead/tr/th[8]").click()
            driver.execute_script("window.scrollTo(0,500);")
            driver.find_element_by_xpath("/html/body/div/div[4]/section[2]/div/section[2]/section/div[1]/div/table").screenshot("C:\\Users\\imdec\\Desktop\\YASH\\Projects\\Resources\\13.png")
            break
        except:
            pass

    while st5:
        try:
            driver.get('https://www.moneycontrol.com/stocks/marketstats/fii_dii_activity/index.php')
            time.sleep(2)
            try:
                driver.find_element_by_xpath("/html/body/div[15]/div[2]/div[3]/button[1]").click()
            except:
                pass
            driver.find_element_by_xpath("/html/body/section/div/div[4]/div[1]").screenshot("C:\\Users\\imdec\\Desktop\\YASH\\Projects\\Resources\\14.png")
            time.sleep(1)
            driver.find_element_by_xpath("/html/body/section/div/div[4]/div[1]/ul/li[2]/a").click()
            time.sleep(1)
            driver.find_element_by_xpath("/html/body/section/div/div[4]/div[1]").screenshot("C:\\Users\\imdec\\Desktop\\YASH\\Projects\\Resources\\15.png")
            time.sleep(1)
            driver.find_element_by_xpath("/html/body/section/div/div[4]/div[1]/div/div[2]/div[1]/div/ul/li[2]/a").click()
            time.sleep(1)
            driver.find_element_by_xpath("/html/body/section/div/div[4]/div[1]").screenshot("C:\\Users\\imdec\\Desktop\\YASH\\Projects\\Resources\\16.png")
            break
        except:
            pass
    while st6:
        try:
            driver.get('https://www.google.com/finance/quote/.DJI:INDEXDJX')
            time.sleep(1)
            driver.find_element_by_xpath("/html/body/c-wiz/div/div[4]/div/main").screenshot("C:\\Users\\imdec\\Desktop\\YASH\\Projects\\Resources\\17.png")
            break
        except:
            pass
    while st7:
        try:
            driver.get('https://oilprice.com/')
            time.sleep(2)
            driver.find_element_by_xpath("/html/body/div[2]/div[3]/div/div[1]").screenshot("C:\\Users\\imdec\\Desktop\\YASH\\Projects\\Resources\\18.png")
            break
        except:
            pass

    exp=3 #For thursday it is 3
    x=datetime.datetime.now()
    if x.weekday()<exp:
        x=x-datetime.timedelta(x.weekday())+datetime.timedelta(exp)
    else:
        x+=datetime.timedelta(7)
        x=x-datetime.timedelta(x.weekday())+datetime.timedelta(exp)
    hlpr=str(x.strftime("%d")+"-"+x.strftime("%m")+"-"+x.strftime("%Y"))
    print(hlpr)


    while st8:
        try:
            driver.get('https://www.niftytrader.in/nifty-put-call-ratio')
            time.sleep(3)
            driver.find_element_by_xpath("/html/body/div[1]/div/div/div[5]/div/div[1]/div[2]").screenshot("C:\\Users\\imdec\\Desktop\\YASH\\Projects\\Resources\\19.png")
            driver.find_element_by_xpath("/html/body/div[1]/div/div/div[5]/div/div[1]/div[2]/div[2]/div[2]/div/div/a[2]").click()
            time.sleep(4)
            driver.find_element_by_xpath("/html/body/div[1]/div/div/div[5]/div/div[1]/div[2]").screenshot("C:\\Users\\imdec\\Desktop\\YASH\\Projects\\Resources\\20.png")
            break
        except:
            pass

    time.sleep(1.5)

    exp=3 #For thursday it is 3
    x=datetime.datetime.now()
    if x.weekday()<exp:
        x=x-datetime.timedelta(x.weekday())+datetime.timedelta(exp)
    else:
        x+=datetime.timedelta(7)
        x=x-datetime.timedelta(x.weekday())+datetime.timedelta(exp)
    hlpr=str(x.strftime("%d")+"-"+x.strftime("%m")+"-"+x.strftime("%Y"))
    print(hlpr)
    while st9:
        try:
            driver.get('https://www.nseindia.com/option-chain')

            time.sleep(2)
            hlpr=str(x.strftime("%d")+"-"+x.strftime("%b")+"-"+x.strftime("%Y"))
            for i in range(1,100):
                print(i)
                strr='/html/body/div[10]/div[2]/section/div/div/div/div/div[1]/div[1]/div/div/div[2]/div[3]/div/select/option['+str(i)+']'
                print(driver.find_element_by_xpath(strr).get_attribute("value"),hlpr)
                if driver.find_element_by_xpath(strr).get_attribute("value")==hlpr:
                    driver.find_element_by_xpath(strr).click()
                    break
            time.sleep(1)

            curr = driver.find_element_by_xpath('/html/body/div[10]/div[2]/section/div/div/div/div/div[1]/div[1]/div/div/div[3]/div[1]/div[1]/span[2]').text
            curr=int(curr.replace(',','').replace('NIFTY ','')[0:-3])
            curr=curr-(curr%50)
            ans=curr+650
            for i in range(1000):
                iter = driver.find_element_by_xpath('/html/body/div[10]/div[2]/section/div/div/div/div/div[1]/div[1]/div/div/div[3]/div[2]/div/div/table[1]/tbody/tr['+str(i+1)+']/td[12]/a').text
                iter=int(iter.replace(',','')[0:-3])
                if (ans==iter):
                    driver.find_element_by_xpath('/html/body/div[10]/div[2]/section/div/div/div/div/div[1]/div[1]/div/div/div[3]/div[2]/div/div/table[1]/tbody/tr['+str(i+1)+']/td[12]/a').screenshot("C:\\Users\\imdec\\Desktop\\YASH\\Projects\\Resources\\21.png")
                    break
            time.sleep(0.5)
            driver.find_element_by_xpath("/html/body/div[10]/div[2]/section/div/div/div/div/div[1]/div[1]/div/div/div[3]/div[2]/div/div/table[1]").screenshot("C:\\Users\\imdec\\Desktop\\YASH\\Projects\\Resources\\21.png")
            driver.execute_script("window.scrollTo(0,0);")
            driver.find_element_by_xpath('/html/body/div[10]/div[2]/section/div/div/div/div/div[1]/div[1]/div/div/div[2]/div[1]/div/select/option[4]').click()
            time.sleep(0.3)
            for i in range(1,100):
                strr='/html/body/div[10]/div[2]/section/div/div/div/div/div[1]/div[1]/div/div/div[2]/div[3]/div/select/option['+str(i)+']'
                if driver.find_element_by_xpath(strr).get_attribute("value")==hlpr:
                    print(driver.find_element_by_xpath(strr).get_attribute("value"))
                    driver.find_element_by_xpath(strr).click()
                    break

            time.sleep(1)
            for i in range(1,100):
                strr='/html/body/div[10]/div[2]/section/div/div/div/div/div[1]/div[1]/div/div/div[2]/div[3]/div/select/option['+str(i)+']'
                if driver.find_element_by_xpath(strr).get_attribute("value")==hlpr:
                    print(driver.find_element_by_xpath(strr).get_attribute("value"))
                    driver.find_element_by_xpath(strr).click()
                    break

            time.sleep(1)

            curr = driver.find_element_by_xpath('/html/body/div[10]/div[2]/section/div/div/div/div/div[1]/div[1]/div/div/div[3]/div[1]/div[1]/span[2]').text
            curr=int(curr.replace(',','').replace('BANKNIFTY ','')[0:-3])
            curr=curr-(curr%100)
            ans=curr+1300
            for i in range(1000):
                iter = driver.find_element_by_xpath('/html/body/div[10]/div[2]/section/div/div/div/div/div[1]/div[1]/div/div/div[3]/div[2]/div/div/table[1]/tbody/tr['+str(i+1)+']/td[12]/a').text
                iter=int(iter.replace(',','')[0:-3])
                if (ans==iter):
                    driver.find_element_by_xpath('/html/body/div[10]/div[2]/section/div/div/div/div/div[1]/div[1]/div/div/div[3]/div[2]/div/div/table[1]/tbody/tr['+str(i+1)+']/td[12]/a').screenshot("C:\\Users\\imdec\\Desktop\\YASH\\Projects\\Resources\\22.png")
                    break

            time.sleep(0.5)
            driver.find_element_by_xpath("/html/body/div[10]/div[2]/section/div/div/div/div/div[1]/div[1]/div/div/div[3]/div[2]/div/div/table[1]").screenshot("C:\\Users\\imdec\\Desktop\\YASH\\Projects\\Resources\\22.png")
            break
        except:
            pass
    driver.quit()
    print("\n\n\n\n\n\n\n\n\n\nProgram Ended")