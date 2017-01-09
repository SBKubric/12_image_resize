import argparse
from math import gcd
from PIL import Image


def is_scale_positive(scale):
    return True if scale and float(scale) > 0 else False


def is_dim_positive(dim):
    return True if dim and round(float(dim)) > 0 else False


def parse_args():
    parser = argparse.ArgumentParser(description='This script resizes given image.')
    parser.add_argument('-wh', '--width', help='The desired width of the image')
    parser.add_argument('-ht', '--height', help='The desired height of the image')
    parser.add_argument('-sc', '--scale', help='The desired scale for the image')
    parser.add_argument('file_path', help='The path to the desired image. Note that extension is important!')
    parser.add_argument('-ot', '--output', default=None, help='The optional argument for saving the result file '
                                                              'to save_path. The default is file_path. '
                                                              'Note that extension is important!')
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


def get_future_size(given_image, args):
    current_x, current_y = given_image.size
    ratio_x, ratio_y = get_image_ratio(given_image)
    scale = float(args.scale) if args.scale else None
    future_width = round(float(args.width)) if args.width else None
    future_height = round(float(args.height)) if args.height else None
    if scale:
        return round(current_x*scale), round(current_y*scale)
    if future_width and future_height:
        return future_width, future_height
    if future_width:
        return future_width, round(future_width*ratio_y/ratio_x)
    if args.height:
        return round(future_height*ratio_x/ratio_y), future_height


def resize_image(path_to_original, path_to_result, args):
    given_image = Image.open(path_to_original)  # type: Image.Image
    future_size = get_future_size(given_image, args)
    resized = given_image.resize(future_size)
    resized.save(path_to_result)


if __name__ == '__main__':
    args = parse_args()
    print('Resizing the file at ./{}'.format(args.file_path))
    resize_image(args.file_path, args.output, args)
    print('Saved at ./{}'.format(args.output))


