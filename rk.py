class File:
    def __init__(self, file_id, name, size):
        self.file_id = file_id
        self.name = name
        self.size = size
        self.directories = []

    def add_directory(self, directory):
        self.directories.append(directory)


class Directory:
    def __init__(self, dir_id, name):
        self.dir_id = dir_id
        self.name = name
        self.files = []

    def add_file(self, file):
        self.files.append(file)
        file.add_directory(self)

    def average_file_size(self):
        if len(self.files) == 0:
            return 0
        total_size = sum(file.size for file in self.files)
        return round(total_size / len(self.files), 2)



file1 = File(1, "file1.txt", 10)
file2 = File(2, "file2.txt", 20)
file3 = File(3, "file3.txt", 30)
file4 = File(4, "file4.txt", 25)
file5 = File(5, "apple.txt", 15)

dir1 = Directory(1, "Каталог файлов 1")
dir2 = Directory(2, "Каталог файлов 2")
dir3 = Directory(3, "Другой каталог")

dir1.add_file(file1)
dir1.add_file(file2)
dir2.add_file(file3)
dir2.add_file(file4)
dir3.add_file(file5)


def query_1(directories):
    return [
        (directory.name, [file.name for file in directory.files])
        for directory in directories if "Каталог файлов" in directory.name
    ]

def query_2(directories):
    return sorted(
        [(directory.name, directory.average_file_size()) for directory in directories],
        key=lambda x: x[1]
    )

def query_3(files):
    return [
        (file.name, [directory.name for directory in file.directories])
        for file in files if file.name.lower().startswith('a')
    ]


directories = [dir1, dir2, dir3]
files = [file1, file2, file3, file4, file5]

print("Запрос 1:")
result_1 = query_1(directories)
for dir_name, files_list in result_1:
    print(f"{dir_name}: {', '.join(files_list)}")

print("\nЗапрос 2:")
result_2 = query_2(directories)
for dir_name, avg_size in result_2:
    print(f"{dir_name}: Средняя загруженность = {avg_size} МБ")

print("\nЗапрос 3:")
result_3 = query_3(files)
for file_name, dirs in result_3:
    print(f"{file_name}: Каталоги - {', '.join(dirs)}")