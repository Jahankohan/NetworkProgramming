import asyncio
from datetime import datetime

## Coroutine
async def say(what, delay):
    await asyncio.sleep(delay)
    print(what)

## Coroutine
async def stop_after(loop, delay):
    await asyncio.sleep(delay)
    loop.stop()

## Event Loop
loop = asyncio.get_event_loop()



## Tasks
loop.create_task(say('first hello world', 2))
loop.create_task(say('second hello world', 3))
loop.create_task(say('third hello world', 5))
loop.create_task(stop_after(loop, 4))


start = datetime.now()
loop.run_forever()
finish = datetime.now()
print("Elapsed: " + str(finish - start))
loop.close()
