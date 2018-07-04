import os

with open('chname.bat', 'w') as f:
    f.write('python %s %s' % (os.path.join(os.path.dirname(os.path.abspath(__file__)), 'change_name.py'), '%1'))
