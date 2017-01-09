# Image Resizer

##Description

The script allows you to resize and scale images. It is possible to provide only height or width of wished size – the
script will generate new image saving the sides ratio. The full list of supported image files is availiable at
[Pillow documentation](https://pillow.readthedocs.io/en/4.0.x/handbook/image-file-formats.html).

**IMPORTANT:** Note that you need to manually specify the input and output file extension.
##Installation

The script is written with Python3.

Install the packages from requirements.txt using pip:

```
pip install -r requirements.txt
```

**IMPORTANT**: best practice is to use virtualenv. See here: [Link](http://docs.python-guide.org/en/latest/dev/virtualenvs/)
##Example

```python
python3 image_resize.py pic.JPG -sc 0.5 -o pic.png
```

**Output:**

```
Resizing the file at ./pic.JPG
Saved at ./pic.png
```

For complete reference run the script with `-h` (`--help`) argument.

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
