from core.webCrwal import *
from core.oai import *


class Start:

    def __init__(self):
        self.gettext = GetData()
        self.process_test = PydenAnalytics() 


    def tag_data(self , url):
        raw_text = self.gettext.extract_data(url)
        if raw_text:
            output_data = self.process_test.genrate_response(raw_text)
            return output_data
        else:
            return f"don't recive any text {raw_text}"

if __name__ == "__main__":
    print('done')
