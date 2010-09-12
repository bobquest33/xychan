
import os
from subprocess import check_call

from .util import random_key, num_encode

IMAGE_DIR = "_images"
THUMBS_DIR = IMAGE_DIR + os.sep + "thumbs"

def _im_identify_type(fn):
    out = check_call("identify", "-format", "%m", fn)
    return out.strip().lower()


def _im_make_thumb(fn):
    check_call("convert", fn, "-resize", "150x150", "-quality", "60",
               THUMBS_DIR + fn[fn.rindex(os.sep):fn.rindex('.')] + '.jpeg')


def store_image(image_data):
    key = num_encode(random_key())
    fn = IMAGE_DIR + os.sep + key
    open(fn, 'w').write(image_data)
    typ = _im_identify_type(fn)
    real_fn = fn + '.' + typ
    check_call("mv", fn, real_fn)
    _im_make_thumb(real_fn)
    return key + '.' + typ


def fetch_image(fn):
    return open(IMAGE_DIR + os.sep + fn).read()


def fetch_thumb(fn):
    return open(THUMBS_DIR + os.sep + fn).read()
