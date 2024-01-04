import os
import requests
from requests.auth import HTTPBasicAuth

import endpoints
import payloads


class Client:
    def __init__(self):
        self.host = os.getenv("HOST_AI")
        self.basic_user = os.getenv("BASIC_USER")
        self.basic_pass = os.getenv("BASIC_AI_PASS")

    def _request(self, path, params, payload, method):
        url = os.path.join(self.host, path)
        if method == "get":
            return self._get(url=url, params=params)
        elif method == "post":
            return self._post(url=url, payload=payload)

    def _get(self, url, params):
        return requests.get(
            headers=None,
            url=url,
            auth=HTTPBasicAuth(username=self.basic_user, password=self.basic_pass),
            params=params
        )

    def _post(self, url, payload):
        return requests.post(
            headers=None,
            url=url,
            json=payload,
            auth=HTTPBasicAuth(username=self.basic_user, password=self.basic_pass),
        )

    def inference(self, model_id):
        return self._request(
            path=endpoints.inference(model_id=model_id),
            params=None,
            payload=payloads.inference,
            method="post",
        )

    def train_by_mode(self):
        return self._request(
            path=endpoints.train_by_mode(),
            params=None,
            payload=payloads.train_by_mode,
            method="post",
        )


def main():
    """
    # クライアントを作成
    client = Client(server_type="ai")

    # 学習(モデルを作成)
    r = client.train_by_mode

    # 推論(モデルの利用)
    r = client.inference(model_id=595)
    """
    client = Client()
    r = client.inference(model_id=599)
    # r = client.train_by_mode()
    print(r.status_code)
    print(r.json())


if __name__ == "__main__":
    main()
