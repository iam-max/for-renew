import random
import string

def generate_password(length):
    # 定义密码字符集
    chars = string.ascii_letters + string.digits + string.punctuation
    # 生成随机密码
    password = "".join(random.choice(chars) for _ in range(length))
    return password

if __name__ == "__main__":
    # 输入密码长度和数量
    length = int(input("请输入密码长度: "))
    count = int(input("请输入密码数量: "))
    # 输出随机密码
    for i in range(count):
        print(f"密码{i+1}: {generate_password(length)}")
