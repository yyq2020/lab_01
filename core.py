import requests
import json

class air_quality():
    # Query the AQI information of the city and provide the AQI information output interface
    
    def __init__(self):
        # Initialize the request information
        self.api_url = "https://api.waqi.info/feed/"
        self.api_token = "/?token=db0f0b8ab15f254faef565b9392003fd2f7d9216"
        self.request_hearders = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
                                 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'}
        
    def info_get(self,city:str):
        # Query the AQI information of a certain place, and query Beijing by default
        self.api_city = city
        response = requests.get(self.api_url+self.api_city+self.api_token,headers=self.request_hearders)
        result = json.loads(response.text)
        # Determines whether the query is successful
        if result['status'] == "ok" :
            # aqi
            self.data_aqi_current = result['data']['aqi']

            # data source
            self.data_source_organization = result['data']['attributions'][0]['name']
            self.data_source_url = result['data']['attributions'][0]['url']

            # city
            self.data_city_name = result['data']['city']['name']
            self.data_city_location = result['data']['city']['geo']

            # weather
            try:
                self.data_humidity_current = result['data']['iaqi']['h']['v']
            except KeyError:
                self.data_humidity_current = -1
            
            try:
                self.data_pressure_current = result['data']['iaqi']['p']['v']
            except KeyError:
                self.data_pressure_current = -1

            try:
                self.data_t_current = result['data']['iaqi']['t']['v']
            except KeyError:
                self.data_t_current = -1

            try:
                self.data_wind_current = result['data']['iaqi']['w']['v']
            except KeyError:
                self.data_wind_current = -1
            
            # pollution
            try:
                self.data_co_current = result['data']['iaqi']['co']['v']
            except KeyError:
                self.data_co_current = -1
            
            try:
                self.data_no2_current = result['data']['iaqi']['no2']['v']
            except KeyError:
                self.data_no2_current = -1
            
            try:
                self.data_o3_current = result['data']['iaqi']['o3']['v']
            except KeyError:
                self.data_o3_current = -1
            
            try:
                self.data_so2_current = result['data']['iaqi']['so2']['v']
            except KeyError:
                self.data_so2_current = -1
            
            try:
                self.data_pm25_current = result['data']['iaqi']['pm25']['v']
            except KeyError:
                self.data_pm25_current = -1
            
            try:
                self.data_pm10_current = result['data']['iaqi']['pm10']['v']
            except KeyError:
                self.data_pm10_current = -1
            

            # global time
            self.data_time_current = result['data']['time']['iso']

            # forecast and history
            self.data_date_long = [i['day'] for i in result['data']['forecast']['daily']['pm10']]
            self.data_pm10_avg_long = [i['avg'] for i in result['data']['forecast']['daily']['pm10']]
            self.data_pm10_max_long = [i['max'] for i in result['data']['forecast']['daily']['pm10']]
            self.data_pm10_min_long = [i['min'] for i in result['data']['forecast']['daily']['pm10']]
            self.data_pm25_avg_long = [i['avg'] for i in result['data']['forecast']['daily']['pm25']]
            self.data_pm25_max_long = [i['max'] for i in result['data']['forecast']['daily']['pm25']]
            self.data_pm25_min_long = [i['min'] for i in result['data']['forecast']['daily']['pm25']]
            self.data_avg_o3 = [i['avg'] for i in result['data']['forecast']['daily']['o3']]
            self.data_max_o3 = [i['max'] for i in result['data']['forecast']['daily']['o3']]
            self.data_min_o3 = [i['min'] for i in result['data']['forecast']['daily']['o3']]

            return True
        
        else :
            return False

def aqi_classify(aqi:int):
    aqi_level = ["Good(优)","Moderate(良)","Unhealthy for Sensitive Groups(轻度污染)",\
                 "Unhealthy(中度污染)","Very Unhealthy(重度污染)","Hazardous(严重污染)"]
    if 0 <= aqi and aqi<= 50:
        return aqi_level[0]
    elif 50 < aqi and aqi<= 100:
        return aqi_level[1]
    elif 100 < aqi and aqi<= 150:
        return aqi_level[2]
    elif 150 < aqi and aqi<= 200:
        return aqi_level[3]
    elif 200 < aqi and aqi<= 300:
        return aqi_level[4]
    else :
        return aqi_level[5]


if __name__ == "__main__" :
    # Test
    test1 = air_quality()
    test1.info_get("hefei")
    print(test1.data_pm10_avg_long)