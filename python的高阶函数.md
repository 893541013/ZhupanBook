# 高阶函数
- python3提供了很多高阶函数的使用，统一把工具封装到functools标准库里面
    - reduce
    ```python
        from functools import reduce

    def test(s1,s2):
        return s1+s2

    reduce(test,[1,2,3,4,5])   #注意reduce不是for循环，第一个参数是test，第二个参数是一个可序列化的参数
    ```


    - partial
    ```python
        from functools import partial

    def test1(s1,s2):
        return s1+s2

    add = partial(test1,1)
    # add 变成了
    # def test2（s2）：
    #    return 1+s2

    #print（add（100，200））   # 此时就多传入了一个参数 typeerror
    print(add(100))
    ```


    - wraps:是为了消除装饰器对原函数的影响
    ```python
        from functools import wraps
    def a(f):
        # wraps 的参数f实际上是被装饰函数，这个前面装饰器的调用链路就可以得知
        @wraps(f)    # wraps 实际上的底层方法就是partial，通过partial函数来帮顶原有的内置属性，以此保证被装饰器的函数不受影响
        def b(*args,**kwargs):
            print("b")
            return f()
        return b

    @a  # @a   相当于  t（） == a（t）  相当于 把 被装饰函数 传给了装饰器函数作为装饰器函数的参数
    def t():
        print("t")

    print(t.__name__)  #这里不用wraps 消除装饰器对被装饰函数的内置属性的修改的话
    #应该打印的是 b

    #经过被装饰后的函数，它的内置属性已经改变了，并不是在运行被装饰函数，实际上
    # 在运行装饰器函数里面生成的原函数的副本
    # 一个函数被装饰之后，实际上他就已经改变了，wraps方法就是在消除这种影响
    ```
