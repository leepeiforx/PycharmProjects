import pandas as pd
import xlrd
from collections import defaultdict
from matplotlib import pyplot as plt

file_path = r'D:\System_files\Desktop\reguar_expression\regular_expression.xlsx'

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

read_excel = xlrd.open_workbook(file_path)
excel_table = read_excel.sheet_by_index(0)

column_names = excel_table.row_values(rowx=0, start_colx=0, end_colx=3)

rows_values = []
for i in range(1, excel_table.nrows):
    rows_values.append(excel_table.row_values(i))

excel_pd = pd.DataFrame(data=rows_values, columns=column_names)


def get_counts(seq):
    counts = defaultdict(int)
    for i in seq:
        counts[i] += 1
    return counts


res = get_counts(excel_pd['网站名称'])

result_pd = pd.DataFrame(list(res.items()), columns=['网站名称', '频数'])

res = result_pd.sort_values(by='频数', ascending=False)
plt.bar(res['网站名称'][1:11], res['频数'][1:11])
plt.show()
