import requests


class API:
    def __init__(self):
        self._session = requests.Session()  # 初始化時建立單一 `Session`

    def session(self):
        return self._session  # 所有 API 呼叫都會使用同一個 `Session

    def send_request(self, method, base_url, access_token=None, api_url="", parameters="", payload=None):
        url = base_url + api_url + parameters
        headers = {
            "Accept": "application/json"
        }
        if access_token:
            headers["Authorization"] = f"{access_token}"
        response = self.session().request(method, url, headers=headers, data=payload)

        if response.status_code == 200:
            pass
        elif response.status_code == 503:
            print("⚠️ API 503, server overload...")
        elif response.status_code == 409:
            pass
        else:
            assert response.status_code == 200, f"Request failed: {response.status_code}, {response.text}"
        return response, [api_url, parameters]
