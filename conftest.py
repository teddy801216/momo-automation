import pytest
from Actions.Common import Common

common = Common()


@pytest.fixture(scope='function')
def load_base_url():
    base_url = common.load_base_url()
    return base_url


@pytest.fixture(scope='function')
def get_test_name(request):
    return request.node.name
