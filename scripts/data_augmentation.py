# _*_ coding: utf-8 _*_
"""
@Auther: Zongzc
@Describe: 
"""
import cv2
from PIL import Image
import os

IMG_END = ['.jpg', '.JPG', '.PNG', '.png', '.jpeg', '.JPEG']


def flip_horizontally(img_path, save_img_path):
    """
    批量水平翻转
    :param img_path: xxx/
    :param save_img_path: yyy/
    :return:
    """
    for filename in os.listdir(img_path):
        # 判断是否为图片
        if os.path.splitext(filename)[1] in IMG_END:
            img = cv2.imread(img_path)
            txt_path = os.path.join(img_path, os.path.splitext(filename)[0] + ".txt")
            # 判断对应的txt路径是否存在
            if os.path.exists(txt_path):
                with open(txt_path, 'r') as f:
                    for line in f:
                        line = line.strip('\n').rstrip()
                        l = line.split(' ')
                        with open(os.path.join(save_img_path, os.path.splitext(filename)[0] + "_horizontally.txt"),
                                  "a") as new_f:
                            f.write(f"{l[0]} {1 - float(l[1])} {l[2]} {l[3]} {l[4]}")
                    cv2.imwrite(os.path.join(save_img_path,
                                             os.path.splitext(filename)[0] + "_horizontally" +
                                             os.path.splitext(filename)[1]),
                                             img[:, ::-1, ])
