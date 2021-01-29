# !/usr/bin/env python
# -*- coding=utf-8 -*-
#
# !/usr/bin/env python
# -*- coding=utf-8 -*-
#

"""Util functions."""
#
import base64, hashlib, json, os, re, subprocess, sys, \
    time, uuid, xmltodict, cv2, pydicom, qrcode, yaml
import SimpleITK as sitk
import numpy as np

# from xpinyin import Pinyin
from datetime import datetime
from functools import reduce
from PIL import Image
from requests import Session
from skimage import draw
# from dncloud.common.constants import DNCLOUD_HOME, REGEX_KEYS, NO_SPACE_SUB
# from dncloud.metrics import hardware


def read_yml(filename):
    """Read yaml file"""
    content = {}
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            content = yaml.full_load(f)
    return content


__author__ = "rudywang"

# Time format protocol
TIME_ISO8601 = "%Y-%m-%dT%H:%M:%SZ"
TIME_ISO8601_MS = "%Y-%m-%dT%H:%M:%S.%fZ"

session = Session()


def get_file_md5_digest(filename, block=64 * 1024):
    """Calculate md5 hexdigest of content."""
    with open(filename, "rb") as r:
        md5 = hashlib.md5()
        while True:
            data = r.read(block)
            if not data:
                break
            md5.update(data)
        return md5.hexdigest()


def get_content_md5_digest(content):
    """Calculate md5 hexdigest of content."""
    md5 = hashlib.md5()
    try:
        md5.update(to_bytes(content))
    except Exception as e:
        raise e
    return md5.hexdigest()


def get_content_sha1_digest(content):
    """Calculate sha1 hexdigest of content."""
    sha1 = hashlib.sha1()
    sha1.update(to_bytes(content))
    return sha1.hexdigest()


def gen_uuid():
    """Generate uuid."""
    return uuid.uuid1().hex


def get_unixtime():
    """Get unixtime.

    :arg int unixtime: UNIX time
    :return unixtime
    """
    return int(time.time())


def get_utctime():
    """Get formatted time (UTC time).

    Note: Time Zone was 0
    :return UTC time
    """
    return time.strftime(TIME_ISO8601, time.gmtime())


def get_gmttime():
    """Get formatted time (GMT time).

    :return GMT time
    """
    return time.strftime("%a, %d %b %Y %H:%M:%S GMT", time.gmtime())


def get_gmttime_from_unixtime(unix_time=None):
    """Get formatted time (GMT time).

    :arg string unix_time: unix time
    :return GMT time
    """
    return time.strftime("%a, %d %b %Y %H:%M:%S GMT", time.localtime(float(unix_time or time.time())))


def get_unixtime_from_gmttime(gmt_time=None):
    """Get unixtime from GMT time.

    :arg string gmt_time: GMT time
    :return unixtime
    """
    formatd = time.gmtime() if gmt_time is None \
        else time.strptime(gmt_time, "%a, %d %b %Y %H:%M:%S GMT")
    return int(time.mktime(formatd))


def get_unixtime_from_strftime(formats, strtime):
    """Get unixtime from format time.

    :arg string formats: format string
    :arg string strtime: format time
    :return unixtime
    """
    return int(time.mktime(time.strptime(strtime, formats)))


def get_format_time(formats, unixtime=None, delay=None):
    """Get format time from unix time.

    :arg string formats: format string
    :arg integer unixtime: time stamp
    :arg integer delay: the seconds delay
    :return format time
    """
    timestamp = unixtime or time.time()
    if delay:
        timestamp += delay
    locatime = datetime.fromtimestamp(timestamp)
    return locatime.strftime(formats)


def to_str(bytes_or_str):
    """Encode bytes or str to str type."""
    return bytes_or_str.decode("utf-8") if isinstance(bytes_or_str, bytes) else bytes_or_str


def to_bytes(bytes_or_str):
    """Encode bytes or str to str type."""
    return bytes_or_str.encode("utf-8") if isinstance(bytes_or_str, str) else bytes_or_str


def base64_urlsafe_encode(digest):
    """Encode url string.

    :arg string digest: url content
    :return string url encoded
    """
    encode = base64.urlsafe_b64encode(to_bytes(digest)).strip()
    return to_str(encode)


def base64_urlsafe_decode(digest):
    """Decode url string.

    :arg string digest: url content
    :return string url decoded
    """
    decode = base64.urlsafe_b64decode(digest).strip()
    return to_str(decode)


def base64_encode(digest):
    """Encode string use base64.

    :arg string digest: encode content
    :return string encoded
    """
    encode = base64.b64encode(to_bytes(digest)).strip()
    return to_str(encode)


def base64_decode(digest):
    """Decode string use base64.

    :arg string digest: decode content
    :return string decoded
    """
    decode = base64.b64decode(digest).strip()
    return to_str(decode)


def base16_encode(digest):
    """Encode string use base64.

    :arg string digest: encode content
    :return string encoded
    """
    encode = base64.b16encode(to_bytes(digest)).strip()
    return to_str(encode)


def base16_decode(digest):
    """Decode string use base64.

    :arg string digest: decode content
    :return string decoded
    """
    decode = base64.b16decode(digest).strip()
    return to_str(decode)


def is_valid_base64_encode(digest):
    """Verify the base64 encode string."""
    pattern = re.compile(r"[A-Z]")
    if pattern.match(digest):
        return True
    return False


def is_contain_zh(string):
    """Verify the word is include ZH."""
    pattern = re.compile(u"[\u4e00-\u9fa5]+")
    if pattern.search(to_str(string)):
        return True
    return False


