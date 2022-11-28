from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        s = self.path
        url_components = parse.urlsplit(s)
        query_string_list = parse.parse_qsl(url_components.query)
        dic = dict(query_string_list)

        if 'country' in dic:
            url = 'https://restcountries.com/v2/name/'
            r = requests.get(url + dic['country'])
            data = r.json()
            country = data[0]['name']
            capital = data[0]['capital']
            message = f'The capital of {country} is {capital}.'

        elif "capital" in dic:
            url = 'https://restcountries.com/v2/capital/'
            r = requests.get(url + dic["capital"])
            data = r.json()
            country = data[0]['name']
            capital = data[0]['capital']
            message = f'{capital} is the capital of {country}.'

        else:
            message = 'Error. Invalid Request.'

        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(message.encode())
        return
