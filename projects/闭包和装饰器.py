def mydecorator(f_name):
    def inner_functor():
        print("登录成功")
        f_name()
    return inner_functor

@mydecorator
def payment():
    print("支付成功")

payment()

def makecounter():
    count =0
    def counter():
        nonlocal count
        count +=1
        print(f"当前计数为：{count}")
    return counter

counter = makecounter()
counter()
counter()
counter()