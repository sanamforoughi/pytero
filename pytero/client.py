import requests


class NateroClient:

    api_hosts = {
        'us': 'https://api.natero.com/api/v2/',
        'eu': 'https://api-eu.natero.com/api/v2/'
    }

    base_headers = {
        'Content-Type': 'application/json',
        'charset': 'utf-8'
    }

    def __init__(self, api_key, region='us', base_params={}):
        self.api_key = api_key
        self.base_params = {'api_key': self.api_key, **base_params}
        self.base_url = self.api_hosts.get(region)
        if self.base_url is None:
            raise Exception('Invalid Natero region, valid options include: us, eu')

    def get(self, endpoint, params=None):
        req_url = '{}{}'.format(self.base_url, endpoint)
        if params is None:
            params = {}
        return requests.get(req_url, params={**params, **self.base_params}, headers=self.base_headers)

    def post(self, endpoint, data=None, params=None):
        req_url = '{}{}'.format(self.base_url, endpoint)
        return requests.post(req_url, data=data, params={**params, **self.base_params}, headers=self.base_headers)

    def accounts(self, order_by='account_id', direction='desc', page=0, include_inactive=False, include=None, raw=False):
        req = self.get('accounts', params={
            'order_by': order_by,
            'direction': direction,
            'page': page,
            'include_inactive': include_inactive,
            'include': ','.join(str(include))
        })
        return req if raw else req.json().get('records')

    def accounts_iter(self, order_by='account_id', direction='desc', include_inactive=False, include=None):
        page, index = 0, None
        while index is None or index == 1000:
            buffer = self.accounts(order_by, direction, page, include_inactive, include)
            index = 0
            while index < len(buffer):
                yield buffer[index]

    def account(self, id):
        endpoint = 'accounts/{}'.format(id)
        return self.get(endpoint)
