import calc_sign
import time
import requests

class Project:
    def __init__(self) -> None:
        self.params = {}
        self.timestamp = int(time.time() * 1000)
        self.headers = {
            'cookie': '',
            'origin': 'https://ticket.hangzhou2022.cn',
            'pragma': 'no-cache',
            'referer': 'https://ticket.hangzhou2022.cn/',
            'sec-ch-ua': '"Chromium";v="21", " Not;A Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'sign': '',
            'site': 'pc',
            'siteversion': 'standard',
            'timestamp': '',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
        }
    
    def setCookie(self, cookie):
        self.headers['cookie'] = cookie

    def setParams(self, params, ts = int(time.time() * 1000)):
        def params2json(params):
            data = {}
            for pair in params.split('&'):
                key, value = pair.split('=')
                data[key] = value
            return data
        self.params = params
        self.timestamp = ts
        self.headers['timestamp'] = str(self.timestamp)
        self.headers['sign'] = calc_sign.calc_sign(params2json(self.params), self.timestamp)
    
    def query(self, params):
        self.setParams(params)
        url = 'https://gtpapi.hangzhou2022.cn/rest/guide/project/detail/query'
        res = requests.get(url, headers=self.headers, params=self.params).json()
        return res

    def queryList(self, params):
        self.setParams(params)
        url = 'https://gtpapi.hangzhou2022.cn/rest/guide/project/list/queryList'
        res = requests.get(url, headers=self.headers, params=self.params).json()
        return res

for i in range(2, 4):
    res = Project().queryList(f"sortType=2&page=1&pageSize=36&projectTypeId=2312007&langType=1")

    for project in res["data"]["projectPager"]["dataList"]:
        try:
            print(project["projectName"], project["cityName"], project["venueName"])
            time.sleep(3)
            res_price = Project().query(f"projectId={project['projectId']}&langType=1")
            
            for event in res_price["data"]["eventList"]:
                flag_price = 0
                for price in event["priceList"]:
                    if price["soldOut"] == True:
                        continue
                    print("席位", price["priceName"], "价格", price["price"], f"https://ticket.hangzhou2022.cn/#/game/selectSeat?projectId={project['projectId']}&eventId={event['eventId']}&priceId={price['priceId']}")
                    flag_price = 1
                    flag_project = 1
                if flag_price == 1:
                    print(event["eventName"])
        except Exception as e:
            print(res_price)
            print(f"出现错误: {e}")
            continue
