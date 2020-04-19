from PIL import Image
from Errors.ConversionFailureError import ConversionFailureError
from Errors.ImageNotSupportedError import ImageNotSupportedError
import os

SUPPORTED_IMAGES = [".jpg", ".jpeg", ".png"]


def basic_file_path_validation(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError

    if not os.path.isfile(file_path):
        raise TypeError

    return True


def convert_image_to_pdf(image_path, pdf_path):

    if not type(image_path) == str:
        raise TypeError('Image path is not a string')

    try:
        basic_file_path_validation(image_path)
    except FileNotFoundError as exception:
        raise ConversionFailureError("File not found at path: {}".format(image_path))
    except TypeError as exception:
        raise ConversionFailureError("Not a file: {}".format(image_path))

    image = get_image_from_path(image_path)

    try:
        image.save(pdf_path, "PDF", resolution=100.0)
        return True
    except Exception as exception:
        # TODO: log failure message
        return False


def get_image_from_path(image_path):

    if not is_supported(image_path):
        raise ImageNotSupportedError("images extension not supported: {}".format(image_path))

    image = Image.open(image_path)
    if image.mode == 'RGBA':
        image = image.convert('RGB')
    return image


def is_supported(image_path):
    return os.path.splitext(image_path)[1] in SUPPORTED_IMAGES


def convert_images_to_pdf(image_path_lst, pdf_path):

    if type(image_path_lst) != list:
        raise TypeError("{} is not a list".format(type(image_path_lst)))

    images = []
    for image_path in image_path_lst:
        try:
            basic_file_path_validation(image_path)
        except FileNotFoundError as exception:
            # logger.warn("File not found at path: {}".format(image_path))
            continue
        except TypeError as exception:
            # logger.warn("Not a file: {}".format(image_path))
            continue

        try:
            image = get_image_from_path(image_path)
        except ImageNotSupportedError as err:
            # logger.warn(err)
            continue

        images.append(image)
    images[0].save(pdf_path, save_all=True, quality=100, append_images=images[1:])
