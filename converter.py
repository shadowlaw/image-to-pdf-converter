from PIL import Image
import os


def basic_file_path_validation(file_path):
    if not os.path.exists(file_path):
        raise os.FileNotFoundError

    if not os.path.isfile(file_path):
        raise TypeError

    return True


def convert_image_to_pdf(image_path, pdf_path):

    if not type(image_path) == str:
        raise TypeError('Image path is not a string')

    try:
        basic_file_path_validation(image_path)
    except os.FileNotFoundError as exception:
        # TODO: indicate failure
        return
    except TypeError as exception:
        # TODO: indicate failure
        return

    image = Image.open(image_path)

    if image.mode == 'RGBA':
        image.convert('RGB')

    try:
        image.save(pdf_path, "PDF", resolution=100.0)
        return True
    except Exception as exception:
        # log failure message
        return False


def convert_images_to_pdf(image_path_lst):
    pass

