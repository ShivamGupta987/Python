
# class Hello:
#     def run(self):
#         for i in range(5):
#             print("Hello")

# class Hi:
#     def run(self):
#         for i in range(5):
#             print('Hi')
            
# t1=Hello()

# t2=Hi()

# t1.run()

# t2.run()



# Python program to illustrate the concept
# of threading
# importing the threading module
import threading


def print_cube(num):
	# function to print cube of given num
	print("Cube: {}" .format(num * num * num))


def print_square(num):
	# function to print square of given num
	print("Square: {}" .format(num * num))


if __name__ =="__main__":
	# creating thread
	t1 = threading.Thread(target=print_square, args=(10,))
	t2 = threading.Thread(target=print_cube, args=(10,))

	# starting thread 1
	t1.start()
	# starting thread 2
	t2.start()

	# wait until thread 1 is completely executed
	t1.join()
	# wait until thread 2 is completely executed
	t2.join()

	# both threads completely executed
	print("Done!")






from time import sleep
from threading import Thread


class Hello(Thread):
    def run(self):
        for i in range(5):
            print("Hello")
            sleep(1)

class Hi(Thread):
    def run(self):
        for i in range(500):
            print('Hi')
            sleep(1)   #1 for time
t1=Hello()

t2=Hi()

t1.start()
sleep(0.2)
t2.start()




