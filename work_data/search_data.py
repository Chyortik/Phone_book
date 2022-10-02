# модуль поиска контакта

from work_data.export_data import export_data
from printing.print_data import print_data

def search_data(word, data):
    if len(data) > 0:
        for item in data:
            if word in item:
                return item
    else:
        return None