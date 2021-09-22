from pyimagesearch.blur_detector import detect_blur_fft
import numpy as np
import cv2
from urllib.request import Request, urlopen


def convert_url_or_path_to_image(url_or_path, type):
    if type == 'url':
        user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 ' \
                       'Safari/537.36 '
        req = Request(url_or_path, headers={'User-Agent': user_agent})
        webpage = urlopen(req).read()
        image = np.asarray(bytearray(webpage), dtype="uint8")
        image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    elif type == 'path':
        image = cv2.imread(url_or_path)
    else:
        image = None

    return image


def get_blur_point(url_or_path, type):
    if type not in ("url", "path"):
        return f"Unknown type '{type}'. Use only 'url' or 'path'"

    orig = convert_url_or_path_to_image(url_or_path, type)

    if orig is not None:
        gray = cv2.cvtColor(orig, cv2.COLOR_BGR2GRAY)

        return detect_blur_fft(gray, size=80)
    else:
        return f"Can not get blur point for image '{url_or_path}' with type '{type}'"
