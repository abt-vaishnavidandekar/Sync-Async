import asyncio

async def open_file1():
    file = open("c1.txt",'a')
    await asyncio.sleep(3)
    a = input("Enter the data: ")
    file.write(f"{a}\n")
    file.close()

    file1 = open("c1.txt",'r')
    data = file1.read()
    print("file 1",data)
    file1.close()

async def open_file2():
    file = open("c2.txt",'a')
    await asyncio.sleep(5)
    a = input("Enter the data: ")
    file.write(f"{a}\n")
    file.close()

    file1 = open("c2.txt",'r')
    data = file1.read()
    print("file 2",data)
    file1.close()

async def open_file3():
    file = open("c3.txt",'a')
    await asyncio.sleep(9)
    a = input("Enter the data: ")
    file.write(f"{a}\n")
    file.close()

    file1 = open("c3.txt",'r')
    data = file1.read()
    print("file 3",data)
    file1.close()

async def open_file4():
    file = open("c4.txt",'a')
    await asyncio.sleep(1)
    a = input("Enter the data: ")
    file.write(f"{a}\n")
    file.close()

    file1 = open("c4.txt",'r')
    data = file1.read()
    print("file 4",data)
    file1.close()

async def main():
    await asyncio.gather(open_file1(), open_file2(), open_file3(), open_file4())

asyncio.run(main())