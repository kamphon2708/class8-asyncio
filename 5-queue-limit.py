# we will create a producer coroutine that will generate ten random numbers
# and put them on the queue. We will also create a consumer coroutine
# that will get numbers from the queue and report their values.


# Wed Aug 23 15:05:16 2023 Consumer: Running
# Wed Aug 23 15:05:16 2023 Producer: Running
# Wed Aug 23 15:05:16 2023 Producer: Running
# Wed Aug 23 15:05:16 2023 Producer: Running
# Wed Aug 23 15:05:16 2023 Producer: Running
# Wed Aug 23 15:05:16 2023 Producer: Running
# Wed Aug 23 15:05:16 2023 > got 0.8668196892572753
# Wed Aug 23 15:05:17 2023 > got 0.36008538145113556
# Wed Aug 23 15:05:17 2023 > got 0.7123505499534486
# Wed Aug 23 15:05:18 2023 > got 0.7135086267771602
# Wed Aug 23 15:05:19 2023 > got 0.16703242414480202
# Wed Aug 23 15:05:19 2023 > got 0.16424570013515294
# Wed Aug 23 15:05:19 2023 > got 0.0723915698340949
# Wed Aug 23 15:05:19 2023 > got 0.562979863582528
# Wed Aug 23 15:05:20 2023 > got 0.5700192469795254
# Wed Aug 23 15:05:20 2023 > got 0.37450764640504663
# Wed Aug 23 15:05:21 2023 > got 0.3389277349167277
# Wed Aug 23 15:05:21 2023 > got 0.7932903037753077
# Wed Aug 23 15:05:22 2023 > got 0.7584108351760707
# Wed Aug 23 15:05:23 2023 > got 0.06350880856643504
# Wed Aug 23 15:05:23 2023 > got 0.864620913927457
# Wed Aug 23 15:05:23 2023 > got 0.15067013559940468
# Wed Aug 23 15:05:24 2023 > got 0.20547972016943827
# Wed Aug 23 15:05:24 2023 > got 0.6123316276573629
# Wed Aug 23 15:05:24 2023 > got 0.8031860035116117
# Wed Aug 23 15:05:25 2023 > got 0.5270237493485245
# Wed Aug 23 15:05:26 2023 > got 0.04833566498334463
# Wed Aug 23 15:05:26 2023 > got 0.2018248476562211
# Wed Aug 23 15:05:26 2023 > got 0.03290136912333963
# Wed Aug 23 15:05:26 2023 > got 0.14941352349912596
# Wed Aug 23 15:05:26 2023 > got 0.833702515976745
# Wed Aug 23 15:05:27 2023 > got 0.7444462585618168
# Wed Aug 23 15:05:28 2023 > got 0.27495454568885
# Wed Aug 23 15:05:28 2023 > got 0.6378124624335483
# Wed Aug 23 15:05:29 2023 > got 0.19359745696662511
# Wed Aug 23 15:05:29 2023 > got 0.30233573754728205
# Wed Aug 23 15:05:29 2023 > got 0.5342320083996165
# Wed Aug 23 15:05:30 2023 > got 0.01083373999275028
# Wed Aug 23 15:05:30 2023 > got 0.12217668440388507
# Wed Aug 23 15:05:30 2023 > got 0.09078729055583756
# Wed Aug 23 15:05:30 2023 > got 0.5444034396135315
# Wed Aug 23 15:05:31 2023 > got 0.06032885091932416
# Wed Aug 23 15:05:31 2023 Producer 1: Done
# Wed Aug 23 15:05:31 2023 > got 0.614689570946161
# Wed Aug 23 15:05:31 2023 > got 0.11754774691329084
# Wed Aug 23 15:05:31 2023 > got 0.49724938168524424
# Wed Aug 23 15:05:32 2023 > got 0.3990519454290299
# Wed Aug 23 15:05:32 2023 > got 0.2831467357958095
# Wed Aug 23 15:05:33 2023 > got 0.1079248281044064
# Wed Aug 23 15:05:33 2023 > got 0.7862399141115263
# Wed Aug 23 15:05:34 2023 > got 0.32113424662112977
# Wed Aug 23 15:05:34 2023 > got 0.8152061676435766
# Wed Aug 23 15:05:34 2023 Producer 3: Done
# Wed Aug 23 15:05:35 2023 > got 0.6775484491483098
# Wed Aug 23 15:05:35 2023 Producer 4: Done
# Wed Aug 23 15:05:35 2023 > got 0.3041839428989156
# Wed Aug 23 15:05:36 2023 > got 0.3238076327596905
# Wed Aug 23 15:05:36 2023 Producer 5: Done
# Wed Aug 23 15:05:36 2023 > got 0.4762607449722839
# Wed Aug 23 15:05:37 2023 > got 0.3824756634791623



from random import random
import asyncio
import time

# coroutine to generate work


async def producer(queue,id):
    print(f"{time.ctime()} Producer: Running")
    # generate work
    for i in range(10):
        # generate work
        value = random()
        # block to simulate work
        await asyncio.sleep((id+1) * 0.1)
        # add to the queue
        await queue.put(value)
        # print(f'{time.ctime()} Producer: put {value}')
    print(f"{time.ctime()} Producer {id+1}: Done")

# coroutine to consume work


async def consumer(queue):
    print(f"{time.ctime()} Consumer: Running")
    # consume work
    while True:

        # get a unit of work without blocking

        item = await queue.get()
        # report
        print(f"{time.ctime()} > got {item}")

        # check for stop signal
        if item:
            await asyncio.sleep(item)

        queue.task_done()


# entry point corotine
async def main():
    # create the shared queue
    queue = asyncio.Queue(2)
    # start the consumer
    _ = asyncio.create_task(consumer(queue))
    # start the producer and wait for it to finish
    producers = [producer(queue,i) for i in range(5)]

    await asyncio.gather(*producers)
    # wait for all items to be processed
    await queue.join()

# start the asyncio program
asyncio.run(main())

