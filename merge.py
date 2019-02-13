import shutil, os


def main():
    target_location = 'C:\\Users\\Atheist8E\\Documents\\Satyagraha\\Convert_Greyscale\\altar'
    target_filename = 'file_list.txt'
    with open(target_location + '\\' + target_filename,'w') as f:
        location = 'C:\\Users\\Atheist8E\\Desktop\\Current\\Computer_Vision\\Dataset\\101_ObjectCategories'
        for folderName, subfolders, filenames in os.walk(location):
            for filename in filenames:
                f.write(folderName + '\n')
                f.write(filename + '\n')
        

if __name__ == "__main__":
    main()
