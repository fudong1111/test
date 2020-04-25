
from os import path

import re


class processmod():

    def __init__(self, path):
        # self.filapath =  os.path.join(os.path.split(os.path.realpath(__file__))[0],path)
        self.filapath = os.path.join(os.path.dirname(__file__), path)
        print("路径创建成功", self.filapath)

    def deletecn(self):
        with open(self.filapath, 'r', encoding='utf-8') as file:
            txt = file.read()
            newtxt = self.remove_punctuation(txt)
        with open(self.filapath, 'w', encoding='utf-8') as file:
            file.write(newtxt)

    def remove_punctuation(self, line):
        #\u4e00-\u9fa5  为汉字范围
        # rule = re.compile(ur"[^a-zA-Z0-9\u4e00-\u9fa5]")
        rule = re.compile('[\u4e00-\u9fa5]')  # 匹配汉字
        line = rule.sub('', line)  # 将汉字转换为空
        print(line)
        return line

if __name__ == "__main__":
    a = processmod('a.txt')
    a.deletecn()
