#!/usr/local/bin/python3

import requests
from bs4 import BeautifulSoup

from selenium import webdriver
#from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from time import sleep
import datetime as dt
import logging

discord_webhook_url = 'https://discordapp.com/api/webhooks/701291315270254622/6JBz0k7t4km3zYF-OR4kXdATVx3shtBzDcfJGvn_TZ_WusL-YIf_wZaj7xS2zYn6qEZ6'
# 必要なセレクター 上から回数、一般ボールナンバー、クラウンボール
site_url = 'https://ball.crown-777.com/index.php'
nummber_of_ball_selector = 'body > div > div.container > table > thead > tr > th:nth-child(4)'
general_ball_selector = 'body > div > div.container > table > tbody > tr:nth-child(1) > td:nth-child(4)'
crown_ball_selector = 'body > div > div.container > table > tbody > tr:nth-child(6) > td:nth-child(4)'

# debug formatter
formatter = '%(levelname)s : %(asctime)s : %(message)s'

def execScraping():
    # HEADLESSブラウザに接続
    browser = webdriver.Remote(
        command_executor='http://selenium-hub:4444/wd/hub',
        desired_capabilities=DesiredCapabilities.CHROME)

    browser.get(site_url)

    html = browser.page_source.encode('utf-8')
    soup = BeautifulSoup(html, "html.parser")

    try:
        get_number = soup.select_one(nummber_of_ball_selector).get_text()
        get_number = get_number.replace('回','')
        get_general = soup.select_one(general_ball_selector).get_text()

        get_crown = soup.select_one(crown_ball_selector).get_text()
        file_name = dt.datetime.now() + dt.timedelta(minutes=-3)
        today = file_name.strftime('%Y-%m-%d')
        file_name = 'data/' + today + '.tsv'
        with open(file_name,mode='a') as f:
            f.write(today + '\t' + get_number + '\t' + get_general + '\t' + get_crown + '\n')
        logging.info('%s %s', 'Success', get_number)
    except:
        import traceback
        traceback.print_exc()
        sleep(1)
        execScraping()
        webhook_content = {
            "content": "execScrapingでエラーが発生しました。"
        }
        requests.post(discord_webhook_url,webhook_content)
    finally:
        # 終了
        browser.close()
        browser.quit()

def exec():
    try:
        execScraping()
    except Exception as e:
        logging.warning('-' * 10)
        logging.warning('Scraping Failure')
        logging.warning('Error dosomething: %s', e)
        webhook_content = {
            "content": "execでエラーが発生しました。"
        }
        requests.post(discord_webhook_url,webhook_content)
        sleep(10)
        exec()

if __name__ == '__main__':
    logging.basicConfig(filename='logging.log', level=logging.INFO, format=formatter)
    logging.debug('%s', 'Scraping Start')
    exec()
