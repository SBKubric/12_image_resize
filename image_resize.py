import argparse
from PIL import Image
import pdb


def parse_args():
    parser = argparse.ArgumentParser(description='This script resizes given image.')
    parser.add_argument('-wh', '--width', help='The desired width of the image')
    parser.add_argument('-ht', '--height', help='The desired height of the image')
    parser.add_argument('-sc', '--scale', help='The desired scale for the image')
    parser.add_argument('file_path', help='The path to the desired image')
    parser.add_argument('-ot', '--output', default=None, help='The optional argument for saving the result file '
                                                              'to save_path. The default is file_path.')
    return parser.parse_args()


def resize_image(path_to_original, path_to_result):
    given_image = Image.open(path_to_original) # type: Image.Image


if __name__ == '__main__':
    args = parse_args()
    args.output = args.output if args.output else args.file_path
    print('Resizing the file at {}'.format(args.file_path))
    resize_image(args.file_path, args.output)
    print('Saved at {}'.format(args.output))


