import argparse
from math import gcd
from PIL import Image


def is_scale_positive(scale):
    return True if scale and float(scale) > 0 else False


def is_dim_positive(dim):
    return True if dim and round(float(dim)) > 0 else False


def parse_args():
    parser = argparse.ArgumentParser(description='The script allows you to resize and scale images. It is possible to '
                                                 'provide only height or width of wished size – the script will '
                                                 'generate new image saving the sides ratio. '
                                                 'The full list of supported image files is availiable at '
                                                 'Pillow documentation: '
                                                 'https://pillow.readthedocs.io/en/4.0.x/handbook/image-file-formats.html '
                                                 '\nIMPORTANT: Note that you need to manually specify '
                                                 'the input and output file extension.')
    parser.add_argument('-wi', '--width', help='The desired width of the image')
    parser.add_argument('-he', '--height', help='The desired height of the image')
    parser.add_argument('-sc', '--scale', help='The desired scale for the image')
    parser.add_argument('file_path', help='The path to the desired image. Note that extension is necessary!')
    parser.add_argument('-o', '--output', default=None, help='The optional argument for saving the result file '
                                                             'to save_path. The default is file_path. '
                                                             'Note that extension is necessary!')
    args = parser.parse_args()
    args.output = args.output if args.output else args.file_path
    if not args.scale and not args.width and not args.height:
        parser.error("No changes were applied.")
    if args.scale and (args.width or args.height):
        parser.error("You can't set the scale and image sizes at the same time!")
    if is_scale_positive(args.scale) or is_dim_positive(args.height) or is_dim_positive(args.width):
        return args
    else:
        parser.error('Bad value! Arguments can be positive ONLY.')


def get_image_ratio(image):
    x, y = image.size
    return int(x / gcd(x, y)), int(y / gcd(x, y))


def resize_image(given_image, *, scale, future_x, future_y):
    current_x, current_y = given_image.size
    ratio_x, ratio_y = get_image_ratio(given_image)
    scale = float(scale) if scale else None
    future_x = round(float(future_x)) if future_x else None
    future_y = round(float(future_y)) if future_y else None
    if scale:
        future_x = round(current_x * scale)
        future_y = round(current_y * scale)
    if future_x:
        future_y = round(future_x * ratio_y / ratio_x)
    if future_y:
        future_x = round(future_y * ratio_x / ratio_y), future_y
    return given_image.resize(future_x, future_y)


if __name__ == '__main__':
    args = parse_args()
    given_image = Image.open(args.file_path)  # type: Image.Image
    print('Resizing the file at ./{}'.format(args.file_path))
    resized = resize_image(args.file_path, scale=args.scale, future_x=args.width, future_y=args.height)
    print('Saved at ./{}'.format(args.output))
    resized.save(args.output)