def safe_pathname(string):
    """Check and process the ZH directory and filename."""
    encode = to_str(string)
    return encode.replace(" ", "")


def gen_qrcode(data, filename, **kwargs):
    """Generate QR code png picture."""
    params = {
        "version": int(kwargs.get("version", 1)),
        "error_correction": qrcode.constants.ERROR_CORRECT_H,
        "box_size": int(kwargs.get("box_size", 10)),
        "border": int(kwargs.get("border", 4))
    }
    qrc = qrcode.QRCode(**params)
    qrc.add_data(data)
    qrc.make(fit=True)
    img = qrc.make_image(fill_color="black", back_color="white")
    img.save(filename)
    return filename


def get_dicom_instance_number(dirname, file_list=None):
    """Gets the maximum file sequence of the uploaded file."""
    file_list = file_list or os.listdir(dirname)
    instance_number = 0
    for file in file_list:
        filename = os.path.join(dirname, file)
        tag = pydicom.read_file(filename)
        instance_number = instance_number if instance_number > int(tag.get("InstanceNumber", 0)) else int(
            tag.get("InstanceNumber"))
    return instance_number


def coord_conversion(shape, size, coord_x, coord_y, coord_z=1):
    """Obtain the corresponding coordinate parameters of the generated nodule detail diagram."""
    half_size = size // 2
    if (coord_z - half_size) < 0:
        start_z = 0
    elif (coord_z + half_size) > shape[0] - 1:
        start_z = shape[0] - size
    else:
        start_z = int(coord_z - half_size)

    if (coord_y - half_size) < 0:
        start_y = 0
    elif (coord_y + half_size) > shape[1] - 1:
        start_y = shape[1] - size
    else:
        start_y = int(coord_y - half_size)

    if (coord_x - half_size) < 0:
        start_x = 0
    elif (coord_x + half_size) > shape[2] - 1:
        start_x = shape[2] - size
    else:
        start_x = int(coord_x - half_size)
    return start_z, start_y, start_x


def normalize(img_array):
    """Standardize the image."""
    img_array = np.clip(img_array, -1000, 400)  # 肺窗开窗范围为　-1000 ~ 400
    return (img_array - np.mean(img_array)) / (np.std(img_array))


def png_set_color(img, x, y, d):
    """Draw the nodule marker box."""
    img_rgb = np.array(Image.fromarray(img).convert("RGB"))
    rr, cc = draw.circle_perimeter(y, x, d // 2 + 4)
    draw.set_color(img_rgb, [rr, cc], [0, 0, 255], alpha=1.0)


def dcm2png(parse_path, cube_size=96, **kwargs):
    """Dicom image of nodules image generation."""
    ds_array = sitk.ReadImage(parse_path)
    img_array = sitk.GetArrayFromImage(ds_array)
    shape = img_array.shape
    img_array = np.reshape(img_array, (shape[1], shape[2]))
    img_array = normalize(img_array)
    high = np.max(img_array)
    low = np.min(img_array)
    lungwin = np.array([low * 1.0, high * 1.0])
    newimg = (img_array - lungwin[0]) / (lungwin[1] - lungwin[0])  # 归一化
    newimg = (newimg * 255).astype('uint8')  # 将像素值扩展到[0,255]
    lesion = kwargs.get("lesion")
    y = int(lesion.get("coordY"))
    x = int(lesion.get("coordX"))
    start_z, start_y, start_x = coord_conversion(shape, cube_size, x, y)
    cube = newimg[start_y:start_y + cube_size, start_x:start_x + cube_size]
    img_rgb = np.array(Image.fromarray(newimg).convert("RGB"))
    # 框选位置的半径（取框选结节ｘ，ｙ轴偏移量的最大值）
    d = max(lesion.get('diameter_x'), lesion.get("diameter_y"))
    rr, cc = draw.circle_perimeter(y, x, int(d) // 2 + 4)
    draw.set_color(img_rgb, [rr, cc], [0, 0, 255], alpha=1.0)
    return img_rgb, cube


def save_img(dirname, img, filename=None):
    """Save the images to local directory.."""
    if not filename:
        filename = os.path.join(dirname, gen_uuid()) + ".png"
    cv2.imwrite(filename, img)
    return filename


def sub_special(info, space=False):
    """Re Filter secial string"""
    # space-True; 过滤空格|space-False; 不过滤空格
    if space:
        return re.sub(u"([^\u4e00-\u9fa5\u0030-\u0039\u0041-\u005a\u0061-\u007a])", "", info)
    sub_info = re.sub(u"([^\u4e00-\u9fa5\u0030-\u0039\u0041-\u005a\u0061-\u007a\u0020])", "", info)
    return sub_info


def xml_to_dict(xml_str):
    """transform xml to dict"""
    if not isinstance(xml_str, str):
        assert AssertionError("Argument type is not str")
    data_ordered_dict = xmltodict.parse(xml_str)
    data_json = json.dumps(data_ordered_dict, indent=4)
    data_dict = json.loads(data_json)
    return data_dict


def dict_to_xml(data_dict):
    """transform dict to xml"""
    if not isinstance(data_dict, dict):
        assert AssertionError("Argument type is not dict")
    return xmltodict.unparse(data_dict, pretty=True, encoding='utf-8')


def reduce_list_attr(name, list_data):
    """列表对象根据属性 name 去重"""
    lam_analy = lambda y, x: y if (x[name] in [i[name] for i in y]) \
        else (lambda z, u: (z.append(u), z))(y, x)[1]
    return reduce(lam_analy, list_data, [])
