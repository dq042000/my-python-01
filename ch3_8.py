import requests
import re

url = 'http://www.mcut.edu.tw'
htmlfile = requests.get(url)

if htmlfile.status_code == requests.codes.ok:
  pattern = input('請輸入欲搜尋的字串：')
  
  if pattern in htmlfile.text:
    print('搜尋 %s 成功' % pattern)
  else:
    print('搜尋 %s 失敗' % pattern)
  
  name = re.findall(pattern, htmlfile.text)
  if name != None:
    print('%s 出現 %d 次' % (pattern, len(name)))
  else:
    print('%s 出現 0 次' % pattern)
else:
  print('網頁下載失敗')