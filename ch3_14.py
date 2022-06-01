from difflib import HtmlDiff
import requests

url = 'https://romspure.cc/roms/nintendo-game-boy'
try:
  htmlfile = requests.get(url)
  print('下載成功')
except Exception as err:
  print('網頁下載失敗： %s' % err)

fn = 'out3_14.txt'
with open(fn, 'wb') as file_Obj:
  for diskStorage in htmlfile.iter_content(40960):
    size = file_Obj.write(diskStorage)
    print(size)
  print('以 %s 儲存網頁HTML檔案成功' % fn)