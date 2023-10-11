import requests
import json

class air_quality():
    # 查询城市aqi信息，并提供aqi信息输出接口
    
    def __init__(self):
        # 初始化request信息
        self.__api_url = "https://api.waqi.info/feed/"
        self.__api_token = "/?token=db0f0b8ab15f254faef565b9392003fd2f7d9216"
        self.__request_hearders = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
                                 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'}
        
    def info_get(self,city:str = "beijing"):
        # 查询某地aqi信息,默认查询北京
        self.__api_city = city
        response = requests.get(self.__api_url+self.__api_city+self.__api_token,headers=self.__request_hearders)
        result = json.loads(response.text)
        # 判断查询是否成功
        if result['status'] == "ok" :
            self.__data = result['data']
            print(self.__data)
            return True
        else :
            return False

if __name__ == "__main__" :
    # 测试
    test1 = air_quality()
    print(test1.info_get("tianjin"))