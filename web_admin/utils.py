#  Copyright (C) AI Power - All Rights Reserved
#  Unauthorized copying of this file, via any medium is strictly prohibited
#  Proprietary and confidential
#  Written by AI Power, January 2020

import os

from django.utils.html import format_html

from config.settings import STATIC_ROOT
from utils.static_util import StaticUtil

from config.settings import log


def get_captured_image_thumbnail(self, obj):
    # noinspection PyBroadException
    try:
        ocr_image_filename = obj.captured_images.get('ocr_image', None)
        back_image_filename_1 = obj.captured_images.get('back_image_1', None)
        back_image_filename_2 = obj.captured_images.get('back_image_2', None)
        left_image_filename = obj.captured_images.get('left_image', None)
        right_image_filename = obj.captured_images.get('right_image', None)
        front_image_filename_1 = obj.captured_images.get('front_image_1', None)
        front_image_filename_2 = obj.captured_images.get('front_image_2', None)
        back_image_filename = obj.captured_images.get('back_image', None)

        ocr_image_filepath = os.path.join(
            STATIC_ROOT,
            'captured_images',
            f'{obj.history_id}',
            f'{ocr_image_filename}',
        )
        left_image_filepath = os.path.join(
            STATIC_ROOT,
            'captured_images',
            f'{obj.history_id}',
            f'{left_image_filename}',
        ) if left_image_filename is not None else None
        right_image_filepath = os.path.join(
            STATIC_ROOT,
            'captured_images',
            f'{obj.history_id}',
            f'{right_image_filename}',
        ) if right_image_filename is not None else None
        front_image_filepath_1 = os.path.join(
            STATIC_ROOT,
            'captured_images',
            f'{obj.history_id}',
            f'{front_image_filename_1}',
        ) if front_image_filename_1 is not None else None
        front_image_filepath_2 = os.path.join(
            STATIC_ROOT,
            'captured_images',
            f'{obj.history_id}',
            f'{front_image_filename_2}',
        ) if front_image_filename_1 is not None else None
        back_image_filepath = os.path.join(
            STATIC_ROOT,
            'captured_images',
            f'{obj.history_id}',
            f'{back_image_filename}',
        ) if back_image_filename is not None else None
        back_image_filepath_1 = os.path.join(
            STATIC_ROOT,
            'captured_images',
            f'{obj.history_id}',
            f'{back_image_filename_1}',
        ) if back_image_filename_1 is not None else None
        back_image_filepath_2 = os.path.join(
            STATIC_ROOT,
            'captured_images',
            f'{obj.history_id}',
            f'{back_image_filename_2}',
        ) if back_image_filename_2 is not None else None

        log.debug(f'ocr_image_file_path {ocr_image_filepath}')
        log.debug(f'left_image_file_path {left_image_filepath}')
        log.debug(f'right_image_file_path {right_image_filepath}')
        log.debug(f'back_image_file_path {back_image_filepath}')

        ocr_image_url = StaticUtil.filepath2url(ocr_image_filepath)
        left_image_url = StaticUtil.filepath2url(left_image_filepath) if left_image_filepath is not None else '#'
        right_image_url = StaticUtil.filepath2url(right_image_filepath) if right_image_filepath is not None else '#'
        front_image_url_1 = StaticUtil.filepath2url(front_image_filepath_1) if front_image_filepath_1 is not None else '#'
        front_image_url_2 = StaticUtil.filepath2url(front_image_filepath_2) if front_image_filepath_2 is not None else '#'
        back_image_url = StaticUtil.filepath2url(back_image_filepath) if back_image_filepath is not None else '#'
        back_image_url_1 = StaticUtil.filepath2url(back_image_filepath_1) if back_image_filepath_1 is not None else '#'
        back_image_url_2 = StaticUtil.filepath2url(back_image_filepath_2) if back_image_filepath_2 is not None else '#'

        log.debug(f'url_ocr_image_filepath {ocr_image_url}')
        log.debug(f'url_left_image_filepath {left_image_url}')
        log.debug(f'url_right_image_filepath {right_image_url}')
        log.debug(f'url_right_image_filepath {back_image_url}')

    except Exception:
        ocr_image_url = '#'
        left_image_url = '#'
        right_image_url = '#'
        front_image_url_1 = '#'
        front_image_url_2 = '#'
        back_image_url = '#'
        back_image_url_1 = '#'
        back_image_url_2 = '#'
    return format_html(
        f'<img title="Show OCR images" attr="Show OCR Image" src="/static/captured_images/ocr.jpg" style="max-width:45px; max-height:45px; margin-right:10px;cursor:pointer" onclick="showListImage({obj.history_id},`ocr`)">'
        f'<img title="Show back_ images" attr="Show back_ Image" src="/static/captured_images/ocr.jpg" style="max-width:45px; max-height:45px; margin-right:10px;cursor:pointer" onclick="showListImage({obj.history_id},`back_`)">'
        f'<img title="Show back2 images" attr="Show back2 Image" src="/static/captured_images/ocr.jpg" style="max-width:45px; max-height:45px; margin-right:10px;cursor:pointer" onclick="showListImage({obj.history_id},`back2`)">'
        f'<img title="Show front1 images" attr="Show front1 Image" src="/static/captured_images/ocr.jpg" style="max-width:45px; max-height:45px; margin-right:10px;cursor:pointer" onclick="showListImage({obj.history_id},`front1`)">'
        f'<img title="Show front2 images" attr="Show front2 Image" src="/static/captured_images/ocr.jpg" style="max-width:45px; max-height:45px; margin-right:10px;cursor:pointer" onclick="showListImage({obj.history_id},`front2`)">'
        f'<img title="Show left images" attr="Show left Image" src="/static/captured_images/ocr.jpg" style="max-width:45px; max-height:45px; margin-right:10px;cursor:pointer" onclick="showListImage({obj.history_id},`left`)">'
        f'<img title="Show right images" attr="Show right Image" src="/static/captured_images/ocr.jpg" style="max-width:45px; max-height:45px; margin-right:10px;cursor:pointer" onclick="showListImage({obj.history_id},`right`)">'
        f'<img title="Show top images" attr="Show top Image" src="/static/captured_images/ocr.jpg" style="max-width:45px; max-height:45px; margin-right:10px;cursor:pointer" onclick="showListImage({obj.history_id},`top`)">'

    )
    # return format_html(
    #     f'<a href="{ocr_image_url}" target="{"_blank" if ocr_image_url != "#" else ""}">'
    #     f'<img src="{ocr_image_url}" style="max-width:120px; max-height:120px;">'
    #     f'</a>'
    #     f'<a href="{left_image_url}" target="{"_blank" if left_image_url != "#" else ""}">'
    #     f'<img src="{left_image_url}" style="max-width:120px; max-height:120px;">'
    #     f'</a>'
    #     f'<a href="{right_image_url}" target="{"_blank" if right_image_url != "#" else ""}">'
    #     f'<img src="{right_image_url}" style="max-width:120px; max-height:120px;">'
    #     f'</a>'
    #     f'<a href="{front_image_url_1}" target="{"_blank" if front_image_url_1 != "#" else ""}">'
    #     f'<img src="{front_image_url_1}" style="max-width:120px; max-height:120px;">'
    #     f'</a>'
    #     f'<a href="{front_image_url_2}" target="{"_blank" if front_image_url_2 != "#" else ""}">'
    #     f'<img src="{front_image_url_2}" style="max-width:120px; max-height:120px;">'
    #     f'</a>'
    #     f'<a href="{back_image_url}" target="{"_blank" if back_image_url != "#" else ""}">'
    #     f'<img src="{back_image_url}" style="max-width:120px; max-height:120px;">'
    #     f'</a>'
    #     f'<a href="{back_image_url_1}" target="{"_blank" if back_image_url_1 != "#" else ""}">'
    #     f'<img src="{back_image_url_1}" style="max-width:120px; max-height:120px;">'
    #     f'</a>'
    #     f'<a href="{back_image_url_2}" target="{"_blank" if back_image_url_2 != "#" else ""}">'
    #     f'<img src="{back_image_url_2}" style="max-width:120px; max-height:120px;">'
    #     f'</a>'
    # )
