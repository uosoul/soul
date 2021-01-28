def double_list(lst):
    for index, item in enumerate(lst):
        if isinstance(item, bool):
            continue
        if isinstance(item, (int, float)):
            lst[index] *= 2
        if isinstance(item, list):
            double_list(item)
    return lst

if __name__ == '__main__':
    lst = [1, [4, 6], True]
    double_list(lst)
    print(lst)
    import sys
    print(sys.argv)
##import os
##print(os.getcwd())  #获取当前目录
###os.chdir('第二章字符串')   #改变当前目录为 输入值
##os.listdir(path='.')   #输出当前文件夹的各个文件名
##os.mkdir('file')  #在当前文件夹 创建 file文件夹
##os.rename('file','new_file')   #重命名
## 
a = double_list([1,5,9])
