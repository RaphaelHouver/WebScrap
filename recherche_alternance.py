import requests
from bs4 import BeautifulSoup
import payload

login_url = ("https://epita.net/node?destination=/node")
jobteaser_url = ("https://epita.jobteaser.com/")
origin_url = "https://epita.net"
offres_path = "fr/job-offers"
dashboard_path = "fr/dashboard"

payload = {
    "name": payload.name,
    "pass": payload.password,
    "form_build_id": "form-uIq4OKqKeQNFBk9WXFgNuhO7hZ-0M9kZGD4uIFmtBZI",
    "form_id": "user_login_form",
    "op": "Se connecter"
}

HEADERS_login = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36",
    "origin": origin_url,
    "referer": origin_url + "/"
}

HEADERS_jobteaser = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36",
    "referer": "https://epita.jobteaser.com/users/jobteaser_auth/process?message=rQ3n9pdUdLnAuRZwhp70wuP0aqLr8ziCeJw6gVWFObe7BSE5TFvzY5twh8hId64TLB4yqK1yEY%2FbEIeXzyAvlYWJipI7eSWVt7aM0NsKpnjFgo04Bzl7O3t50%2F9sINbjFmCBKc2gCcroq%2FEiG0peH%2FuhvZRSTONHVXU7LaXLGoc%3D&iv=0ipyU2DQXGbzan%2BEJdK%2F7g%3D%3D"
}


with requests.session() as s:
    login_request = s.post(login_url, headers = HEADERS_login, data=payload)

    jobteaser_request = s.get(origin_url + dashboard_path, headers = HEADERS_jobteaser)

    soup = BeautifulSoup(jobteaser_request.text, "html.parser")
    

    
    print(jobteaser_request.status_code)
    print(soup.prettify())

