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
    filename = re.sub('\[.*?www.*?\]', '', filename).strip()  #re.sub()将filename中匹配'\[.*?\]'的字符串替换为''
    filename = re.sub('【.*?www.*?】'.decode(file_encoding), '', filename).strip()  #re.sub()将filename中匹配'\【.*?\】'的字符串替换为''
    filename = filename.strip('.').strip('-')
    filename = filename.strip('-').strip('.')
    return '%s.%s'%(filename,suffix)

def main():
    '''电影销毁器主程序'''
    filename = sys.argv[1]


if __name__ == '__main__':
    main()
