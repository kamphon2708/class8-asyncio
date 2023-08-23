# we will create a producer coroutine that will generate ten random numbers 
# and put them on the queue. We will also create a consumer coroutine 
# that will get numbers from the queue and report their values.

# {time.ctime()} Consumer Running
# {time.ctime()} Producer Running
# {time.ctime()} Producer:Done
# Wed Aug 23 14:42:40 2023 > got 0.16610177407967208
# {time.ctime()} Producer:Done
# Wed Aug 23 14:42:40 2023 > got 0.2740151635480461
# {time.ctime()} Producer:Done
# Wed Aug 23 14:42:41 2023 > got 0.8000310054567181
# {time.ctime()} Producer:Done
# Wed Aug 23 14:42:42 2023 > got 0.26776513970744054
# {time.ctime()} Producer:Done
# Wed Aug 23 14:42:42 2023 > got 0.7630162418466409
# {time.ctime()} Producer:Done
# Wed Aug 23 14:42:43 2023 > got 0.9331862617805463
# {time.ctime()} Producer:Done
# Wed Aug 23 14:42:44 2023 > got 0.1316464452942907
# {time.ctime()} Producer:Done
# Wed Aug 23 14:42:44 2023 > got 0.9772363246298266
# {time.ctime()} Producer:Done
# Wed Aug 23 14:42:45 2023 > got 0.5260459330025866
# {time.ctime()} Producer:Done
# Wed Aug 23 14:42:45 2023 Producer: Done
# Wed Aug 23 14:42:46 2023 > got 0.6975331687170059
# Wed Aug 23 14:42:46 2023 > got None



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
         #report
         print(f"{time.ctime()} > got {item}")
         #block whilr precessing

         if item :
             await asyncio.sleep(item)
        #mark the task as done
         queue.task_done()
         
#entry point corotine
async def main():
    #creat the shared queue
    queue = asyncio.Queue()
    #start tje consumer
    _ = asyncio.create_task(consumer(queue))
    #start the producer and wait for it to finiched
    await asyncio.create_task(producer(queue))
    #wait for all item to be processd
    await queue.join()

#start the asyncuo programe
asyncio.run(main())