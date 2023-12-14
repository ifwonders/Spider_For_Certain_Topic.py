# 2023-10-20
import prefech
import requests
from bs4 import BeautifulSoup
import xlwt
import datetime


# 为热点话题下的帖子创建一个类
class Post:
    # 一条帖子应该包含：特殊标签/发帖人/发帖时间与标记/发帖来源/发帖正文/转发数/评论数/点赞数
    # 特殊标签：顶置、热门  事件与标记：如 今天 18:03 转赞人数超过100
    def __int__(self, sp_label, poster, time, sp_mark, origin, text, retweets_num, comments_num, likes_num):
        self.sp_label = sp_label
        self.poster = poster
        self.time = time
        self.origin = origin
        self.text = text
        self.retweet_num = retweets_num
        self.comments_num = comments_num
        self.likes_num = likes_num


def dateList(begin_date, end_date):
    ord_begin = datetime.date.toordinal(begin_date)
    ord_end = datetime.date.toordinal(end_date)
    date_list = []
    for date in range(int(ord_begin), int(ord_end) + 1):
        date_list.append(datetime.date.fromordinal(date))

    return date_list


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/116.0.5845.97 Safari/537.36",
    "Cookie": "SINAGLOBAL=2851174343261.038.1696934649160; UOR=,,login.sina.com.cn; XSRF-TOKEN=S4Ocx_Xt0OYJ5Q43NpAnYUYJ; PC_TOKEN=dc64b7d803; login_sid_t=d172e145204961687aebd44b792ce7bf; cross_origin_proto=SSL; WBStorage=4d96c54e|undefined; _s_tentry=passport.weibo.com; wb_view_log=1920*10801; Apache=6929872306212.778.1701252598046; ULV=1701252598048:4:1:1:6929872306212.778.1701252598046:1698562814332; WBtopGlobal_register_version=2023112918; SUB=_2A25IY35cDeRhGeFJ41sV8ifOzTiIHXVrAf-UrDV8PUNbmtANLVn_kW9NfsqxfYdlaZjH0qzdlaox4QHS_JqVpLnu; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WhLS.XxHpR2AiNXxNiITuEV5JpX5KzhUgL.FoMN1h.Xeo.ESoB2dJLoIXnLxK.L1KeL1h2LxK.LBKqL1K.LxKBLB.zL122LxK-LBKBLBK.LxKBLBo.L1-qLxKnLBKqL1h2LxK-L1hqL1h-LxK-L12BLBoMt; ALF=1732788619; SSOLoginState=1701252620; WBPSESS=itv9JLRJGL_8jx8Djy3d8eef2gwLr3J2czwh9xk97Z_vzNoPWc9iWO_FqoLVoHV9hv5oJov1s3gfJ9bPS_ftsATcK6oRqESYczH3hjrWMNPuCSOwqeXF_e_8MC3RTj8aPRE3WDCnDlLHFaD0SYT25A=="}


url = (f"https://s.weibo.com/weibo?q=%23%E5%BC%A0%E5%B0%8F%E6%B3%89%E5%AE%A2%E6%9C%8D%E7%A7%B0%E8%8F%9C%E5%88%80%E4%B8%8D%E8%83%BD%E6%8B%8D%E8%92%9C%23&typeall=1&suball=1&timescope=custom")
       # "%3A{2023-10-29}%3A{2023-10-29}&{page=1}")

# 初始化表格文件
xls = xlwt.Workbook()

# 确定起始日期和结束日期
begin_date = datetime.date(2022, 7, 13)
end_date = datetime.date(2022, 7, 18)
date_list = dateList(begin_date, end_date)

# 按日期跨度建立sheet表
for date in date_list:
    print(date)
    # 初始化当前sheet表
    sheet1 = xls.add_sheet(sheetname=f"{date}")
    table_titles = ['特殊标签', '发帖人', '发帖时间与标记', '发帖来源', '发帖正文', '转发数', '评论数', '点赞数']
    for i in range(len(table_titles)):
        sheet1.write(0, i, table_titles[i])

    url_for_page = url + f"%3A{date}%3A{date}"
    response_for_page = requests.get(url=url_for_page,headers=headers)
    soup_for_page = BeautifulSoup(response_for_page.text,'html.parser')
    tmp_soup = soup_for_page.find('ul', attrs={"node-type":"feed_list_page_morelist"})
    try:
        page_limit = len(tmp_soup.find_all('li'))
    except:
        page_limit = 1

    row = 0
    for page in range(1, page_limit+1):
        main_url = url_for_page + f"&page={page}"

        main_response = requests.get(url=main_url, headers=headers)
        soup = BeautifulSoup(main_response.text, 'html.parser')

        cards_list = soup.find_all('div', attrs={"action-type": "feed_list_item"})

        # 每单条帖子都将数据存入实例类中

        for card in cards_list:
            row += 1
            column = 0
            # 创建实例
            post = Post()

            # 筛选特殊标签
            title = card.find('h4', attrs={"class": "title"})
            try:
                sp_mark = title.find('a')
                post.sp_mark = sp_mark.text
            except:
                post.sp_mark = ''
            sheet1.write(row, column, post.sp_mark)
            column += 1

            # 筛选发帖人
            name = card.find('a', class_="name")
            post.poster = name.text
            sheet1.write(row, column, post.poster)
            column += 1

            # 筛选发帖时间与标记
            mid = card.find('div', class_="from")
            time = mid.find('a')
            post.time = time.text.strip()
            sheet1.write(row, column, post.time)
            column += 1

            # 筛选发帖来源
            mid = card.find('div', attrs={"class": "from"})
            origin = mid.find('a', attrs={"rel": "nofollow"})
            try:
                post.origin = origin.text
            except:
                post.origin = ''
            sheet1.write(row, column, post.origin)
            column += 1

            # 筛选发帖正文 需要格式化处理开头空格
            content = card.find('p', attrs={"node-type": "feed_list_content_full", "class": "txt"})
            if content is None:
                content = card.find('p', attrs={"node-type": "feed_list_content", "class": "txt"})
            post.text = content.text
            post.text = post.text.strip()
            post.text = post.text.strip('\u200b')
            post.text = post.text.strip('收起d')
            sheet1.write(row, column, post.text)
            column += 1

            # 筛选帖子转发评论点赞数量
            act = card.find(name='div', attrs={"class": "card-act"})
            act_list = act.text.split('\n')
            # 3 4 8
            post.retweet_num = act_list[3].strip()
            post.comments_num = act_list[4].strip()
            post.likes_num = act_list[8].strip()
            sheet1.write(row, column, post.retweet_num)
            column += 1
            sheet1.write(row, column, post.comments_num)
            column += 1
            sheet1.write(row, column, post.likes_num)
            column += 1

file_name = f"D:\\wang\\Desktop\\Sina_Topic_From_{begin_date}_To_{end_date}_zhangxiaoquan.xls"
xls.save(file_name)
