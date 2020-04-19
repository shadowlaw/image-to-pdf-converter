import converter
from sys import exit
from os.path import isfile, join, splitext
from os import listdir


def get_user_input():
    conversion_type = input("Are you converting a single image or multiple? (1. Single/2. Multiple): ")
    path = ""

    if conversion_type == '1':
        path = input("Enter image path from root: ")
    elif conversion_type == '2':
        path = input("Enter path of folder that contains the images for conversion: ")
    else:
        print("Invalid option selected.")
        exit(121)

    pdf_path = input("Enter full path and name of new pdf: ")

    pdf_path = pdf_path if splitext(pdf_path)[1].lower() == '.pdf' else pdf_path+".pdf"

    return {"conversion_type": conversion_type, "path": path, "pdf_path": pdf_path}


def get_image_paths(images_path):
    image_file_paths = []
    files = listdir(images_path)
    files.sort()

    for file in files:
        if isfile(join(images_path, file)) and converter.is_supported(join(images_path, file)):
            image_file_paths.append(join(images_path, file))
        else:
            # logger.warn("file not supported {}".format(file))
            pass
    return image_file_paths


def run():
    user_input = get_user_input()

    if user_input["conversion_type"] == '1':
        converter.convert_image_to_pdf(user_input["path"], user_input["pdf_path"])
    else:
        image_paths = get_image_paths(user_input["path"])
        if len(image_paths) == 0:
            exit(0)

        converter.convert_images_to_pdf(image_paths, user_input["pdf_path"])


if __name__ == '__main__':
    run()
