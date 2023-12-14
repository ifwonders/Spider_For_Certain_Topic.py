from aip import AipNlp
import xlrd
import time
import Spider_For_Certain_Topic
import matplotlib.pyplot as plt

# 我的 APPID AK SK #
APP_ID = '41812820'
API_Key = 'eDIj4w5mFEDjzzUSQSCNGD1T'
Secret_Key = 'rTmCY9lePr05GPpwhP6sX9m1mVxWeFdY'

# 储存客户端
client = AipNlp(APP_ID, API_Key, Secret_Key)

# url = input("请输入爬取话题链接：")
# pages = input("请输入爬取页数：")
#
# # 爬取话题帖子并返回所存储的xls文件路径
# file_name = Spider_For_Certain_Topic.make_excel(url=url, pages=pages)
file_name = 'D:\\wang\\Desktop\\Sina_Topic_At_2023-10-29.xls'
# 打开表格文件
xls = xlrd.open_workbook_xls(file_name)
table = xls.sheets()[0]

# 数据上传分析
emo_list = []
for cell in table.col(4, 1):
    text = cell.value
    result = client.sentimentClassify(text)
    if 'error_msg' in result:
        print(result['error_msg'])
    else:
        print(result['items'])
        emo_list.append(result['items'])
    time.sleep(2)

print("数据分析完毕")

# 数据处理
neg_cnt = 0
neg_rate = 0.0
valid_cnt = 0
for emotion in emo_list:
    # 筛选出确定度大于0.85的评论
    if emotion[0]['confidence'] < 0.85:
        continue
    else:
        valid_cnt += 1
        neg_rate += emotion[0]['negative_prob']
        if emotion[0]['negative_prob'] > 0.5:
            neg_cnt += 1

neg_rate /= valid_cnt
pos_cnt = valid_cnt - neg_cnt
pos_rate = 1.0 - neg_rate

# 绘制图表
# 绘制情绪数饼图
labels_cnt = ['Positive','Negative']
sizes_cnt = [pos_cnt,neg_cnt]
plt.pie(sizes_cnt,labels=labels_cnt,autopct='%1.1f%%',shadow=False,startangle=100)
plt.show()

labels = ['Positive','Negative']
sizes = [pos_rate,neg_rate]
plt.pie(sizes,labels=labels,autopct='%1.1f%%',shadow=True,startangle=100)
plt.show()

