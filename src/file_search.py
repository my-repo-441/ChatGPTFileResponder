import os

def search_files(directory, extension):
    print(directory,extension)
    files_list = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(extension):
                files_list.append(os.path.join(root, file))
                print(file)
    return files_list
