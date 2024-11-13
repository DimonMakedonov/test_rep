import os

def g_size(path):
    #print("g_size")
    size = 0
    if os.path.isfile(path):
        size = os.path.getsize(path)
    else:
        for dirpath,dirnames,filenames in os.walk(path):
            for filename in filenames:
                fp = os.path.join(dirpath,filename)
                if os.path.isfile(fp):
                    size += os.path.getsize(fp)
    return size

def hrs(size):
    #print("hrs")
    for unit in ['b', 'kb', 'mb', 'gb', 'tb']:
        if size < 1024:
            break
        size /= 1024
    return "{:.1f}{}".format(size,unit)

def main():
    #print("main")
    pwd = os.getcwd()
    items = os.listdir(pwd)
    s_list = []
    for item in items:
        f_path = os.path.join(pwd,item)
        size = g_size(f_path)
        s_list.append((size,item))
    s_list.sort(key=lambda x: x[0], reverse = True)
    for size, item in s_list:
        print("{} {}".format(hrs(size), item))

if __name__ == "__main__":
    main()