import requests


class NateroClient:

    api_hosts = {
        "us": "https://api.natero.com/api/v2/",
        "eu": "https://api-eu.natero.com/api/v2/"
    }

    error_messages = {
        "invalid_region": "Invalid region identifier, valid options include 'us' and 'eu'."
    }

    def __init__(self, api_key, region="us", base_params={}):
        self.api_key = api_key
        self.base_params = {self.api_key, **base_params}
        self.base_url = self.api_hosts.get(region)
        if self.base_url is None:
            raise Exception(self.error_messages["invalid_region"])

    def get(self, endpoint, params=None):
        req_url = "{}{}".format(self.base_url, endpoint)
        return requests.get(req_url, params={**params, **self.base_params})

    def post(self, endpoint, data=None, params=None):
        req_url = "{}{}".format(self.base_url, endpoint)
        return requests.post(req_url, data=data, params={**params, **self.base_params})

    def accounts(self, order_by="account_id", direction="desc", page=0, include_inactive=False, include=None):
        return self.get("accounts", params={
            "order_by": order_by,
            "direction": direction,
            "page": page,
            "include_inactive": include_inactive
            "include": ",".join(str(include))
        })

    def account(self, id):
        endpoint = "accounts/{}".format(id)
        return self.get(endpoint)
