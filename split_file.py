import os
import argparse

def main():
    parser = argparse.ArgumentParser(description="split file into specified size chuncks or rebuild")
    parser.add_argument("-f", dest="filename", help="filename to split or directory to rebuild", required=True)
    parser.add_argument("-s", dest="size", help="specify size of each chunk, defualt is 25MB", default="25MB")
    parser.add_argument("-m", dest="mode", choices={"b", "s"}, help="select mode 'b' to build, 's' to split", required=True)
    parser.add_argument("-o", dest="out_dir", help="specify an output directory", default="./", required=False)
    args = parser.parse_args()
    filename = args.filename
    size = human_readable_to_int(args.size)
    mode = args.mode
    if args.out_dir[-1] is not '/':
        out_dir = args.out_dir + '/'
    else:
        out_dir = args.out_dir
    if not os.path.isdir(out_dir):
        os.mkdir(out_dir)
    if mode == 's':
        split_file(filename, size, out_dir)
    elif mode == 'b':
        build_dir(filename, out_dir)

def human_readable_to_int(size):
    if size[-2:] == "KB":
        return 1024 * int(size[:-2])
    elif size[-2:] == "MB":
        return 1024 ** 2 * int(size[:-2])
    elif size[-2:] == "GB":
        return 1024 ** 3 * int(size[:-2])
    else:
        return int(size)

def split_file(filename, size, out_dir):
    try:
        count = 0
        with open(filename, "rb") as f:
            data = f.read()
            os.mkdir("{}split.{}".format(out_dir, filename))
            for i in range(int(len(data) / size + 1)):
                nf = open("{}split.{}/{}.{}.chunk".format(out_dir,filename,i,filename), 'wb')
                nf.write(data[i * size:i * size + size])
                nf.close()
                count += 1
            with open("{}split.{}/.data".format(out_dir,filename), 'w') as nf:
                nf.write(str(count) + '\n')
                nf.write(filename)
    except Exception as e:
        print(e)
        
def build_dir(dir_filename, out_dir):
    try:
        with open(dir_filename + "/.data") as f:
            count = int(f.readline())
            filename = f.readline()
            data = b''
            for i in range(count):
                with open("{}/{}.{}.chunk".format(dir_filename,i,filename), 'rb') as f:
                    data += f.read()
            with open(out_dir + filename, "wb") as nf:
                nf.write(data)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()