#第一种
'''
import asyncio
from aiowebsocket.converses import AioWebSocket

async def startup(uri):
    async with AioWebSocket(uri) as aws:
        converse = aws.manipulator

        # 给服务端发送验证消息，观察网页接口数据动态获取
        message = '{发送的验证信息}'
        await converse.send(message)

        while True:
            receive = await converse.receive()

            # 拿到的是byte类型数据，解码为字符串数据
            print(receive.decode())


if __name__ == '__main__':
    remote = 'wss://mempool.space:8999/'
    asyncio.get_event_loop().run_until_complete(startup(remote))
'''
#第二种
from websocket import create_connection
url = "wss://mempool.space:8999/"
while True:
    try:
        ws = create_connection(url)
        print(ws)
        break
    except Exception as e:
        print(e)
        continue
while True:
    ws.send('2')
    response = ws.recv()
    print(response)
