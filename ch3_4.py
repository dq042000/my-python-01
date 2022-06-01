from cgitb import html
import requests

url = 'http://www.google.com/'
htmlfile = requests.get(url)
if htmlfile.status_code == requests.codes.ok:
  print('取得網頁內容成功')
  print('網頁內容大小：', len(htmlfile.text))
else:
  print('取得網頁內容失敗')

print(htmlfile.text)