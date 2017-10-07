import requests
from bs4 import BeautifulSoup

# Fill in your details here to Sbe posted to the login form.
payload = {
    'next': '/admin/',
    'password':'(famille)',
    'username':'admin1'
}

def get_the_csrftoken(webpage):
    #Parse the content of that page
    soup = BeautifulSoup(webpage, 'lxml')
    #Get the CSRF token
    token = soup.find_all('input')[0]['value']

    return token

def get_the_title(webpage):
    #Parse the content of that page
    soup = BeautifulSoup(webpage, 'lxml')
    #Get the CSRF token
    title = soup.find_all("h1")[1].text

    return title


def main():
    # Use 'with' to ensure the session context is closed after use.
    with requests.Session() as s:
        #Go to the login URL page
        admin_login_page = s.get('http://localhost:8000/admin/login/')

        #Parse the content of that page to retrieve the CSRF Token
        token = get_the_csrftoken(admin_login_page.content)
        #Add a new key to the Dictionnary
        payload['csrfmiddlewaretoken'] = token

        # Get to an authorised request. (that requires Admin)
        resp = s.post('http://localhost:8000/admin/login/', data=payload)

        title = get_the_title(resp.content)

        #Assert that I receive the right page content
        # assert 'Site administration' in title
        # print(title)
        return title

if __name__ == "__main__":
    title = main()
    print(title)
