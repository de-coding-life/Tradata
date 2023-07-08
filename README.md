
# Tradata

## Description

This project automates the collection of daily stock market data, including option chain, index prices, and FII DII data from multiple stock market websites thereby efficiently presenting it to the user in a clear and summarized format. By using this automation, the data collection process takes an average of **2 minutes and 6 seconds**, compared to the **7 minutes and 35 seconds** it would take to gather the data manually,thereby resulting in a significant time saving of approximately **72.31%**.

## Issues Faced
* Adverstisements in several websites changed the **xpath** for several elements resulting in error, to tackle this I added *Adblock extension* in the selenium webdriver.

* Some websites detected selenium being used, and hence **denied** connection requestion,so I used *undetected chromedriver* to access all the websites.








