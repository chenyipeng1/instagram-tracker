import requests

url = 'https://hypeauditor.com/'
login_email = 'chenyp@umich.edu'
login_password = 'cyp123456dfdfa'
# 创建一个session,作用会自动保存cookie
session = requests.session()
data = {
    'login_email': login_email,
    'login_password': login_password
}
# 使用session发起post请求来获取登录后的cookie,cookie已经存在session中
response = session.post(url = url,data=data)

print(response)
# # 用session给个人主页发送请求，因为session中已经有cookie了
# index_url = 'https://hypeauditor.com/en/top-instagram/?p=2'
# index_page = session.get(url=index_url).text
# print(index_page)