import requests
from bs4 import BeautifulSoup

login_url = ("https://epita.net/node?destination=/node")
secure_url = ("https://epita.jobteaser.com/fr/job-offers")

payload = {
    "name": "raphael.houver@epita.fr",
    "pass": "wjp57KcV&E9%h!Mi",
    "form_build_id": "form-uIq4OKqKeQNFBk9WXFgNuhO7hZ-0M9kZGD4uIFmtBZI",
    "form_id": "user_login_form",
    "op": "Se connecter"
}

with requests.session() as s:
    login_request = s.post(login_url, data=payload)
    soup = BeautifulSoup(s.get(login_url).text, "html.parser")
    
    print(login_request.status_code)
    print(soup.prettify())