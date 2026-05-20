import os
import shutil


def main():
    generate_content("./static", "./public", True)


def generate_content(src, dst, del_existing=False):
    if del_existing is True and os.path.exists(dst):
        shutil.rmtree(dst)
    os.mkdir(dst)
    dir_items = os.listdir(src)
    for i in dir_items:
        print(f"Item in directory is {i}")
        if os.path.isfile(os.path.join(src, i)):
            # Found a file, copying over
            shutil.copy(os.path.join(src, i), os.path.join(dst, i))
        else:
            # Found a folder, dig deeper
            generate_content(os.path.join(src, i), os.path.join(dst, i))


if __name__ == "__main__":
    main()
