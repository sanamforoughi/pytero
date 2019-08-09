import requests


class NateroClient:
    """Client for interacting with Natero via `requests`-style API calls
    """

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
        self.cache = {}
        if self.base_url is None:
            raise Exception(
                'Invalid Natero region, valid options include: us, eu')

    def get(self, endpoint, params=None):
        req_url = '{}{}'.format(self.base_url, endpoint)
        if params is None:
            params = {}
        return requests.get(req_url, params={**params, **self.base_params}, headers=self.base_headers)

    def post(self, endpoint, data=None, params=None):
        req_url = '{}{}'.format(self.base_url, endpoint)
        return requests.post(req_url, data=data, params={**params, **self.base_params}, headers=self.base_headers)

    def accounts(self, order_by='account_id', direction='desc', page=0, include_inactive=False, include=None, raw=False, use_cache=True):
        if self.cache.get('accounts'):
            return self.cache.get('accounts')
        req = self.get('accounts', params={
            'order_by': order_by,
            'direction': direction,
            'page': page,
            'include_inactive': include_inactive,
            'include': ','.join(str(include))
        })
        self.cache['accounts'] = req.json().get('results')
        return req if raw else self.cache['accounts']

    def accounts_iter(self, order_by='account_id', direction='desc', include_inactive=False, include=None):
        page, index = 0, None
        while index is None or index == 1000:
            buffer = self.accounts(
                order_by=order_by,
                direction=direction,
                page=page,
                include_inactive=include_inactive,
                include=include
            )
            index = 0
            while index < len(buffer):
                yield buffer[index]
                index += 1

    def account_users(self, id, order_by='user_id', direction='desc', page=0, include_inactive=False, raw=False, use_cache=True):
        if self.cache.get('account_users'):
            return self.cache.get('account_users')
        
        endpoint = 'accounts/{}/users'.format(id)
        req = self.get(endpoint, params={
            'order_by': order_by,
            'direction': direction,
            'page': page,
            'include_inactive': include_inactive
        })
        self.cache['account_users'] = req.json().get('results')
        return req if raw else self.cache['account_users']

    def account_users_iter(self, id, order_by='user_id', direction='desc', page=0, include_inactive=False):
        page, index = 0, None
        while index is None or index == 1000:
            buffer = self.account_users(
                id,
                order_by=order_by,
                direction=direction,
                page=page,
                include_inactive=include_inactive
            )
            index = 0
            while index < len(buffer):
                yield buffer[index]
                index += 1

    def account(self, id):
        endpoint = 'accounts/{}'.format(id)
        return self.get(endpoint)
