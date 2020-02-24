# split_file
Splits a file into chunks of a defined size and rebuilds it

```
usage: split_file.py [-h] -f FILENAME [-s SIZE] -m {s,b}

split file into specified size chuncks or rebuild

optional arguments:
  -h, --help   show this help message and exit
  -f FILENAME  filename to split or directory to rebuild
  -s SIZE      specify size of each chunk, defualt is 25MB
  -m {s,b}     select mode 'b' to build, 's' to split
  ```