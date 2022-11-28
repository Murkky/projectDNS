import datetime


class Base:
    def __init__(self, driver):
        self.driver = driver

    # Method get current URL
    def get_current_url(self):
        get_url = self.driver.current_url
        print(f'Current URL {get_url}')

    # Method assert word
    def assert_word(self, word, result):
        assert word == result
        print('Good Value Word')

    # Method Screenshot
    def screenshot(self):
        now_date = datetime.datetime.utcnow().strftime(" %Y.%m.%d, %H.%M")
        name_screenshot = 'screenshot' + now_date + '.png'
        self.driver.save_screenshot('.\\screen\\' + name_screenshot)

    # Method assert current URL
    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print('Good Value URL')
