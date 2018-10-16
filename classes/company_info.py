import requests, sys

class Info:
    def __init__(self):
        return

    def get_summary(self, symbol, stock_url):
        summary_url_list = []
        try:
            response = requests.get(stock_url + symbol + '/news/last/10')
            json = response.json()

            for row in json:
                if row['summary'] == 'No summary available.':
                    continue
                summary_url_list.append([ row['summary'] , row['url'] ])
            return summary_url_list

        except Exception as e:
            print (str(e))

    def get_company_name(self, symbol, stock_url):
        try:
            response = requests.get(stock_url + symbol + '/company')
            json = response.json()
            return json['companyName']
        except Exception as e:
            print (str(e))

    def get_exchange(self, symbol, stock_url):
        try:
            response = requests.get(stock_url + symbol + '/company')
            json = response.json()
            return json['exchange']
        except Exception as e:
            print (str(e))