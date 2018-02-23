class Dog:

    # 私有方法__send_msg，不给外部直接使用，先验证通过然后再调用
    def __send_msg(self):
        print("----正在发送短信----")

    # 公有方法
    def send_msg(self, new_money):
        if new_money > 10000:
            self.__send_msg()
        else:
            print("余额不足请先充值")


dog = Dog()

# dog.__send_msg()
dog.send_msg(10000000)
