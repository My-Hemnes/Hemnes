# !/usr/bin/env python
# -*- coding=utf-8 -*-
#

"""Util functions."""
#
import os, cv2, pydicom, qrcode
import SimpleITK as sitk
import numpy as np
from PIL import Image
from skimage import draw
from apps.utils.common_utils import gen_uuid


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
