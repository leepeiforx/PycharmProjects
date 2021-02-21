import aiohttp
import asyncio
import requests
import time

# %%
start = time.perf_counter()
urls = ['https://www.baidu.com', 'https://www.sogou.com', 'https://cn.bing.com/']


async def get_page(url):
    print('正在下载', url)
    # requests.get是基于同步的,所以无法实现异步,必须使用基于异步的网络请求模块进行指定url的请求发送,如
    # alohttp
    response = requests.get(url)
    print('{}下载完毕'.format(url), response.text)


tasks = []
for url in urls:
    c = get_page(url)
    task = asyncio.ensure_future(c)
    tasks.append(task)

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))
end = time.perf_counter()
print(end - start)


# %%

# 使用aiohttp中的ClientSession
async def get_page_aio(url):
    print('正在下载', url)
    # requests.get是基于同步的,所以无法实现异步,必须使用基于异步的网络请求模块进行指定url的请求发送,如
    # alohttp
    # response = requests.get(url)
    async with aiohttp.ClientSession() as session:
        # get(),post():
        # headers(),params/data,proxy = 'http://ip:posrt'
        async with await session.get(url) as response:
            # text()返回字符串形式的响应数据
            # read()返回二进制形式的响应数据
            # json()返回二进制形式的响应数据
            # 在获取响应数据操作之前,一定要使用await进行手动挂起
            page_text = await response.text()
            print(page_text)


tasks = []
for url in urls:
    c = get_page_aio(url)
    task = asyncio.ensure_future(c)
    tasks.append(task)

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))
end = time.perf_counter()
print(end - start)
