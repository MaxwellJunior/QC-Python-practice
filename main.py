import requests

session = requests.Session()
headers = {'Content-Type': 'application/x-www-form-urlencoded'}
login_url = 'https://login.software.microfocus.com/msg/actions/doLogin.action'
data = {'username': 'MaxwellAdilez@gmail.com', 'password': 'password'}
resp = session.post(url=login_url, data=data, headers=headers)
print(requests.utils.dict_from_cookiejar(session.cookies)['LWSSO_COOKIE_KEY'])

d = requests.utils.dict_from_cookiejar(session.cookies)
session_url = 'https://almalmqc1250saastrial.saas.hpe.com/qcbin/rest/site-session'
LWSSO = d.get('LWSSO_COOKIE_KEY')
d1 = {'LWSSO_COOKIE_KEY': d.get('LWSSO_COOKIE_KEY')}
resp = requests.post(session_url, cookies=requests.utils.cookiejar_from_dict(d1))
print("Site-session resposne cookies %s" % resp.cookies)
print("rest/site-session response code: %s  " % resp.status_code)
QCSession = resp.cookies.get('QCSession')
XSRF_TOKEN = resp.cookies.get('XSRF-TOKEN')
print(QCSession + '\n' + XSRF_TOKEN + '\n' + session_url)
