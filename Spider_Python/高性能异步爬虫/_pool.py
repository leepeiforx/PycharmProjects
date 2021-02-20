import time


# 使用单线程串行方式执行

def get_page(str):
    print('正在下载:', str)
    time.sleep(2)
    print('下载成功', str)


name_list = ['xiaozi', 'aa', 'bb', 'cc']

start_time = time.perf_counter()
for i in range(len(name_list)):
    get_page(name_list[i])
end_time = time.perf_counter()
print('%seconds:{}s'.format(end_time-start_time))

#%%
# 使用线程池
# 导入线程池对应的类
from multiprocessing.dummy import Pool

start_time = time.perf_counter()
# 实例化线程池对象
pool = Pool(4)
# 将列表中每一个元素传递给get_page进行处理
pool.map(get_page, name_list)
end_time = time.perf_counter()
print('%seconds:{}s'.format(end_time-start_time))


