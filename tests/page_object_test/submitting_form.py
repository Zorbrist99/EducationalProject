from selene import browser, have, be

class StudentSubmittingForm:

    def __init__(self):
        self.submit_form = '#example-modal-sizes-title-lg'
        self.content_form = '.table-dark'

    def check_heading_form(self, value):
        browser.element(self.submit_form).should(have.text(value)).should(be.visible)
        return self

    def check_content_form(self, value):
        browser.element(self.content_form).should(have.text(value)).should(be.visible)
        return self