"""
[{'confidence': 0.555887, 'negative_prob': 0.199851, 'positive_prob': 0.800149, 'sentiment': 2}]
[{'confidence': 0.994512, 'negative_prob': 0.00246962, 'positive_prob': 0.99753, 'sentiment': 2}]
[{'confidence': 0.987102, 'negative_prob': 0.994196, 'positive_prob': 0.00580393, 'sentiment': 0}]
[{'confidence': 0.672326, 'negative_prob': 0.852547, 'positive_prob': 0.147453, 'sentiment': 0}]
[{'confidence': 0.99897, 'negative_prob': 0.999536, 'positive_prob': 0.000463693, 'sentiment': 0}]
[{'confidence': 0.85192, 'negative_prob': 0.933364, 'positive_prob': 0.0666359, 'sentiment': 0}]
[{'confidence': 0.699518, 'negative_prob': 0.135217, 'positive_prob': 0.864783, 'sentiment': 2}]
[{'confidence': 0.748082, 'negative_prob': 0.886637, 'positive_prob': 0.113363, 'sentiment': 0}]
[{'confidence': 0.709499, 'negative_prob': 0.869275, 'positive_prob': 0.130725, 'sentiment': 0}]
input text too long
[{'confidence': 0.986574, 'negative_prob': 0.993958, 'positive_prob': 0.00604168, 'sentiment': 0}]
[{'confidence': 0.994762, 'negative_prob': 0.997643, 'positive_prob': 0.0023569, 'sentiment': 0}]
[{'confidence': 0.226963, 'negative_prob': 0.347867, 'positive_prob': 0.652134, 'sentiment': 2}]
[{'confidence': 0.99866, 'negative_prob': 0.999397, 'positive_prob': 0.000602821, 'sentiment': 0}]
[{'confidence': 0.999969, 'negative_prob': 0.999986, 'positive_prob': 1.39464e-05, 'sentiment': 0}]
[{'confidence': 0.985771, 'negative_prob': 0.993597, 'positive_prob': 0.00640284, 'sentiment': 0}]
[{'confidence': 0.813002, 'negative_prob': 0.915851, 'positive_prob': 0.0841489, 'sentiment': 0}]
[{'confidence': 0.581621, 'negative_prob': 0.18827, 'positive_prob': 0.81173, 'sentiment': 2}]
[{'confidence': 0.626741, 'negative_prob': 0.832034, 'positive_prob': 0.167966, 'sentiment': 0}]
[{'confidence': 0.39525, 'negative_prob': 0.272137, 'positive_prob': 0.727863, 'sentiment': 2}]
[{'confidence': 0.677482, 'negative_prob': 0.854867, 'positive_prob': 0.145133, 'sentiment': 0}]
[{'confidence': 0.997317, 'negative_prob': 0.998793, 'positive_prob': 0.00120737, 'sentiment': 0}]
[{'confidence': 0.937751, 'negative_prob': 0.028012, 'positive_prob': 0.971988, 'sentiment': 2}]
[{'confidence': 0.822815, 'negative_prob': 0.0797332, 'positive_prob': 0.920267, 'sentiment': 2}]
[{'confidence': 0.732461, 'negative_prob': 0.879607, 'positive_prob': 0.120393, 'sentiment': 0}]
[{'confidence': 0.0171207, 'negative_prob': 0.557704, 'positive_prob': 0.442296, 'sentiment': 0}]
[{'confidence': 0.296395, 'negative_prob': 0.683378, 'positive_prob': 0.316622, 'sentiment': 0}]
[{'confidence': 0.94077, 'negative_prob': 0.0266537, 'positive_prob': 0.973346, 'sentiment': 2}]
[{'confidence': 0.977262, 'negative_prob': 0.0102319, 'positive_prob': 0.989768, 'sentiment': 2}]
[{'confidence': 0.868463, 'negative_prob': 0.940809, 'positive_prob': 0.0591915, 'sentiment': 0}]
[{'confidence': 0.986133, 'negative_prob': 0.99376, 'positive_prob': 0.00624005, 'sentiment': 0}]
[{'confidence': 0.87225, 'negative_prob': 0.942512, 'positive_prob': 0.0574876, 'sentiment': 0}]
[{'confidence': 0.910983, 'negative_prob': 0.0400575, 'positive_prob': 0.959942, 'sentiment': 2}]
[{'confidence': 0.75251, 'negative_prob': 0.888629, 'positive_prob': 0.111371, 'sentiment': 0}]
[{'confidence': 0.879351, 'negative_prob': 0.0542923, 'positive_prob': 0.945708, 'sentiment': 2}]
[{'confidence': 0.807194, 'negative_prob': 0.0867626, 'positive_prob': 0.913237, 'sentiment': 2}]
[{'confidence': 0.562647, 'negative_prob': 0.803191, 'positive_prob': 0.196809, 'sentiment': 0}]
[{'confidence': 0.971636, 'negative_prob': 0.987236, 'positive_prob': 0.0127636, 'sentiment': 0}]
[{'confidence': 0.874707, 'negative_prob': 0.943618, 'positive_prob': 0.0563816, 'sentiment': 0}]
[{'confidence': 0.284264, 'negative_prob': 0.322081, 'positive_prob': 0.677919, 'sentiment': 2}]
[{'confidence': 0.96587, 'negative_prob': 0.0153586, 'positive_prob': 0.984641, 'sentiment': 2}]
[{'confidence': 0.999673, 'negative_prob': 0.999853, 'positive_prob': 0.000147305, 'sentiment': 0}]
[{'confidence': 0.0838053, 'negative_prob': 0.412288, 'positive_prob': 0.587712, 'sentiment': 2}]
[{'confidence': 0.784204, 'negative_prob': 0.097108, 'positive_prob': 0.902892, 'sentiment': 2}]
[{'confidence': 0.724594, 'negative_prob': 0.123933, 'positive_prob': 0.876067, 'sentiment': 2}]
[{'confidence': 0.567165, 'negative_prob': 0.194776, 'positive_prob': 0.805224, 'sentiment': 2}]
[{'confidence': 0.423222, 'negative_prob': 0.74045, 'positive_prob': 0.25955, 'sentiment': 0}]
[{'confidence': 0.995285, 'negative_prob': 0.997878, 'positive_prob': 0.00212172, 'sentiment': 0}]
[{'confidence': 0.438228, 'negative_prob': 0.252797, 'positive_prob': 0.747203, 'sentiment': 2}]
[{'confidence': 0.907902, 'negative_prob': 0.958556, 'positive_prob': 0.0414442, 'sentiment': 0}]
[{'confidence': 0.0989309, 'negative_prob': 0.405481, 'positive_prob': 0.594519, 'sentiment': 2}]
[{'confidence': 0.978297, 'negative_prob': 0.990234, 'positive_prob': 0.00976631, 'sentiment': 0}]
[{'confidence': 0.991567, 'negative_prob': 0.996205, 'positive_prob': 0.00379474, 'sentiment': 0}]
[{'confidence': 0.555887, 'negative_prob': 0.199851, 'positive_prob': 0.800149, 'sentiment': 2}]
[{'confidence': 0.999838, 'negative_prob': 0.999927, 'positive_prob': 7.29647e-05, 'sentiment': 0}]
[{'confidence': 0.860498, 'negative_prob': 0.937224, 'positive_prob': 0.0627758, 'sentiment': 0}]
[{'confidence': 0.961401, 'negative_prob': 0.98263, 'positive_prob': 0.0173697, 'sentiment': 0}]
[{'confidence': 0.274978, 'negative_prob': 0.536251, 'positive_prob': 0.463749, 'sentiment': 1}]
[{'confidence': 0.941098, 'negative_prob': 0.973494, 'positive_prob': 0.0265059, 'sentiment': 0}]
[{'confidence': 0.964231, 'negative_prob': 0.983904, 'positive_prob': 0.0160958, 'sentiment': 0}]
[{'confidence': 0.358837, 'negative_prob': 0.711476, 'positive_prob': 0.288524, 'sentiment': 0}]
[{'confidence': 0.998496, 'negative_prob': 0.999323, 'positive_prob': 0.000676892, 'sentiment': 0}]
[{'confidence': 0.969993, 'negative_prob': 0.0135032, 'positive_prob': 0.986497, 'sentiment': 2}]
[{'confidence': 0.810825, 'negative_prob': 0.914871, 'positive_prob': 0.0851288, 'sentiment': 0}]
[{'confidence': 0.99945, 'negative_prob': 0.999753, 'positive_prob': 0.000247318, 'sentiment': 0}]
[{'confidence': 0.955872, 'negative_prob': 0.980142, 'positive_prob': 0.0198578, 'sentiment': 0}]
[{'confidence': 0.0410177, 'negative_prob': 0.568458, 'positive_prob': 0.431542, 'sentiment': 0}]
[{'confidence': 0.316297, 'negative_prob': 0.692334, 'positive_prob': 0.307666, 'sentiment': 0}]
[{'confidence': 0.990354, 'negative_prob': 0.995659, 'positive_prob': 0.00434085, 'sentiment': 0}]
[{'confidence': 0.9433, 'negative_prob': 0.0255147, 'positive_prob': 0.974485, 'sentiment': 2}]
[{'confidence': 0.889449, 'negative_prob': 0.0497479, 'positive_prob': 0.950252, 'sentiment': 2}]
[{'confidence': 0.851067, 'negative_prob': 0.93298, 'positive_prob': 0.0670201, 'sentiment': 0}]
[{'confidence': 0.928315, 'negative_prob': 0.0322582, 'positive_prob': 0.967742, 'sentiment': 2}]
[{'confidence': 0.694823, 'negative_prob': 0.86267, 'positive_prob': 0.13733, 'sentiment': 0}]
[{'confidence': 0.998059, 'negative_prob': 0.999127, 'positive_prob': 0.000873362, 'sentiment': 0}]
[{'confidence': 0.999159, 'negative_prob': 0.999621, 'positive_prob': 0.000378652, 'sentiment': 0}]
[{'confidence': 0.966844, 'negative_prob': 0.0149203, 'positive_prob': 0.98508, 'sentiment': 2}]
[{'confidence': 0.688232, 'negative_prob': 0.859704, 'positive_prob': 0.140296, 'sentiment': 0}]
[{'confidence': 0.659305, 'negative_prob': 0.153313, 'positive_prob': 0.846687, 'sentiment': 2}]
[{'confidence': 0.405972, 'negative_prob': 0.267313, 'positive_prob': 0.732687, 'sentiment': 2}]
[{'confidence': 0.936683, 'negative_prob': 0.971507, 'positive_prob': 0.0284928, 'sentiment': 0}]
[{'confidence': 0.0181679, 'negative_prob': 0.441824, 'positive_prob': 0.558176, 'sentiment': 2}]
[{'confidence': 0.833961, 'negative_prob': 0.0747174, 'positive_prob': 0.925283, 'sentiment': 2}]
[{'confidence': 0.0771413, 'negative_prob': 0.415286, 'positive_prob': 0.584714, 'sentiment': 2}]
[{'confidence': 0.998703, 'negative_prob': 0.999416, 'positive_prob': 0.000583833, 'sentiment': 0}]
[{'confidence': 0.57183, 'negative_prob': 0.192677, 'positive_prob': 0.807323, 'sentiment': 2}]
[{'confidence': 0.239984, 'negative_prob': 0.657993, 'positive_prob': 0.342007, 'sentiment': 0}]
[{'confidence': 0.688897, 'negative_prob': 0.860004, 'positive_prob': 0.139996, 'sentiment': 0}]
[{'confidence': 0.718105, 'negative_prob': 0.126853, 'positive_prob': 0.873147, 'sentiment': 2}]
[{'confidence': 0.368416, 'negative_prob': 0.284213, 'positive_prob': 0.715787, 'sentiment': 2}]
[{'confidence': 0.98802, 'negative_prob': 0.994609, 'positive_prob': 0.00539103, 'sentiment': 0}]
[{'confidence': 0.641279, 'negative_prob': 0.838576, 'positive_prob': 0.161424, 'sentiment': 0}]
[{'confidence': 0.0759208, 'negative_prob': 0.584164, 'positive_prob': 0.415836, 'sentiment': 0}]
[{'confidence': 0.528921, 'negative_prob': 0.211986, 'positive_prob': 0.788014, 'sentiment': 2}]
[{'confidence': 0.439215, 'negative_prob': 0.747647, 'positive_prob': 0.252353, 'sentiment': 0}]
[{'confidence': 0.973927, 'negative_prob': 0.0117327, 'positive_prob': 0.988267, 'sentiment': 2}]
[{'confidence': 0.231326, 'negative_prob': 0.345903, 'positive_prob': 0.654097, 'sentiment': 2}]
[{'confidence': 0.978814, 'negative_prob': 0.00953387, 'positive_prob': 0.990466, 'sentiment': 2}]
[{'confidence': 0.976087, 'negative_prob': 0.0107607, 'positive_prob': 0.989239, 'sentiment': 2}]
[{'confidence': 0.479368, 'negative_prob': 0.765715, 'positive_prob': 0.234285, 'sentiment': 0}]
[{'confidence': 0.935618, 'negative_prob': 0.028972, 'positive_prob': 0.971028, 'sentiment': 2}]
[{'confidence': 0.885217, 'negative_prob': 0.948348, 'positive_prob': 0.0516522, 'sentiment': 0}]
[{'confidence': 0.469162, 'negative_prob': 0.238877, 'positive_prob': 0.761123, 'sentiment': 2}]
[{'confidence': 0.917284, 'negative_prob': 0.0372222, 'positive_prob': 0.962778, 'sentiment': 2}]
[{'confidence': 0.668463, 'negative_prob': 0.149192, 'positive_prob': 0.850808, 'sentiment': 2}]
[{'confidence': 0.244957, 'negative_prob': 0.537752, 'positive_prob': 0.462248, 'sentiment': 1}]
[{'confidence': 0.977249, 'negative_prob': 0.010238, 'positive_prob': 0.989762, 'sentiment': 2}]
[{'confidence': 0.875855, 'negative_prob': 0.0558651, 'positive_prob': 0.944135, 'sentiment': 2}]
[{'confidence': 0.727378, 'negative_prob': 0.87732, 'positive_prob': 0.12268, 'sentiment': 0}]
[{'confidence': 0.925167, 'negative_prob': 0.0336747, 'positive_prob': 0.966325, 'sentiment': 2}]
[{'confidence': 0.973378, 'negative_prob': 0.98802, 'positive_prob': 0.0119797, 'sentiment': 0}]
[{'confidence': 0.299318, 'negative_prob': 0.684693, 'positive_prob': 0.315307, 'sentiment': 0}]
[{'confidence': 0.531596, 'negative_prob': 0.210782, 'positive_prob': 0.789218, 'sentiment': 2}]
[{'confidence': 0.828585, 'negative_prob': 0.922863, 'positive_prob': 0.0771369, 'sentiment': 0}]
[{'confidence': 0.697334, 'negative_prob': 0.8638, 'positive_prob': 0.1362, 'sentiment': 0}]
[{'confidence': 0.356639, 'negative_prob': 0.289512, 'positive_prob': 0.710488, 'sentiment': 2}]
[{'confidence': 0.999187, 'negative_prob': 0.000365984, 'positive_prob': 0.999634, 'sentiment': 2}]
[{'confidence': 0.978588, 'negative_prob': 0.990364, 'positive_prob': 0.00963561, 'sentiment': 0}]
[{'confidence': 0.538791, 'negative_prob': 0.792456, 'positive_prob': 0.207544, 'sentiment': 0}]
[{'confidence': 0.859689, 'negative_prob': 0.93686, 'positive_prob': 0.06314, 'sentiment': 0}]
[{'confidence': 0.625557, 'negative_prob': 0.168499, 'positive_prob': 0.831501, 'sentiment': 2}]
[{'confidence': 0.990399, 'negative_prob': 0.99568, 'positive_prob': 0.00432035, 'sentiment': 0}]
[{'confidence': 0.630422, 'negative_prob': 0.83369, 'positive_prob': 0.16631, 'sentiment': 0}]
[{'confidence': 0.992204, 'negative_prob': 0.996492, 'positive_prob': 0.00350819, 'sentiment': 0}]
[{'confidence': 0.287429, 'negative_prob': 0.464371, 'positive_prob': 0.535629, 'sentiment': 1}]
[{'confidence': 0.998204, 'negative_prob': 0.999192, 'positive_prob': 0.00080813, 'sentiment': 0}]
[{'confidence': 0.942455, 'negative_prob': 0.0258951, 'positive_prob': 0.974105, 'sentiment': 2}]
[{'confidence': 0.896159, 'negative_prob': 0.953271, 'positive_prob': 0.0467286, 'sentiment': 0}]
[{'confidence': 0.975796, 'negative_prob': 0.49879, 'positive_prob': 0.50121, 'sentiment': 1}]
[{'confidence': 0.998899, 'negative_prob': 0.999504, 'positive_prob': 0.000495576, 'sentiment': 0}]
[{'confidence': 0.320259, 'negative_prob': 0.305883, 'positive_prob': 0.694117, 'sentiment': 2}]
[{'confidence': 0.585672, 'negative_prob': 0.813553, 'positive_prob': 0.186447, 'sentiment': 0}]
[{'confidence': 0.963851, 'negative_prob': 0.983733, 'positive_prob': 0.0162669, 'sentiment': 0}]
[{'confidence': 0.851552, 'negative_prob': 0.933198, 'positive_prob': 0.0668017, 'sentiment': 0}]
[{'confidence': 0.998999, 'negative_prob': 0.999549, 'positive_prob': 0.000450556, 'sentiment': 0}]
[{'confidence': 0.99535, 'negative_prob': 0.997907, 'positive_prob': 0.00209269, 'sentiment': 0}]
[{'confidence': 0.363442, 'negative_prob': 0.286451, 'positive_prob': 0.713549, 'sentiment': 2}]
[{'confidence': 0.953737, 'negative_prob': 0.0208183, 'positive_prob': 0.979182, 'sentiment': 2}]
[{'confidence': 0.70467, 'negative_prob': 0.867101, 'positive_prob': 0.132899, 'sentiment': 0}]
[{'confidence': 0.417809, 'negative_prob': 0.738014, 'positive_prob': 0.261986, 'sentiment': 0}]
[{'confidence': 0.92411, 'negative_prob': 0.965849, 'positive_prob': 0.0341507, 'sentiment': 0}]
[{'confidence': 0.995135, 'negative_prob': 0.997811, 'positive_prob': 0.00218937, 'sentiment': 0}]
[{'confidence': 0.77173, 'negative_prob': 0.897279, 'positive_prob': 0.102721, 'sentiment': 0}]
[{'confidence': 0.99679, 'negative_prob': 0.998555, 'positive_prob': 0.00144465, 'sentiment': 0}]
[{'confidence': 0.143438, 'negative_prob': 0.385453, 'positive_prob': 0.614547, 'sentiment': 2}]
[{'confidence': 0.344248, 'negative_prob': 0.704911, 'positive_prob': 0.295088, 'sentiment': 0}]
[{'confidence': 0.999287, 'negative_prob': 0.999679, 'positive_prob': 0.000321016, 'sentiment': 0}]
[{'confidence': 0.766525, 'negative_prob': 0.105064, 'positive_prob': 0.894936, 'sentiment': 2}]
[{'confidence': 0.578723, 'negative_prob': 0.810426, 'positive_prob': 0.189574, 'sentiment': 0}]
[{'confidence': 0.553363, 'negative_prob': 0.799013, 'positive_prob': 0.200987, 'sentiment': 0}]
[{'confidence': 0.0369019, 'negative_prob': 0.433394, 'positive_prob': 0.566606, 'sentiment': 2}]
[{'confidence': 0.26826, 'negative_prob': 0.670717, 'positive_prob': 0.329283, 'sentiment': 0}]
[{'confidence': 0.853223, 'negative_prob': 0.93395, 'positive_prob': 0.0660498, 'sentiment':s 0}]
[{'confidence': 0.975829, 'negative_prob': 0.989123, 'positive_prob': 0.0108769, 'sentiment': 0}]
[{'confidence': 0.993781, 'negative_prob': 0.997201, 'positive_prob': 0.00279864, 'sentiment': 0}]
[{'confidence': 0.993452, 'negative_prob': 0.997054, 'positive_prob': 0.00294637, 'sentiment': 0}]
[{'confidence': 0.676962, 'negative_prob': 0.145367, 'positive_prob': 0.854633, 'sentiment': 2}]
[{'confidence': 0.947103, 'negative_prob': 0.976196, 'positive_prob': 0.0238037, 'sentiment': 0}]
[{'confidence': 0.527894, 'negative_prob': 0.212448, 'positive_prob': 0.787552, 'sentiment': 2}]
[{'confidence': 0.754871, 'negative_prob': 0.110308, 'positive_prob': 0.889692, 'sentiment': 2}]
[{'confidence': 0.957165, 'negative_prob': 0.980724, 'positive_prob': 0.0192758, 'sentiment': 0}]
[{'confidence': 0.503262, 'negative_prob': 0.223532, 'positive_prob': 0.776468, 'sentiment': 2}]
[{'confidence': 0.65525, 'negative_prob': 0.155137, 'positive_prob': 0.844863, 'sentiment': 2}]
[{'confidence': 0.981436, 'negative_prob': 0.991646, 'positive_prob': 0.008354, 'sentiment': 0}]
[{'confidence': 0.995143, 'negative_prob': 0.00218566, 'positive_prob': 0.997814, 'sentiment': 2}]
[{'confidence': 0.886086, 'negative_prob': 0.0512613, 'positive_prob': 0.948739, 'sentiment': 2}]
[{'confidence': 0.0280243, 'negative_prob': 0.437389, 'positive_prob': 0.562611, 'sentiment': 2}]
[{'confidence': 0.74136, 'negative_prob': 0.883612, 'positive_prob': 0.116388, 'sentiment': 0}]
[{'confidence': 0.16771, 'negative_prob': 0.625469, 'positive_prob': 0.374531, 'sentiment': 0}]
[{'confidence': 0.438643, 'negative_prob': 0.74739, 'positive_prob': 0.25261, 'sentiment': 0}]
[{'confidence': 0.824281, 'negative_prob': 0.0790734, 'positive_prob': 0.920927, 'sentiment': 2}]
[{'confidence': 0.853799, 'negative_prob': 0.93421, 'positive_prob': 0.0657905, 'sentiment': 0}]
[{'confidence': 0.649759, 'negative_prob': 0.842391, 'positive_prob': 0.157609, 'sentiment': 0}]
[{'confidence': 0.800715, 'negative_prob': 0.910322, 'positive_prob': 0.0896781, 'sentiment': 0}]
[{'confidence': 0.187973, 'negative_prob': 0.365412, 'positive_prob': 0.634588, 'sentiment': 2}]
[{'confidence': 0.0211555, 'negative_prob': 0.55952, 'positive_prob': 0.44048, 'sentiment': 0}]
[{'confidence': 0.226725, 'negative_prob': 0.347974, 'positive_prob': 0.652026, 'sentiment': 2}]
[{'confidence': 0.730712, 'negative_prob': 0.87882, 'positive_prob': 0.12118, 'sentiment': 0}]
[{'confidence': 0.895092, 'negative_prob': 0.952791, 'positive_prob': 0.0472085, 'sentiment': 0}]
[{'confidence': 0.913746, 'negative_prob': 0.0388143, 'positive_prob': 0.961186, 'sentiment': 2}]
[{'confidence': 0.998954, 'negative_prob': 0.000470871, 'positive_prob': 0.999529, 'sentiment': 2}]
[{'confidence': 0.495961, 'negative_prob': 0.226817, 'positive_prob': 0.773183, 'sentiment': 2}]
[{'confidence': 0.986587, 'negative_prob': 0.00603592, 'positive_prob': 0.993964, 'sentiment': 2}]
[{'confidence': 0.99877, 'negative_prob': 0.999447, 'positive_prob': 0.000553389, 'sentiment': 0}]
[{'confidence': 0.718882, 'negative_prob': 0.873497, 'positive_prob': 0.126503, 'sentiment': 0}]
[{'confidence': 0.770357, 'negative_prob': 0.896661, 'positive_prob': 0.103339, 'sentiment': 0}]
[{'confidence': 0.663745, 'negative_prob': 0.848685, 'positive_prob': 0.151315, 'sentiment': 0}]
[{'confidence': 0.933323, 'negative_prob': 0.0300046, 'positive_prob': 0.969995, 'sentiment': 2}]
[{'confidence': 0.199399, 'negative_prob': 0.36027, 'positive_prob': 0.63973, 'sentiment': 2}]
[{'confidence': 0.258904, 'negative_prob': 0.333493, 'positive_prob': 0.666507, 'sentiment': 2}]
[{'confidence': 0.695673, 'negative_prob': 0.863053, 'positive_prob': 0.136947, 'sentiment': 0}]
[{'confidence': 0.980325, 'negative_prob': 0.991146, 'positive_prob': 0.00885353, 'sentiment': 0}]
[{'confidence': 0.997306, 'negative_prob': 0.998788, 'positive_prob': 0.00121235, 'sentiment': 0}]
[{'confidence': 0.201775, 'negative_prob': 0.640799, 'positive_prob': 0.359201, 'sentiment': 0}]
[{'confidence': 0.947809, 'negative_prob': 0.0234858, 'positive_prob': 0.976514, 'sentiment': 2}]
[{'confidence': 0.989603, 'negative_prob': 0.00467853, 'positive_prob': 0.995321, 'sentiment': 2}]
[{'confidence': 0.760108, 'negative_prob': 0.892049, 'positive_prob': 0.107951, 'sentiment': 0}]
[{'confidence': 0.863053, 'negative_prob': 0.938374, 'positive_prob': 0.0616263, 'sentiment': 0}]
[{'confidence': 0.226048, 'negative_prob': 0.348278, 'positive_prob': 0.651722, 'sentiment': 2}]
[{'confidence': 0.9817, 'negative_prob': 0.991765, 'positive_prob': 0.008235, 'sentiment': 0}]
[{'confidence': 0.754184, 'negative_prob': 0.110617, 'positive_prob': 0.889383, 'sentiment': 2}]
[{'confidence': 0.158864, 'negative_prob': 0.378511, 'positive_prob': 0.621489, 'sentiment': 2}]
[{'confidence': 0.769827, 'negative_prob': 0.896422, 'positive_prob': 0.103578, 'sentiment': 0}]
[{'confidence': 0.704807, 'negative_prob': 0.132837, 'positive_prob': 0.867163, 'sentiment': 2}]
[{'confidence': 0.998556, 'negative_prob': 0.99935, 'positive_prob': 0.000649662, 'sentiment': 0}]
[{'confidence': 0.961585, 'negative_prob': 0.982713, 'positive_prob': 0.0172868, 'sentiment': 0}]
[{'confidence': 0.969329, 'negative_prob': 0.986198, 'positive_prob': 0.0138019, 'sentiment': 0}]
[{'confidence': 0.940955, 'negative_prob': 0.97343, 'positive_prob': 0.0265704, 'sentiment': 0}]
[{'confidence': 0.773344, 'negative_prob': 0.898005, 'positive_prob': 0.101995, 'sentiment': 0}]
[{'confidence': 0.98713, 'negative_prob': 0.00579138, 'positive_prob': 0.994209, 'sentiment': 2}]
[{'confidence': 0.968886, 'negative_prob': 0.985999, 'positive_prob': 0.014001, 'sentiment': 0}]
[{'confidence': 0.407116, 'negative_prob': 0.733202, 'positive_prob': 0.266798, 'sentiment': 0}]
[{'confidence': 0.996135, 'negative_prob': 0.998261, 'positive_prob': 0.00173908, 'sentiment': 0}]
[{'confidence': 0.268148, 'negative_prob': 0.670667, 'positive_prob': 0.329333, 'sentiment': 0}]
[{'confidence': 0.838004, 'negative_prob': 0.927102, 'positive_prob': 0.0728983, 'sentiment': 0}]
[{'confidence': 0.524746, 'negative_prob': 0.213864, 'positive_prob': 0.786136, 'sentiment': 2}]
[{'confidence': 0.610257, 'negative_prob': 0.175384, 'positive_prob': 0.824616, 'sentiment': 2}]
[{'confidence': 0.972731, 'negative_prob': 0.0122712, 'positive_prob': 0.987729, 'sentiment': 2}]
[{'confidence': 0.882638, 'negative_prob': 0.052813, 'positive_prob': 0.947187, 'sentiment': 2}]
[{'confidence': 0.73028, 'negative_prob': 0.878626, 'positive_prob': 0.121374, 'sentiment': 0}]
[{'confidence': 0.517458, 'negative_prob': 0.217144, 'positive_prob': 0.782856, 'sentiment': 2}]
[{'confidence': 0.914198, 'negative_prob': 0.961389, 'positive_prob': 0.0386108, 'sentiment': 0}]
[{'confidence': 0.712488, 'negative_prob': 0.129381, 'positive_prob': 0.870619, 'sentiment': 2}]
[{'confidence': 0.956744, 'negative_prob': 0.980535, 'positive_prob': 0.019465, 'sentiment': 0}]
[{'confidence': 0.974499, 'negative_prob': 0.988524, 'positive_prob': 0.0114757, 'sentiment': 0}]
[{'confidence': 0.49866, 'negative_prob': 0.225603, 'positive_prob': 0.774397, 'sentiment': 2}]
[{'confidence': 0.994493, 'negative_prob': 0.00247828, 'positive_prob': 0.997522, 'sentiment': 2}]
[{'confidence': 0.995319, 'negative_prob': 0.997894, 'positive_prob': 0.00210629, 'sentiment': 0}]
[{'confidence': 0.576146, 'negative_prob': 0.190734, 'positive_prob': 0.809266, 'sentiment': 2}]
[{'confidence': 0.980219, 'negative_prob': 0.991099, 'positive_prob': 0.00890129, 'sentiment': 0}]
[{'confidence': 0.997296, 'negative_prob': 0.00121689, 'positive_prob': 0.998783, 'sentiment': 2}]
[{'confidence': 0.324424, 'negative_prob': 0.695991, 'positive_prob': 0.304009, 'sentiment': 0}]
[{'confidence': 0.991406, 'negative_prob': 0.996133, 'positive_prob': 0.00386724, 'sentiment': 0}]
[{'confidence': 0.979478, 'negative_prob': 0.990765, 'positive_prob': 0.00923497, 'sentiment': 0}]
[{'confidence': 0.980489, 'negative_prob': 0.99122, 'positive_prob': 0.00878009, 'sentiment': 0}]
[{'confidence': 0.696967, 'negative_prob': 0.863635, 'positive_prob': 0.136365, 'sentiment': 0}]
[{'confidence': 0.247672, 'negative_prob': 0.661453, 'positive_prob': 0.338547, 'sentiment': 0}]
[{'confidence': 0.999626, 'negative_prob': 0.000168235, 'positive_prob': 0.999832, 'sentiment': 2}]
[{'confidence': 0.986673, 'negative_prob': 0.994003, 'positive_prob': 0.00599694, 'sentiment': 0}]
[{'confidence': 0.569082, 'negative_prob': 0.806087, 'positive_prob': 0.193913, 'sentiment': 0}]
[{'confidence': 0.763429, 'negative_prob': 0.106457, 'positive_prob': 0.893543, 'sentiment': 2}]
[{'confidence': 0.290264, 'negative_prob': 0.319381, 'positive_prob': 0.680619, 'sentiment': 2}]
[{'confidence': 0.75982, 'negative_prob': 0.891919, 'positive_prob': 0.108081, 'sentiment': 0}]
[{'confidence': 0.999255, 'negative_prob': 0.999665, 'positive_prob': 0.000335316, 'sentiment': 0}]
[{'confidence': 0.999895, 'negative_prob': 4.71008e-05, 'positive_prob': 0.999953, 'sentiment': 2}]
[{'confidence': 0.731101, 'negative_prob': 0.513445, 'positive_prob': 0.486555, 'sentiment': 1}]
[{'confidence': 0.877171, 'negative_prob': 0.944727, 'positive_prob': 0.0552731, 'sentiment': 0}]
[{'confidence': 0.0672315, 'negative_prob': 0.419746, 'positive_prob': 0.580254, 'sentiment': 2}]
[{'confidence': 0.985067, 'negative_prob': 0.00671993, 'positive_prob': 0.99328, 'sentiment': 2}]
[{'confidence': 0.737735, 'negative_prob': 0.881981, 'positive_prob': 0.118019, 'sentiment': 0}]
[{'confidence': 0.854394, 'negative_prob': 0.934477, 'positive_prob': 0.0655227, 'sentiment': 0}]
[{'confidence': 0.999553, 'negative_prob': 0.999799, 'positive_prob': 0.000201169, 'sentiment': 0}]
[{'confidence': 0.0906176, 'negative_prob': 0.409222, 'positive_prob': 0.590778, 'sentiment': 2}]
[{'confidence': 0.976032, 'negative_prob': 0.0107858, 'positive_prob': 0.989214, 'sentiment': 2}]
[{'confidence': 0.463456, 'negative_prob': 0.758555, 'positive_prob': 0.241445, 'sentiment': 0}]
[{'confidence': 0.995016, 'negative_prob': 0.00224286, 'positive_prob': 0.997757, 'sentiment': 2}]
[{'confidence': 0.926323, 'negative_prob': 0.966845, 'positive_prob': 0.0331549, 'sentiment': 0}]
[{'confidence': 0.983898, 'negative_prob': 0.992754, 'positive_prob': 0.00724602, 'sentiment': 0}]
[{'confidence': 0.257201, 'negative_prob': 0.665741, 'positive_prob': 0.334259, 'sentiment': 0}]
[{'confidence': 0.867527, 'negative_prob': 0.0596127, 'positive_prob': 0.940387, 'sentiment': 2}]
[{'confidence': 0.991712, 'negative_prob': 0.00372953, 'positive_prob': 0.99627, 'sentiment': 2}]
[{'confidence': 0.466025, 'negative_prob': 0.240289, 'positive_prob': 0.759711, 'sentiment': 2}]
[{'confidence': 0.755614, 'negative_prob': 0.890027, 'positive_prob': 0.109973, 'sentiment': 0}]
[{'confidence': 0.771013, 'negative_prob': 0.896956, 'positive_prob': 0.103044, 'sentiment': 0}]
[{'confidence': 0.706934, 'negative_prob': 0.13188, 'positive_prob': 0.86812, 'sentiment': 2}]
[{'confidence': 0.664924, 'negative_prob': 0.150784, 'positive_prob': 0.849216, 'sentiment': 2}]
[{'confidence': 0.678289, 'negative_prob': 0.85523, 'positive_prob': 0.14477, 'sentiment': 0}]
[{'confidence': 0.973044, 'negative_prob': 0.98787, 'positive_prob': 0.0121303, 'sentiment': 0}]
[{'confidence': 0.402401, 'negative_prob': 0.26892, 'positive_prob': 0.73108, 'sentiment': 2}]
[{'confidence': 0.9973, 'negative_prob': 0.998785, 'positive_prob': 0.00121489, 'sentiment': 0}]
[{'confidence': 0.774, 'negative_prob': 0.1017, 'positive_prob': 0.8983, 'sentiment': 2}]
[{'confidence': 0.95578, 'negative_prob': 0.980101, 'positive_prob': 0.0198988, 'sentiment': 0}]
[{'confidence': 0.334666, 'negative_prob': 0.7006, 'positive_prob': 0.2994, 'sentiment': 0}]
[{'confidence': 0.74926, 'negative_prob': 0.887167, 'positive_prob': 0.112833, 'sentiment': 0}]
[{'confidence': 0.971382, 'negative_prob': 0.0128779, 'positive_prob': 0.987122, 'sentiment': 2}]
[{'confidence': 0.58684, 'negative_prob': 0.814078, 'positive_prob': 0.185922, 'sentiment': 0}]
[{'confidence': 0.983838, 'negative_prob': 0.992727, 'positive_prob': 0.00727296, 'sentiment': 0}]
[{'confidence': 0.865032, 'negative_prob': 0.939264, 'positive_prob': 0.0607356, 'sentiment': 0}]
[{'confidence': 0.802696, 'negative_prob': 0.911213, 'positive_prob': 0.0887866, 'sentiment': 0}]
[{'confidence': 0.201742, 'negative_prob': 0.359216, 'positive_prob': 0.640784, 'sentiment': 2}]
[{'confidence': 0.789439, 'negative_prob': 0.0947524, 'positive_prob': 0.905248, 'sentiment': 2}]
[{'confidence': 0.858112, 'negative_prob': 0.93615, 'positive_prob': 0.0638497, 'sentiment': 0}]
[{'confidence': 0.914728, 'negative_prob': 0.961627, 'positive_prob': 0.0383726, 'sentiment': 0}]
[{'confidence': 0.988257, 'negative_prob': 0.994716, 'positive_prob': 0.00528425, 'sentiment': 0}]
[{'confidence': 0.830771, 'negative_prob': 0.923847, 'positive_prob': 0.0761528, 'sentiment': 0}]
[{'confidence': 0.996648, 'negative_prob': 0.998492, 'positive_prob': 0.0015084, 'sentiment': 0}]
[{'confidence': 0.962599, 'negative_prob': 0.983169, 'positive_prob': 0.0168306, 'sentiment': 0}]
[{'confidence': 0.999865, 'negative_prob': 0.999939, 'positive_prob': 6.08415e-05, 'sentiment': 0}]
[{'confidence': 0.507089, 'negative_prob': 0.22181, 'positive_prob': 0.77819, 'sentiment': 2}]
[{'confidence': 0.995934, 'negative_prob': 0.99817, 'positive_prob': 0.00182987, 'sentiment': 0}]
[{'confidence': 0.927368, 'negative_prob': 0.0326845, 'positive_prob': 0.967315, 'sentiment': 2}]
[{'confidence': 0.834189, 'negative_prob': 0.0746148, 'positive_prob': 0.925385, 'sentiment': 2}]
[{'confidence': 0.994145, 'negative_prob': 0.997365, 'positive_prob': 0.00263487, 'sentiment': 0}]
[{'confidence': 0.413623, 'negative_prob': 0.263869, 'positive_prob': 0.736131, 'sentiment': 2}]
[{'confidence': 0.975924, 'negative_prob': 0.498796, 'positive_prob': 0.501204, 'sentiment': 1}]
[{'confidence': 0.968885, 'negative_prob': 0.985998, 'positive_prob': 0.0140018, 'sentiment': 0}]
[{'confidence': 0.637109, 'negative_prob': 0.836699, 'positive_prob': 0.163301, 'sentiment': 0}]
[{'confidence': 0.926456, 'negative_prob': 0.966905, 'positive_prob': 0.0330946, 'sentiment': 0}]
[{'confidence': 0.99094, 'negative_prob': 0.995923, 'positive_prob': 0.00407685, 'sentiment': 0}]
[{'confidence': 0.998731, 'negative_prob': 0.999429, 'positive_prob': 0.000570935, 'sentiment': 0}]
[{'confidence': 0.949346, 'negative_prob': 0.977206, 'positive_prob': 0.0227944, 'sentiment': 0}]
[{'confidence': 0.999477, 'negative_prob': 0.999765, 'positive_prob': 0.000235107, 'sentiment': 0}]
[{'confidence': 0.998353, 'negative_prob': 0.999259, 'positive_prob': 0.000741142, 'sentiment': 0}]
[{'confidence': 0.204619, 'negative_prob': 0.357921, 'positive_prob': 0.642079, 'sentiment': 2}]
[{'confidence': 0.992731, 'negative_prob': 0.996729, 'positive_prob': 0.00327124, 'sentiment': 0}]
[{'confidence': 0.987237, 'negative_prob': 0.994257, 'positive_prob': 0.00574331, 'sentiment': 0}]
[{'confidence': 0.999694, 'negative_prob': 0.999862, 'positive_prob': 0.000137507, 'sentiment': 0}]
[{'confidence': 0.995949, 'negative_prob': 0.998177, 'positive_prob': 0.00182302, 'sentiment': 0}]
[{'confidence': 0.684122, 'negative_prob': 0.857855, 'positive_prob': 0.142145, 'sentiment': 0}]
[{'confidence': 0.406419, 'negative_prob': 0.732888, 'positive_prob': 0.267112, 'sentiment': 0}]
[{'confidence': 0.886535, 'negative_prob': 0.494327, 'positive_prob': 0.505673, 'sentiment': 1}]
[{'confidence': 0.92533, 'negative_prob': 0.966398, 'positive_prob': 0.0336016, 'sentiment':
"""
