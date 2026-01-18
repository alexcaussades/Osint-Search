import argparse
import json
import sys
import requests



def get_geo_ip_info(ip_address):
    try:
        apiURL = "http://ip-api.com/json/" + ip_address
        response = requests.get(apiURL)
        if response.status_code == 200:
            data = response.json()
            if data['status'] == 'success':
                print("Geo IP Information:")
                ip_loc = {
                    'ip': data['query'],
                    'country': data["country"],
                    'region': data["regionName"],
                    'city': data["city"],
                    'zip': data["zip"],
                    'lat': data["lat"],
                    'lon': data["lon"],
                    'isp': data["isp"],
                    'org': data["org"],
                    'as': data["as"]
                }
                return ip_loc['ip'], ip_loc['country'], ip_loc['region'], ip_loc['city'], ip_loc['zip'], ip_loc['lat'], ip_loc['lon'], ip_loc['isp'], ip_loc['org'], ip_loc['as']
            else:
                return {'error': f"Error from API: {data.get('message', 'Unknown error')}"}
        else:
            return {'error': f"HTTP Error: {response.status_code}"}
    except requests.RequestException as e:
        return {'error': str(e)}
    

get_geo_ip_info("88.177.21.65")