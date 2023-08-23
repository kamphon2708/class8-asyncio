# we will create a producer coroutine that will generate ten random numbers 
# and put them on the queue. We will also create a consumer coroutine 
# that will get numbers from the queue and report their values.

# {time.ctime()} Consumer Running
# {time.ctime()} Producer Running
# {time.ctime()} Producer Running
# {time.ctime()} Producer Running
# {time.ctime()} Producer Running
# {time.ctime()} Producer Running
# {time.ctime()} Producer Running
# {time.ctime()} Producer:Done
# Wed Aug 23 14:40:42 2023 > got 0.2990836200966219
# {time.ctime()} Producer:Done
# {time.ctime()} Producer:Done
# Wed Aug 23 14:40:43 2023 > got 0.42426788724465014
# {time.ctime()} Producer:Done
# Wed Aug 23 14:40:43 2023 > got 0.43178255473492533
# {time.ctime()} Producer:Done
# Wed Aug 23 14:40:44 2023 > got 0.4326731085852714
# {time.ctime()} Producer:Done
# Wed Aug 23 14:40:44 2023 > got 0.7647313669078647
# {time.ctime()} Producer:Done
# Wed Aug 23 14:40:45 2023 > got 0.9053437299889892
# {time.ctime()} Producer:Done
# Wed Aug 23 14:40:46 2023 > got 0.37536661156719053
# {time.ctime()} Producer:Done
# Wed Aug 23 14:40:46 2023 > got 0.5450051742728897
# {time.ctime()} Producer:Done
# Wed Aug 23 14:40:47 2023 > got 0.7351538046430857
# {time.ctime()} Producer:Done
# Wed Aug 23 14:40:47 2023 > got 0.09146038062632023
# {time.ctime()} Producer:Done
# Wed Aug 23 14:40:48 2023 > got 0.7912681199641328
# {time.ctime()} Producer:Done
# Wed Aug 23 14:40:48 2023 > got 0.020570006581942746
# {time.ctime()} Producer:Done
# Wed Aug 23 14:40:48 2023 > got 0.5543096541957684
# {time.ctime()} Producer:Done
# Wed Aug 23 14:40:49 2023 > got 0.43528891869364106
# {time.ctime()} Producer:Done
# Wed Aug 23 14:40:49 2023 > got 0.991061661380886
# {time.ctime()} Producer:Done
# Wed Aug 23 14:40:50 2023 > got 0.9149743096907466
# {time.ctime()} Producer:Done
# Wed Aug 23 14:40:51 2023 > got 0.5763238379263176
# {time.ctime()} Producer:Done
# Wed Aug 23 14:40:52 2023 > got 0.665466190630158
# {time.ctime()} Producer:Done
# Wed Aug 23 14:40:53 2023 > got 0.6197286514035242
# {time.ctime()} Producer:Done
# Wed Aug 23 14:40:53 2023 > got 0.9885778873859614
# {time.ctime()} Producer:Done
# Wed Aug 23 14:40:54 2023 > got 0.998180705273892
# {time.ctime()} Producer:Done
# Wed Aug 23 14:40:55 2023 > got 0.1473129766900857
# {time.ctime()} Producer:Done
# Wed Aug 23 14:40:55 2023 > got 0.9599391506165922
# {time.ctime()} Producer:Done
# Wed Aug 23 14:40:56 2023 > got 0.32946004466535794
# {time.ctime()} Producer:Done
# Wed Aug 23 14:40:57 2023 > got 0.10762693840520521
# {time.ctime()} Producer:Done
# Wed Aug 23 14:40:57 2023 > got 0.8324594972060795
# {time.ctime()} Producer:Done
# Wed Aug 23 14:40:58 2023 > got 0.038579496298373095
# {time.ctime()} Producer:Done
# Wed Aug 23 14:40:58 2023 > got 0.7290426241525505
# {time.ctime()} Producer:Done
# Wed Aug 23 14:40:58 2023 > got 0.30971593776185247
# {time.ctime()} Producer:Done
# Wed Aug 23 14:40:59 2023 > got 0.5394682448433754
# {time.ctime()} Producer:Done
# Wed Aug 23 14:40:59 2023 > got 0.41037968084744114
# {time.ctime()} Producer:Done
# Wed Aug 23 14:41:00 2023 > got 0.5530935349939822
# {time.ctime()} Producer:Done
# Wed Aug 23 14:41:00 2023 > got 0.6542483029669937
# {time.ctime()} Producer:Done
# Wed Aug 23 14:41:01 2023 > got 0.5492176166323167
# {time.ctime()} Producer:Done
# Wed Aug 23 14:41:02 2023 > got 0.5675407246725913
# {time.ctime()} Producer:Done
# Wed Aug 23 14:41:02 2023 > got 0.664577028915714
# {time.ctime()} Producer:Done
# Wed Aug 23 14:41:03 2023 > got 0.32412788219169597
# {time.ctime()} Producer:Done
# Wed Aug 23 14:41:03 2023 > got 0.9260950680707455
# {time.ctime()} Producer:Done
# Wed Aug 23 14:41:04 2023 > got 0.7637592608018587
# {time.ctime()} Producer:Done
# Wed Aug 23 14:41:05 2023 > got 0.820691602335835
# {time.ctime()} Producer:Done
# Wed Aug 23 14:41:06 2023 > got 0.6199672187202315
# {time.ctime()} Producer:Done
# Wed Aug 23 14:41:06 2023 > got 0.9649724589393138
# {time.ctime()} Producer:Done
# Wed Aug 23 14:41:07 2023 > got 0.9533191970301588
# {time.ctime()} Producer:Done
# Wed Aug 23 14:41:08 2023 > got 0.8268036522854384
# {time.ctime()} Producer:Done
# Wed Aug 23 14:41:09 2023 > got 0.15468448025716808
# {time.ctime()} Producer:Done
# Wed Aug 23 14:41:09 2023 > got 0.5423214760069298
# {time.ctime()} Producer:Done
# Wed Aug 23 14:41:10 2023 > got 0.41263498959678846
# {time.ctime()} Producer:Done
# Wed Aug 23 14:41:10 2023 > got 0.24026357580240143
# {time.ctime()} Producer:Done
# Wed Aug 23 14:41:10 2023 > got 0.15692501545167847
# {time.ctime()} Producer:Done
# Wed Aug 23 14:41:11 2023 > got 0.45210312052778545
# {time.ctime()} Producer:Done
# Wed Aug 23 14:41:11 2023 > got 0.4185866145984317
# {time.ctime()} Producer:Done
# Wed Aug 23 14:41:11 2023 > got 0.17108745172263762
# {time.ctime()} Producer:Done
# Wed Aug 23 14:41:12 2023 > got 0.20985841754731183
# {time.ctime()} Producer:Done
# Wed Aug 23 14:41:12 2023 > got 0.1091490829789864
# {time.ctime()} Producer:Done
# Wed Aug 23 14:41:12 2023 > got 0.5819017496662037
# {time.ctime()} Producer:Done
# Wed Aug 23 14:41:13 2023 > got 0.5351302855823233
# {time.ctime()} Producer:Done
# Wed Aug 23 14:41:13 2023 > got 0.5883623094492358
# Wed Aug 23 14:41:13 2023 Producer: Done
# Wed Aug 23 14:41:14 2023 > got 0.8109913866694286
# {time.ctime()} Producer:Done
# Wed Aug 23 14:41:15 2023 > got None
# Wed Aug 23 14:41:15 2023 > got 0.5667454879150585
# Wed Aug 23 14:41:15 2023 Producer: Done
# Wed Aug 23 14:41:15 2023 Producer: Done
# Wed Aug 23 14:41:15 2023 > got None
# Wed Aug 23 14:41:15 2023 > got None
# {time.ctime()} Producer:Done
# Wed Aug 23 14:41:15 2023 Producer: Done
# Wed Aug 23 14:41:15 2023 > got 0.2951653747671251
# Wed Aug 23 14:41:15 2023 Producer: Done
# Wed Aug 23 14:41:15 2023 > got None
# Wed Aug 23 14:41:15 2023 > got None
# Wed Aug 23 14:41:15 2023 Producer: Done
# Wed Aug 23 14:41:15 2023 > got None
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
    queue = asyncio.Queue(2)
    #start tje consumer
    _ = asyncio.create_task(consumer(queue))
    producers = [producer(queue) for _ in range(6)]
    #run and wait for the producers to finiched
   
    await asyncio.gather(*producers)
    #wait for all item to be processd
    await queue.join()

#start the asyncuo programe
asyncio.run(main())