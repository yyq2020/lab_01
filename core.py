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
        
    def info_get(self,city:str = "beijing"):
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
            self.data_humidity_current = result['data']['iaqi']['h']['v']
            self.data_pressure_current = result['data']['iaqi']['p']['v']
            self.data_t_current = result['data']['iaqi']['t']['v']
            self.data_wind_current = result['data']['iaqi']['w']['v']

            # pollution
            self.data_co_current = result['data']['iaqi']['co']['v']
            self.data_no2_current = result['data']['iaqi']['no2']['v']
            self.data_o3_current = result['data']['iaqi']['o3']['v']
            self.data_so2_current = result['data']['iaqi']['so2']['v']
            self.data_pm25_current = result['data']['iaqi']['pm25']['v']
            self.data_pm10_current = result['data']['iaqi']['pm10']['v']

            # time
            self.data_time_current = result['data']['time']['s']

            # forecast and history
            self.data_pm10_long = result['data']['forecast']['daily']['pm10']
            self.data_pm25_long = result['data']['forecast']['daily']['pm25']
            self.data_o3 = result['data']['forecast']['daily']['o3']

            return True
        
        else :
            return False

if __name__ == "__main__" :
    # Test
    test1 = air_quality()
    test1.info_get("hefei")