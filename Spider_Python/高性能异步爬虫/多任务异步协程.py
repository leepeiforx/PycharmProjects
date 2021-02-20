import asyncio
import time


async def requests(url):
    print('正在下载', url)
    # 在异步协程中,如果存在同步模块相关的代码,那么就无法实现异步
    # time.sleep(2)
    # 当在asyncio中遇到阻塞操作,必须进行手动挂起
    await asyncio.sleep(2)
    print('下载完成', url)


urls = ['www.baidu.com','www.sogou.com','www.doubanjiang.com']

start_time = time.perf_counter()
#任务列表:存放多个任务对象
stacks = []
for url in urls:
    c = requests(url)
    task = asyncio.ensure_future(c)
    stacks.append(task)

loop = asyncio.get_event_loop()
# 需要将任务列表封装到wait中
loop.run_until_complete(asyncio.wait(stacks))
end_time = time.perf_counter()
print(end_time-start_time)
