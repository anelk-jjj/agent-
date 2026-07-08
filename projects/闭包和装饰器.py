def mydecorator(f_name):
    def inner_functor():
        print("登录成功")
        f_name()
    return inner_functor

@mydecorator
def payment():
    print("支付成功")

payment()