"""
把文件名最后一个 `_` 以后的内容删除
"""
import os

# 输入路径
tip = '文件路径：'
while True:
    path = input(tip)
    if os.path.exists(path) or os.path.lexists(path):
        break
    tip = "\n'{}' 路径不存在。\n请重新输入：".format(path)

paths = [path]
while paths:
    path = paths.pop(0)
    left = path.rindex(os.sep) + 1 if os.sep in path else 0
    right = path.rindex('.') if '.' in path[left:] else len(path)
    if '_' not in path[left:right]:
        continue
    underline_index = path.rindex('_', left, right)
    new_path = path[:underline_index] + path[right:]
    os.rename(path, new_path)
    print('{} --> {}'.format(path, new_path))
    if os.path.isdir(new_path):
        paths += [os.path.join(new_path, d) for d in os.listdir(new_path)]
