import sys
import os

CHANGE_SIGN = '_'


def ch_name(old, new):
    try:
        os.renames(old, new)
    except Exception as e:
        input('ERROR>>\n %s' % e)

file = sys.argv[1]

# 进入文件夹
try:
    os.chdir(file)
    # 进入成功则获取里面的文件名列表
    files = os.listdir('./')
except:
    # 进入失败则表示这就是一个文件而不是文件夹
    files = [file]
for file in files:
    if '.' not in file:
        end_num, end_str = None, ''
    else:
        # 后缀的.的位置
        end_num = file.rfind('.')
        # 后缀
        end_str = file[end_num:]

    if CHANGE_SIGN not in file[:end_num]:
        continue

    # _ 的位置
    _num = file.rfind(CHANGE_SIGN, 0, end_num)
    # 新名字
    new_name = file[:_num] + end_str
    ch_name(file, new_name)
