import os
import datetime
import shutil

# for i in range(100):
#     with open(f"{i}.txt", "w") as f:
#         f.write(str(i))

txt_data = [file for file in os.listdir() if file.endswith(".txt")]
print(txt_data)

PATH_ODD = 'data/odd'
PATH_EVEN = 'data/even'
# os.makedirs('data')
# os.makedirs('data/odd', exist_ok=True)
# os.makedirs('data/even', exist_ok=True)

# for file in txt_data:
#     if int(file[:-4]) % 2 == 0:
#         os.replace(file, os.path.join(PATH_EVEN, file))
#     else:
#         os.replace(file, os.path.join(PATH_ODD, file))

# txt_files = []
# for file_tuple in os.walk('data'):
#     if file_tuple[2]:
#         txt_files.extend(file_tuple[2])
#
# print(*txt_files)

# for file_tuple in os.walk('data'):
#     if file_tuple[2]:
#         for file in file_tuple[2]:
#             os.rename(os.path.join(file_tuple[0], file), file)

# print(*os.walk('data'))

# print(oct(os.stat('data/even/0.txt').st_mode)[-3:])
# print(os.stat('data/even/0.txt').st_size)
# print(datetime.datetime.fromtimestamp(os.stat('data/even/0.txt').st_mtime))
# print(datetime.datetime.fromtimestamp(os.stat('data/even/0.txt').st_atime))
#
# print(oct(os.stat('data/odd/1.txt').st_mode)[-3:])
# print(os.stat('data/odd/1.txt').st_size)
# print(datetime.datetime.fromtimestamp(os.stat('data/odd/1.txt').st_mtime))
# print(datetime.datetime.fromtimestamp(os.stat('data/odd/1.txt').st_atime))
#
# os.makedirs('copy_data/even', exist_ok=True)
# os.makedirs('copy_data/odd', exist_ok=True)
# shutil.copy('data/even/0.txt', 'copy_data/even/0.txt')
# shutil.copy2('data/odd/1.txt', 'copy_data/odd/1.txt')
#
# print(oct(os.stat('copy_data/even/0.txt').st_mode)[-3:])
# print(os.stat('copy_data/even/0.txt').st_size)
# print(datetime.datetime.fromtimestamp(os.stat('copy_data/even/0.txt').st_mtime))
# print(datetime.datetime.fromtimestamp(os.stat('copy_data/even/0.txt').st_atime))
#
# print(oct(os.stat('copy_data/odd/1.txt').st_mode)[-3:])
# print(os.stat('copy_data/odd/1.txt').st_size)
# print(datetime.datetime.fromtimestamp(os.stat('copy_data/odd/1.txt').st_mtime))
# print(datetime.datetime.fromtimestamp(os.stat('copy_data/odd/1.txt').st_atime))

# os.remove('copy_data/odd/1.txt')
# os.rmdir('copy_data/odd')
# shutil.rmtree('copy_data')

# for i in range(20):
#     with open(f"txt.{i}", "w") as f:
#         f.write(str(i))

folders = [folder for folder in os.listdir() if os.path.isfile(folder)]
print(dir(os.path))
# print(*folders)
print(os.path.split(os.getcwd()))