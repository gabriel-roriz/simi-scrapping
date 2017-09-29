from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

class Simi:
    def __init__(self, driver):
        self.driver = driver
        self.url = 'http://www.simi.org.br/'
        self.all_news = 'all-news' # class
        self.more_news = 'row more-news' # class

        self.news = []

    def navigate(self):
        self.driver.get(self.url)

    def _get_all_news(self):
        return self.driver.find_element_by_class_name(self.all_news)

    def _get_rows(self):
        return (self._get_all_news().find_element_by_tag_name('div')).find_elements_by_class_name('row')

    def _get_itens_by_row(self, row):
        cols = row.find_elements_by_class_name('col-xs-12')
        for news in cols:
            try:
                dic = {'title': news.find_element_by_tag_name('p').text,
                        'link': news.find_element_by_class_name('item').get_attribute("href"),
                        'resume': news.find_element_by_class_name('resume').text,
                        'image': ''}

                self.news.append(dic)

            except NoSuchElementException:
                print('')

    def get_news(self):
        rows = self._get_rows()
        for row in rows:
            self._get_itens_by_row(row)


ff = webdriver.Firefox()
simi = Simi(ff)
simi.navigate()
simi.get_news()

print(simi.news)
