# coding:UTF-8
import json
import unittest
from compiler.ast import Assert

import requests

server_url = 'http://api.olavoice.com/olaweb/webvoice/api/ask'


def getResponse(question):
    param = '''{
    "data_type": "stt",
    "data": {
        "text": "''' + question + '''",
        "location": {
            "position_type": "0",
            "is_last": "1",
            "street": "天潼路",
            "province": "上海市",
            "longitude": 121481332,
            "number": "619号",
            "latitude": 31243361,
            "district": "闸北区",
            "city": "上海市"
        },
        "force_slot_reply": 0,
        "input_type": 1
    }
}'''
    data = {
        'appid': (None, '0B647B01-1BAF-4EE2-8165-239752A3B76F'),
        'cusid': (None, 'abc123'),
        'rq': (None, param)
    }
    response = requests.request("POST", server_url, data=data)
    rs = json.loads(response.content)
    return rs

