import json
import configparser


class Common:
    def load_base_url(self):
        config = configparser.ConfigParser()
        config.read(r"config.txt")
        return config.get('MOMO_LOGIN_PAGE', 'api_url')

    def load_openai_api_token(self):
        config = configparser.ConfigParser()
        config.read(r"config.txt")
        return config.get('OPENAI_API_TOKEN', 'GITHUB_TOKEN')

    def write_to_folder(self, response, api_url, parameters=None, write_option=False, test_name="None"):
        content_type = response.headers.get("Content-Type", "")
        if "application/json" in content_type:
            if write_option is True:
                api_url = api_url.replace("/", "_")
                request_method = response.request.method
                format_test_name = f"({test_name})"
                if parameters is not None:
                    parameters = parameters.replace("/", "_")
                    parameters = parameters.replace("?", "_")
                    with open('test/csv/' + api_url[1:] + format_test_name + '(' + request_method + ')(' + str(response.status_code) + ')' + str(parameters) + '.json', 'w') as f:
                        json.dump(response.json(), f)
                else:
                    with open('test/csv/' + api_url[1:] + format_test_name + '(' + request_method + ')(' + str(response.status_code) + ')' + '.json', 'w') as f:
                        json.dump(response.json(), f)

    def schema_checker(self, data, schema):
        schema.model_validate(data)
