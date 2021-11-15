import requests
import argparse
import shlex

def _main():
    parser = argparse.ArgumentParser()
    parser.add_argument("url", type=str, help='url path')
    #args = parser.parse_args(shlex.split('-h'))
    args = parser.parse_args(shlex.split('http://127.0.0.1:8080/json'))
    
    s = requests.session()
    requests.utils.add_dict_to_cookiejar(s.cookies, {"cookies_key": "cookies_val"})
    rsp = s.get("http://127.0.0.1:8080/login")
    print(rsp)
    rsp = s.post("http://127.0.0.1:8080/login", data={
        "username": "xiaol-luo",
        "password": "xiaolzz"
    })
    print("cookies", rsp.cookies)
    print(rsp.text)



if __name__ == "__main__":
    _main()