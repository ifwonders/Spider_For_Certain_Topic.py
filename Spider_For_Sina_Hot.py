# 2023-10-19

import requests
from bs4 import BeautifulSoup

import xlwt
import datetime

import prefech

headers = prefech.getcookie()

# 携带Cookie访问新浪微博热搜榜 防止重定向
main_url = "https://s.weibo.com/top/summary"

main_response = requests.get(url=main_url, headers=headers)
# 用BS库解析返回的热搜榜html文件
soup = BeautifulSoup(main_response.text, 'html.parser')
# 利用词条特点筛选出top50榜单
top50_list = soup.find_all('a', target="_blank")

# 制作xls文件
xls = xlwt.Workbook()
sheet1 = xls.add_sheet(sheetname=f"{datetime.date.today()}")

sheet1.write(0, 0, "热搜排名")
sheet1.write(0, 1, "话题")
sheet1.write(0, 2, "链接")

for rank in range(0, 51):
    if rank == 0:
        sheet1.write(rank + 1, 0, "顶置热搜")
    else:
        sheet1.write(rank + 1, 0, f"热搜第{rank}")
    sheet1.write(rank + 1, 1, str(top50_list[rank].text))
    sheet1.write(rank + 1, 2, f"https://s.weibo.com{top50_list[rank].get('href')}")

xls.save("D:\\wang\\Desktop\\Sina_Hot.xls")
