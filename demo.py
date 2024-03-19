from Loop import Loop
import asyncio



async def main():
    my_loop = Loop(10,lambda x: x * 2 ,1)


    for _ in range(0,5):

        x = await my_loop.async_manual_next()
        my_loop.arg +=1
        print(x)



if __name__ == "__main__":

    asyncio.run(main())

