import json
import os
import traceback
import webbrowser
from itertools import cycle
from random import choice, uniform
from time import sleep

import requests
from pydash import get as _
from selectolax.parser import HTMLParser

MIN_HOLDERS = 10
MAX_HOLDERS = 300

USER_AGENTS = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'
]

# Hàm này trả về một user agent ngẫu nhiên từ danh sách các user agent được định nghĩa trước.
def random_ua():
    return choice(USER_AGENTS)

# Hàm này đọc dữ liệu từ một tập tin có tên được chỉ định và trả về danh sách các dòng trong tập tin đó.
def file2list(filename):
    result = []
    if os.path.isfile(filename):
        with open(filename, encoding='utf-8') as f:
            return f.read().splitlines()
    return []

# Hàm này tải các proxy từ tập tin proxy.txt và trả về một tập hợp các proxy đã tải.
def load_proxy():
    proxies = set()
    if os.path.exists('./proxy.txt'):
        with open('./proxy.txt', 'r') as f:
            for line in f:
                px = line.strip().split(':')
                proxies.add(f'http://{px[2]}:{px[3]}@{px[0]}:{px[1]}')
    return proxies


proxies = cycle(load_proxy())
coins = set(file2list('coins.txt'))

# Hàm này nhận vào một selector CSS và một đối tượng HTMLParser,
# và trả về văn bản của phần tử được chọn.
# Nếu selector không được cung cấp, nó trả về toàn bộ văn bản của soup.
def get_text(selector: str, soup: HTMLParser):
    try:
        t = (soup.css_first(selector) if selector else soup).text(
            separator=' ', strip=True).replace('\xa0', ' ').replace(
                '\t', ' ').replace('\r', ' ').replace('\n', ' ').strip()
        while '  ' in t:
            t = t.replace('  ', ' ')
        return t
    except:
        return ''

# Hàm này dừng chương trình trong một khoảng thời gian ngẫu nhiên giữa start và end.
def rand_sleep(start, end):
    sleep(uniform(start, end))

# Hàm này chuyển đổi một chuỗi thành một số nguyên, loại bỏ dấu phẩy và khoảng trắng trong quá trình chuyển đổi.
def to_int(s):
    try:
        return int(s.replace(',', '').replace(' ', '').strip())
    except:
        return 0

# Hàm này thực hiện một yêu cầu đồng bộ đến một URL được chỉ định
# Sử dụng một proxy và một user agent ngẫu nhiên nếu có.
# Nó trả về kết quả của yêu cầu.
def sync_fetch(url: str, session=None, headers=None):
    tried = 0
    while tried < 5:
        try:
            proxy = next(proxies, None)
            print(f'Getting {url}')
            return (session or requests).get(
                url,
                headers=headers if headers else {'User-Agent': random_ua()},
                timeout=30,
                proxies={
                    'http': proxy,
                    'https': proxy
                } if proxy else None)

        except KeyboardInterrupt:
            raise KeyboardInterrupt('Abort')
        except:
            traceback.print_exc()
            tried += 1
            sleep(1)

# Hàm này trả về các phần tử con của một phần tử được chọn dựa trên một selector CSS và văn bản của phần tử cha.
def get_next_elements(selector: str, next_selector, text, soup: HTMLParser):
    try:
        elements = []
        for el in soup.css(selector):
            t = el.text().replace('\xa0', ' ').strip()
            if text == t:
                start = False
                for cnode in el.parent.iter():
                    if cnode == el:
                        start = True
                    elif start:
                        elements.append(cnode)
        return elements
    except:
        return None

# Hàm này trích xuất giá trị của một thuộc tính từ một phần tử được chọn và trả về giá trị của thuộc tính đó.
def get_attr(selector: str, attr: str, soup: HTMLParser):
    try:
        return (soup.css_first(selector) if selector else soup).attributes.get(
            attr, '').replace('\xa0', ' ').strip()
    except:
        return ''

# Hàm này thực hiện một yêu cầu đồng bộ đến một URL được chỉ định 
# và trả về một đối tượng HTMLParser của nội dung trả về từ yêu cầu.
def sync_bs(url: str, session=None):
    r = sync_fetch(url, session)
    soup = HTMLParser(r.text if r else '')
    return soup

# Hàm này là hàm chính của chương trình.
# Nó thực hiện logic chính của chương trình để thu thập thông tin về các token từ trang giao dịch token BSC.
def main():
    while True:
        try:
            soup = sync_bs('https://bscscan.com/tokentxns')
            for el in soup.css('#content td a'):
                href = get_attr(None, 'href', el)

                if '/token/' in href and '/images/main/empty-token.png' in get_attr(
                        'img', 'src', el):
                    url = f'https://bscscan.com{href}'
                    poocoin_url = f'http://poocoin.app/tokens/{href.split("/token/")[-1]}'
                    if url not in coins:
                        s = sync_bs(url)
                        t = get_text(None, s)
                        if 'LPs' in t or '-LP' in t or 'BLP' in t:
                            continue
                        els = get_next_elements('div', 'div', 'Holders:', s)
                        if els:
                            for node in els:
                                text = get_text(None, node)
                                if 'addresses' in text:
                                    holders = to_int(
                                        text.split('addresses')[0])

                                    if MIN_HOLDERS < holders < MAX_HOLDERS:
                                        # Kiểm tra coin đã tồn tại trong file txt chưa
                                        with open('tokens.txt', 'r', encoding='utf-8') as file:
                                            existing_coins = file.read()
                                            if url not in existing_coins:
                                                # Ghi tên và URL vào file
                                                with open('tokens.txt', 'a', encoding='utf-8') as file:
                                                    file.write(f"Token name: {t}\n")
                                                    file.write(f"Poocoin URL: {poocoin_url}\n\n")
                                    break
                    if holders > MIN_HOLDERS:
                        coins.add(url)
            rand_sleep(1, 3)
        except KeyboardInterrupt:
            return
        except:
            traceback.print_exc()
            sleep(1)


if __name__ == '__main__':
    try:
        main()
    finally:
        with open('coins.txt', 'w', encoding='utf-8') as f:
            f.write('\n'.join(coins))