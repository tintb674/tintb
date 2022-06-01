import requests
import json


def get_inven_org():
    organizationId = '681155'
    url = f'https://api.meraki.com/api/v1/organizations/{organizationId}/inventory/devices'
    header = {
        'X-Cisco-Meraki-API-Key': '6bec40cf957de430a6f1f2baa056b99a4fac9ea0'
    }
    response = requests.get(url, headers=header)
    r = response.json()
    # print(json.dumps(r, indent=4))
    num = len(r)
    for i in range(num):
        network = r[i]['networkId']
        if network is None:
            print(json.dumps(r[i], indent=4))


get_inven_org()

