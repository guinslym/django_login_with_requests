import requests
import pprint
from bs4 import BeautifulSoup
#try selenium

# Fill in your details here to Sbe posted to the login form.
payload = {
    'next': '/admin/',
    'password':'(famille)',
    'username':'admin'
}

# Use 'with' to ensure the session context is closed after use.
with requests.Session() as s:
    pr = s.get('http://localhost:8000/admin/login/?next=/admin/')
    # print the html returned or something more intelligent to see if it's a successful login page.
    soup = BeautifulSoup(pr.content, 'lxml')
    token = soup.find_all('input')[0]['value']
    payload['csrfmiddlewaretoken'] = token
    # print (pr.text)

    # An authorised request.
    import pdb;pdb.set_trace()
    resp = s.post('http://localhost:8000/admin/login/', data=payload)
    # print (resp.text)

        # etc...
    f = open("result.html", "w")
    content = str(resp.content)
    f.write(content)
    f.close()
