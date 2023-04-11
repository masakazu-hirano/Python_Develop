import urllib.request

from PIL import Image

if __name__ == '__main__':
    image_url = urllib.request.urlopen(url='URL')
    image = Image.open(image_url, mode='r', formats=[''])
        # 画像ファイルのサポート形式: `$ python3 -m PIL`

    with open('ファイルパス（保存先）', mode='xb') as image_file:
        image.save(image_file, format='PNG', compress_level=0)
