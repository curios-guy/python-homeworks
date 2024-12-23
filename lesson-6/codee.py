# def rrange(start, stop = None, step =1):
#     if stop == None:
#         stop = start
#         start = 0
    
#     num = start
#     while num < start:
#         yield num
#         num+=step

# nums = rrange(10, 20, 2)
# print(nums)
# for i in nums:
#     print(i)


def repeat(n):
    def d(func):
        def wrapper(name):
            for __ in range(n):
                func(name)

        wrapper.__name__ = func.__name__

        return wrapper
    return d

@repeat(14)
def greet(namee):
    print(f"Hello {namee}")

greet("Alish")