from bs4 import BeautifulSoup
import requests


url = 'https://icodrops.com/category/active-ico/'


def get_info(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "lxml")
    return soup


def all_info(func):
    final_info = {}
    ico_list = func.find_all('div', class_='white-desk ico-card')
    for item in ico_list:
        name = item.find('div', class_='ico-main-info').find("a").text
        link = item.find('div', class_='ico-main-info').find("a").get('href')
        category_coin = item.find('div', class_='ico-category-name').text
        received = item.find('span', class_='green').text
        interest = item.find('div', class_='interest').text
        invisted_pull = item.find('div', id='new_column_categ_invisted').find('span').text
        goal = item.find('div', id='categ_desctop').find('span').text
        date_active = item.find('div', class_='date active').text

        # if "Not Rated" in interest:
        #     print(interest)

        final_info[name] = {
            "link": link,
            "category_coin": category_coin,
            "received": received,
            "interest": interest,
            "invisted_pull": invisted_pull,
            "goal": goal,
            "date_active": date_active
                    }
    return final_info


result = all_info(get_info(url))






