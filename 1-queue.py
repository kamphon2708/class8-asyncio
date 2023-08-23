# we will create a producer coroutine that will generate ten random numbers 
# and put them on the queue. We will also create a consumer coroutine 
# that will get numbers from the queue and report their values.

# {time.ctime()} Producer Running
# {time.ctime()} Consumer Running
# {time.ctime()} Producer:Done
# Wed Aug 23 14:44:19 2023 consumer: Done
# {time.ctime()} Producer:Done
# Wed Aug 23 14:44:20 2023 consumer: Done
# {time.ctime()} Producer:Done
# Wed Aug 23 14:44:20 2023 consumer: Done
# {time.ctime()} Producer:Done
# Wed Aug 23 14:44:21 2023 consumer: Done
# {time.ctime()} Producer:Done
# Wed Aug 23 14:44:21 2023 consumer: Done
# {time.ctime()} Producer:Done
# Wed Aug 23 14:44:21 2023 consumer: Done
# {time.ctime()} Producer:Done
# Wed Aug 23 14:44:22 2023 consumer: Done
# {time.ctime()} Producer:Done
# Wed Aug 23 14:44:23 2023 consumer: Done
# {time.ctime()} Producer:Done
# Wed Aug 23 14:44:23 2023 consumer: Done
# {time.ctime()} Producer:Done
# Wed Aug 23 14:44:23 2023 Producer: Done
# Wed Aug 23 14:44:23 2023 consumer: Done
# Wed Aug 23 14:44:23 2023 consumer: Done


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
        print('{time.ctime()} Producer:Done')
    #send an all done signal
    await queue.put(None)
    print(f'{time.ctime()} Producer: Done')
#corotine to consume work
async def consumer(queue):
    print('{time.ctime()} Consumer Running')
     #consume work
    while True:
         #get a unit of work
         item = await queue.get()
         #check for stop sinnal
         if item is None:
             break
         #report
         print(f"{time.ctime()} consumer: Done")
    #all done
    print(f"{time.ctime()} consumer: Done")

#entry point corotine
async def main():
    #creat the shared queue
    queue = asyncio.Queue()
    #run the producer and cusumers
    await asyncio.gather(producer(queue), consumer(queue))

#start the asyncuo programe
asyncio.run(main())