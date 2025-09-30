import json
from API.ApiUtils import API
from Actions.schema import QueryGoodsStockDto
from Actions.Common import Common

api = API()
common = Common()


def test_query_goods_stock(load_base_url, get_test_name):
    api_url = "/QueryGoodsStockDto"
    payload = json.dumps({
        "goodsCode": "TP77777990000002"
    })

    response, _api_list = api.send_request(
        "post",
        base_url=load_base_url,
        api_url=api_url,
        access_token=None,
        parameters="",
        payload=payload
    )

    assert response.status_code == 200
    common.schema_checker(data=response.json(), schema=QueryGoodsStockDto)
    common.write_to_folder(response=response, api_url=api_url, test_name=get_test_name, write_option=False)
