# {time.ctime()} Producer Running
# Consumer: Running
# Wed Aug 23 14:43:54 2023 Consumer: got nothing, waitting a whine...
# Wed Aug 23 14:43:55 2023 Consumer: got nothing, waitting a whine...
# Wed Aug 23 14:43:55 2023 >got 0.5112985466194957
# Wed Aug 23 14:43:55 2023 >got 0.23379320513729251
# Wed Aug 23 14:43:55 2023 Consumer: got nothing, waitting a whine...
# Wed Aug 23 14:43:56 2023 >got 0.2670471569787526
# Wed Aug 23 14:43:56 2023 Consumer: got nothing, waitting a whine...
# Wed Aug 23 14:43:56 2023 >got 0.9656327029114609
# Wed Aug 23 14:43:56 2023 Consumer: got nothing, waitting a whine...
# Wed Aug 23 14:43:57 2023 >got 0.27085536192257587
# Wed Aug 23 14:43:57 2023 Consumer: got nothing, waitting a whine...
# Wed Aug 23 14:43:57 2023 >got 0.6815927814831462
# Wed Aug 23 14:43:57 2023 Consumer: got nothing, waitting a whine...
# Wed Aug 23 14:43:58 2023 Consumer: got nothing, waitting a whine...
# Wed Aug 23 14:43:58 2023 >got 0.6315325192095643
# Wed Aug 23 14:43:58 2023 >got 0.23228952819543658
# Wed Aug 23 14:43:58 2023 Consumer: got nothing, waitting a whine...
# Wed Aug 23 14:43:59 2023 Consumer: got nothing, waitting a whine...
# Wed Aug 23 14:43:59 2023 >got 0.7394766328452153
# Wed Aug 23 14:43:59 2023 Consumer: got nothing, waitting a whine...
# Wed Aug 23 14:43:59 2023 Producer: Done
# Wed Aug 23 14:44:00 2023 >got 0.6864960698230771
# Wed Aug 23 14:44:00 2023 consume Done


from random import random
import asyncio
import time

#corotine ti generate work
async def producer(queue): 
    print('{time.ctime()} Producer Running')
    #genelate worl
    for i in range(10):          
        #generate a value
        value = random()
        #block to simulate work
        await asyncio.sleep(value)
        #add to the queue
        await queue.put(value)
        #print('{time.ctime()} Producer:Done')
    #send an all done signal
    await queue.put(None)
    print(f'{time.ctime()} Producer: Done')
#corotine to consume work
async def consumer(queue):
    print("Consumer: Running")
    #consume work
    while True:
        #get a unit of work without blocking
        try:
            item = queue.get_nowait()
        except asyncio.QueueEmpty:
            print(f"{time.ctime()} Consumer: got nothing, waitting a whine...")
            await asyncio.sleep(0.5)
            continue   
        #check for stop
        if item is None:
            break
        print(f"{time.ctime()} >got {item}")
    #all done
    print(f"{time.ctime()} consume Done") 


async def main():
    #creat the shared queue
    queue = asyncio.Queue()
    #run the producer and cusumers
    await asyncio.gather(producer(queue), consumer(queue))

#start the asyncuo programe
asyncio.run(main())

        
                    