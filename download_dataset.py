import os

# 打开并读取文件
with open('repositories.txt', 'r') as file:
    lines = file.readlines()

target_directory = '../../datasets/AI-interview'
# 对于每一个仓库链接，执行git clone命令
for line in lines:
    repo_name = line.strip().split('/')[-1].split('.')[0]
    os.system(f'git clone {line.strip()} {os.path.join(target_directory, repo_name)}')