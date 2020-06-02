import shutil
import os
import time
import requests
from pyquery import PyQuery as pq
from rich.console import Console

console = Console()


def page_number_to_url(page):
    """
    将页码添加到 url 中
    :param page: 要转换的页面
    :return: 生成的 url
    """
    return "https://beautyptt.cc/extend/?search=search&title=正妹&author=&infinite_json&page=" + str(page)


def url_to_html(url):
    """
    将 url 转换为 HTML对象
    :param url: 需要转换的 url
    :return: 返回 HTML 文本
    """
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    return response.text


def html_to_json(html):
    """
    根据 HTML 对象提取图片和名称
    :param html: HTML 对象
    :return: 一个跑含图片名称和 url 词典的列表
    """
    d = pq(html)
    grid_item_a_img = d("a>img.img-responsive")
    # console.log(grid_item_a_img)
    grid_item_a_img_length = grid_item_a_img.length
    console.log(f'length: {grid_item_a_img_length}')
    name_and_url_list = []
    # console.log(html)
    for i in range(0, grid_item_a_img_length):
        tmp_img_info = pq(grid_item_a_img[i])

        attribs = tmp_img_info.attr

        alt = attribs.alt
        src = attribs.src

        console.log(src)

        photo_name = alt + src.split('/')[-1]

        if photo_name != 'undefinedPinExt.png':
            if src.index('//') == 0:
                src = 'http:' + src

            name_and_url_list.append({
                'name': photo_name,
                'url': src
            })
    console.log(name_and_url_list)
    return name_and_url_list


def download_image(img_name, img_url):
    """
    给定 url，下载图片
    :param img_url: 图片 url
    :param img_name: 图片名称
    :return: void
    """
    console.log(f'image_url: {img_url} name: {img_name}')
    filename = './images/' + img_name
    if os.path.exists(filename):
        console.log(f'{img_name} 已经存在，跳过该图片')
        return 1
    r = requests.get(img_url, stream=True)
    r.raw.decode_content = True
    with open(filename, 'wb') as f:
        shutil.copyfileobj(r.raw, f)
    console.log(f'{img_name} 下载成功')
    return 0


def main():
    """
    主函数
    :return: 状态码，0代表成功
    """
    # 检查文件夹是否存在，如果不存在就创建一个
    if not os.path.exists('./images'):
        os.mkdir('./images')

    # 注意，请起始页码
    current_page_number = 1
    # 觉定下次是否继续下载
    next_download = True
    # 计算图片的数量
    total_downloads = 0
    # 等待的时间，默认为 10 秒
    wait_time = 10

    while next_download:
        # 生成暂时的的 url
        tmp_url = page_number_to_url(current_page_number)
        console.log(f'请求的 url: {tmp_url}')
        tmp_html = url_to_html(tmp_url)

        if len(tmp_html) < 1:
            next_download = False
            console.log("== 下载停止 ==")
        else:
            # 得到目标下载图片的数组
            img_json = html_to_json(tmp_html)
            for img in img_json:
                if download_image(img['name'], img['url']) == 0:
                    total_downloads = total_downloads + 1
                    # 休息一定时间，减轻服务器负荷
                    console.log(f'等待 {wait_time} 秒')
                    time.sleep(wait_time)

        current_page_number = current_page_number + 1

    console.log(f'== 抓取完成，共抓取了 {total_downloads} 张图片 ==')
    return 0


# 运行 main 函数
main()
