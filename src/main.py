import os
import shutil

from markdown_conversion import markdown_to_html_node


def main():
    generate_content("./static", "./public", True)
    generate_page("./content/index.md", "./template.html", "./public/index.html")


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


def extract_title(markdown):
    title = ""
    with open(markdown, "r") as file:
        for line in file:
            if line.startswith("# "):
                title = line[2:].strip()
    return title


def generate_page(from_path, template_path, dest_path):
    print(f"Generating a page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, "r") as file:
        from_content = file.read()

    with open(template_path, "r") as file:
        template_content = file.read()

    # Generate html nodes and html file
    html_node = markdown_to_html_node(from_content)
    html = ""
    for child in html_node.children:
        html += child.to_html()

    title = extract_title(from_path)

    dest_content = template_content.replace("{{ Title }}", title)
    dest_content = dest_content.replace("{{ Content }}", html)

    with open(dest_path, "w") as dest_file:
        dest_file.write(dest_content)


if __name__ == "__main__":
    main()
