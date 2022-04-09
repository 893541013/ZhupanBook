#封装的方法
#成员方法 （构造方法，析构方法），类方法，静态方法

class ServerInFo:

    @staticmethod      #静态方法，类名，方法   @修饰符
    def get_url(url):
        return"http://haimo.testgoup.com/{}".format(url)



# 静态方法  类名. 的方法来调用
# ServerInFo.get_url()



# def get_url(url):
#     return"http://ljtest.liuyun.tech:28080{}".format(url)
# a = get_url("/haimo/sass/systemUser/release/getLogin")
# print(a)