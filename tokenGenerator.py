import random
def token_Generator():
    """
    token生成方法
    返回值：token值
    """
    token = ""
    t = "1234567890abcdefghijklmnoqprstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(32):
        token = token + random.choice(t)

    return token


