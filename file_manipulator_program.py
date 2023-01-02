import sys
# reverse inputpath outputpath: inputpath にあるファイルを受け取り、outputpath に inputpath の内容を逆にした新しいファイルを作成します。
def reverse_str(input_str : str):
    output_str = ""
    for i in range(1, len(input_str) + 1):
        output_str += input_str[-i]
    return output_str

if sys.argv[1] == "reverse":
    with open(sys.argv[2]) as f:
        original_contents = f.read()
        reversed_file = open(sys.argv[3], 'w')
        reversed_file.write(reverse_str(original_contents))

# copy inputpath outputpath: inputpath にあるファイルのコピーを作成し、outputpath として保存します。
if sys.argv[1] == "copy":
    with open(sys.argv[2]) as f:
        original_contents = f.read()
        copy_file = open(sys.argv[3], 'w')
        copy_file.write(original_contents)

# duplicate-contents inputpath n: inputpath にあるファイルの内容を読み込み、その内容を複製し、複製された内容を inputpath に n 回複製します。
if sys.argv[1] == "duplicate-contents":
    with open(sys.argv[2], 'r+') as f:
        original_contents = f.read()
        n = int(sys.argv[3])
        if n <= 0:
            print("To duplicate content correctly, fourth argument should be bigger than zero.")
            exit()
        for i in range(n):
            print(i)
            f.write(original_contents)   

# replace-string inputpath needle newstring: inputpath' にあるファイルの内容から文字列 'needle' を検索し、'needle' の全てを 'newstring' に置き換えます。
if sys.argv[1] == "replace-string":
    f = open(sys.argv[2], 'r+')
    original_contents = f.read()
    if original_contents not in sys.argv[3]:
        print(f'{sys.argv[3]} cannot find in {sys.argv[2]}, so its content does not be changed at all.')
        exit()
    modified_contents = original_contents.replace(sys.argv[3], sys.argv[4])
    f.close()
    with open(sys.argv[2], 'w') as f:
        f.write(modified_contents)

