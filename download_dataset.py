import os

# 打开并读取文件
with open('repositories.txt', 'r') as file:
    lines = file.readlines()

# 对于每一个仓库链接，执行git clone命令
for line in lines:
    os.system(f'git clone {line.strip()}')