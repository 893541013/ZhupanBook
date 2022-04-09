import requests
import pytest

@pytest.fixture(scope='function')
def user_login():
    u = "http://haimo.testgoup.com/haimo/sass/systemUser/release/getLogin"
    d = {"userName":"admin","password":"e10adc3949ba59abbe56e057f20f883e"}
    res = requests.post(url=u,json = d)
    assert res.status_code == 200
    assert res.json()["code"] == 1

    return res.json()["data"][0]["token"]

    