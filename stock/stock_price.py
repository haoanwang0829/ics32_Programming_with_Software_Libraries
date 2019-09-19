import json
import urllib.parse
import urllib.request
import xlwt
from datetime import datetime
index_cate = ['日期','开盘价','最高价','收盘价','最低价','量','涨跌额','涨跌幅','5日均价','10日均价','20日均价','5日均量','10日均量','20日均量','换手率']

type_input = ''

BASE_STOCK_URL = 'http://api.finance.ifeng.com/'

def get_data():
    stock_num = input()
    stock_type = input()
    if stock_type == 'm':
        type_input = 'akmonthly'
    elif stock_type == 'w':
        type_input = 'akweekly'
    elif stock_type == 'd':
        type_input = 'akdaily'
    query_parameters = [('code', stock_num), ('type', 'last')]
    data_type = '{}/?'.format(type_input)
    url = BASE_STOCK_URL  + data_type + urllib.parse.urlencode(query_parameters)

    response = urllib.request.urlopen(url)
    json_text = response.read().decode(encoding = 'ascii')
    json_result = json.loads(json_text)['record']
    
    
    
    
    wb = xlwt.Workbook()
    ws = wb.add_sheet('{}'.format(stock_num))
    for k, index in enumerate(index_cate):
        ws.write(0, k, index)
    for i, his in enumerate(json_result):
        for j, info in enumerate(his):
            ws.write(i+1, j, info)

    wb.save('{},{}.xls'.format(stock_num,stock_type))



if __name__ == '__main__':
    get_data()


    



        
