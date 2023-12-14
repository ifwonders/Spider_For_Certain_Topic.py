import xlrd
import jieba
import re
import wordcloud
#import Spider_For_Certain_Topic

# url = input("请输入爬取话题链接：")
# pages = int(input("请输入爬取页数："))
#
#
# file_name = Spider_For_Certain_Topic.make_excel(url=url, pages=pages)
file_name = "D:\\wang\\Desktop\\Sina_Topic_From_2022-07-13_To_2022-07-18_zhangxiaoquan.xls"
xls = xlrd.open_workbook_xls(file_name)
table = xls.sheets()[5]

word_cloud = ''
words = []

for cell in table.col(4, 1):
    text = re.sub(r'[\W]', "", cell.value)
    words += jieba.lcut(text)


for word in words[:]:
    if len(word) < 2:
        words.remove(word)
    if word == "微博":
        words.remove(word)
    if word == "视频":
        words.remove(word)

word_cloud += ' '.join(words)

# print(word_cloud)
wc = wordcloud.WordCloud(background_color='white', font_path='msyh.ttc', width=1000, height=860,
                         margin=2).generate(word_cloud).to_file("D:\\wang\\Desktop\\test6.png")
