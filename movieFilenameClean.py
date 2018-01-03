#coding=utf-8
import os
import re
import sys

# 编码信息
input_encoding = sys.stdin.encoding
output_encoding = sys.stdout.encoding
file_encoding = 'utf8'

def filenameClean(fullfilename):
    '''清除电影文件名中的广告部分'''
    suffix = fullfilename.split('.')[-1]
    filename = fullfilename[:-len(suffix)-1]
    # 判断是否是电影文件，如果不是，原样返回
    if suffix.lower() not in ['asf', 'avi', 'flv', 'mkv', 'mov', 'mp4', 'mpeg', 'mpg', 'qt', 'ra', 'ram', 'rm', 'rmvb', 'viv', 'wmv']:
        return fullfilename
    # 是电影文件，继续处理
    # 净化文件名
    filename = re.sub('\[.*?www.*?\]', '', filename.lower()).strip()  # re.sub()将filename中匹配'\[.*?\]'的字符串替换为''
    filename = re.sub('\[.*?.com*?\]', '', filename.lower()).strip()  
    filename = re.sub('【.*?www.*?】'.decode(file_encoding), '', filename.lower()).strip()  # re.sub()将filename中匹配'\【.*?\】'的字符串替换为''
    filename = re.sub('【.*?.com*?】'.decode(file_encoding), '', filename.lower()).strip()  # re.sub()将filename中匹配'\【.*?\】'的字符串替换为''
    filename = filename.strip('.').strip('-')
    filename = filename.strip('-').strip('.')
    return '%s.%s'%(filename,suffix)

def main():
    '''电影文件名清理程序主程序'''
    # 遍历当前目录下的文件
    for filename in os.listdir(os.getcwd()):
        filename = filename.decode(input_encoding)

        # 本文件不处理
        if filename == "movieFilenameClean.py":
            continue

        # 对文件名进行清理
        new_filename = filenameClean(filename)
        
        # 如果文件名没有变化，处理下一个文件
        if new_filename == filename:
            continue

        # 对文件进行重命名
        os.rename(filename,new_filename) #对文件进行重命名

if __name__ == '__main__':
    main()
