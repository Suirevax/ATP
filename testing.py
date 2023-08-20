def count(f):
    def inner(a, b):
        inner.counter += 1
        return f(a, b)
    inner.counter = 0
    return inner
@count
def myadd(a,b):
    return a+b

print(myadd(1,2)) # 3
print(myadd(3,4)) # 7
print(myadd(5,6)) # 11
print('myadd.counter = ', myadd.counter) # myadd.counter = 3


def outer_function(argument):
    def inner_function():
        print(argument)
    return inner_function
give_me_the_answer = outer_function(42)
give_me_the_answer() # 42