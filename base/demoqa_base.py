from playwright.sync_api import Browser, expect
from support.logger import log_method
import logging as log

import os



class DemoQa():
    log = log_method()

    def __init__(self, browser: Browser, url='https://demoqa.com'):
        self.base_url = url
        self.browser = browser
        self.context = self.browser.new_context()
        self.page = self.context.new_page()
        self.page.set_default_navigation_timeout(60000)

    def open_demoqa(self):
        self.page.goto(self.base_url)
        log.info(f'{self.base_url} opened')



