import pandas as pd


def build_file():
    for ci in citys:
        path = r'D:\System_files\Desktop\allowance\中国移动通信集团陕西有限公司{}分公司.XLS'.format(ci)
        excel_name_build.append(path)


def excel_handle(file_path):
    col_names = ['序列号', '项目名称', '合计', '个人', '家庭', '集团', '新业务合计', '新业务个人', '新业务家庭',
                 '新业务集团', '同期合计', '同期个人', '同期家庭', '同期集团', '新业务同期合计', '新业务同期个人',
                 '新业务同期家庭', '新业务同期集团']
    excel_file = pd.read_excel(file_path, sheet_name='SL_0405 四轮驱动折扣折让报表-累计', header=4)

    df = pd.DataFrame(excel_file)
    # 替换字段名称
    df.columns = col_names

    # 增加地市字段
    df['地市'] = file_path[-9:-7]

    # 将所需字段中的'---'替换为0
    df['项目名称'] = df['项目名称'].str.strip()
    df['集团'] = df['集团'].replace('────', 0)
    df['新业务集团'] = df['新业务集团'].replace('────', 0)
    df['同期集团'] = df['同期集团'].replace('────', 0)
    df['新业务同期集团'] = df['新业务同期集团'].replace('────', 0)

    # 计算各期集团累计
    df['当期集团累计'] = df['集团'] + df['新业务集团']
    df['同期集团累计'] = df['同期集团'] + df['新业务同期集团']

    index = ['集团短信',
             '手机上网（统付）',
             '物联网流量费',
             'WLAN',
             '小微宽带',
             '集团客户互联网专线',
             '物联网服务费',
             '云计算',
             '专线业务收入',
             'IDC业务收入',
             'ICT业务收入',
             'IMS固话',
             '和教育', 'CMNET业务收入-其他-移动云',
             '集团通讯录']
    values = ['集团短彩净收入',
              '流量统付',
              '物联网',
              '专线',
              '专线',
              '专线',
              '物联网',
              '云',
              '专线',
              'IDC',
              'ICT',
              '融合通信（IMS固话）',
              '和教育',
              '云',
              '集团号簿']

    merge_dict = dict(zip(['项目名称', '业务分类'], [index, values]))

    merge_df = pd.DataFrame(merge_dict)

    needed_seq = [34, 57, 60, 62, 69, 74, 118, 125, 133, 142, 148, 152, 153, 167, 168]
    needed_df = df.loc[needed_seq]
    needed_df['当期集团累计'] = needed_df['当期集团累计'].astype(float)
    needed_df['同期集团累计'] = needed_df['同期集团累计'].astype(float)

    needed_df = needed_df[['地市', '项目名称', '当期集团累计', '同期集团累计']]
    pd_merge = pd.merge(needed_df, merge_df, on='项目名称', how='left')

    res = pd_merge.groupby(by=['业务分类', '地市']).sum()

    return res


if __name__ == '__main__':

    output_file_path = r'D:\System_files\Desktop\allowance\allowance_result.xlsx'
    citys = ['西安', '咸阳', '宝鸡', '渭南', '铜川', '延安', '榆林', '汉中', '安康', '商洛']
    excel_name_build = []

    build_file()
    result = []
    for excel_path in excel_name_build:
        result.append(excel_handle(excel_path))

    pd_c = pd.concat([result[0], result[1], result[2],
                      result[3], result[4], result[5]
                         , result[6], result[7], result[8], result[9]], axis=0)

    pd_c = pd.concat([result[0], result[1], result[2],
                      result[3], result[4], result[5],
                      result[6], result[7], result[8],
                      result[9]], axis=0)

    ans = pd_c.groupby(by=['业务分类', '地市']).sum()
    print(ans)
    print(ans.unstack('地市'))
    ans.unstack('地市').to_excel(output_file_path, sheet_name='result')
    print('done')
