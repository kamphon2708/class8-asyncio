# {time.ctime()} Producer Running
# Consumer: Running
# Wed Aug 23 14:43:20 2023 Consumer: gave up waitting 
# Wed Aug 23 14:43:20 2023 >got 0.4709857607762512
# Wed Aug 23 14:43:20 2023 Consumer: gave up waitting 
# Wed Aug 23 14:43:21 2023 >got 0.8149640440234326
# Wed Aug 23 14:43:21 2023 Consumer: gave up waitting 
# Wed Aug 23 14:43:22 2023 >got 0.8710029994139191
# Wed Aug 23 14:43:22 2023 >got 0.12389697223055574
# Wed Aug 23 14:43:22 2023 >got 0.07717339571356296
# Wed Aug 23 14:43:22 2023 Consumer: gave up waitting 
# Wed Aug 23 14:43:23 2023 >got 0.9434406660023076
# Wed Aug 23 14:43:23 2023 Consumer: gave up waitting 
# Wed Aug 23 14:43:24 2023 >got 0.9547066033204944
# Wed Aug 23 14:43:24 2023 Consumer: gave up waitting 
# Wed Aug 23 14:43:24 2023 >got 0.6833186718128855
# Wed Aug 23 14:43:25 2023 Consumer: gave up waitting 
# Wed Aug 23 14:43:25 2023 >got 0.8358769094381646
# Wed Aug 23 14:43:26 2023 Consumer: gave up waitting 
# Wed Aug 23 14:43:26 2023 Producer: Done
# Wed Aug 23 14:43:26 2023 >got 0.6418488336174314
# Wed Aug 23 14:43:26 2023 consume Done


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
            #retrive the get() awaittable
            get_await = queue.get()
            item = await asyncio.wait_for(get_await, 0.5)
        except asyncio.TimeoutError:
            print(f"{time.ctime()} Consumer: gave up waitting ")
          
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

        
                    