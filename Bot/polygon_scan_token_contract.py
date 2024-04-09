# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from bs4 import BeautifulSoup
# import time

# # Khởi tạo trình duyệt Chrome
# driver = webdriver.Chrome()

# # Mở trang web PolygonScan
# driver.get("https://polygonscan.com/")

# # Đọc danh sách coin từ file 'test.txt'
# with open('test.txt', 'r') as file:
#     coins = file.readlines()
#     coins = [coin.strip() for coin in coins]

# # Thực hiện tìm kiếm và in kết quả cho từng coin trong danh sách
# for coin in coins:
#     try:
#         # Tìm ô tìm kiếm và nhập dữ liệu từ file 'test.txt'
#         search_input = driver.find_element("id","search-panel")
#         search_input.clear()  # Xóa bất kỳ dữ liệu nào có thể đã tồn tại trước đó
#         search_input.send_keys(coin)
#         search_input.send_keys(Keys.RETURN)  # Nhấn phím Enter

#         # Tạm dừng để đợi kết quả tải xuống
#         time.sleep(3)

#         # Lấy nội dung HTML của trang hiện tại
#         html = driver.page_source

#         # Sử dụng BeautifulSoup để phân tích HTML
#         soup = BeautifulSoup(html, 'html.parser')

#         # Tìm tất cả các thẻ <a> có class là "text-truncate d-block"
#         links = soup.find_all('a', class_='text-truncate d-block')

#         # In ra nội dung của từng thẻ <a>
#         for link in links:
#             print(link.text)

#     except Exception as e:
#         print(f"Lỗi khi tìm kiếm cho {coin}: {e}")

# # Đóng trình duyệt
# driver.quit()

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
import webbrowser

# Đọc danh sách coin từ file 'test.txt'
with open('test.txt', 'r') as file:
    coins = file.readlines()
    coins = [coin.strip().replace('(', '').replace(')', '') for coin in coins]

# Thực hiện tìm kiếm và in kết quả cho từng coin trong danh sách
for coin in coins:
    try:
        # Khởi tạo trình duyệt Chrome
        driver = webdriver.Chrome()

        # Mở trang web PolygonScan
        driver.get("https://polygonscan.com/")

        # Tìm ô tìm kiếm và nhập dữ liệu từ file 'test.txt'
        search_input = driver.find_element("id","search-panel")
        search_input.clear()  # Xóa bất kỳ dữ liệu nào có thể đã tồn tại trước đó
        search_input.send_keys(coin)

        # Tạm dừng để đợi kết quả tải xuống
        time.sleep(1)

        search_input.send_keys(Keys.RETURN)  # Nhấn phím Enter

        # Tạm dừng để đợi kết quả tải xuống
        time.sleep(1)

        # Lấy nội dung HTML của trang hiện tại
        html = driver.page_source

        # Sử dụng BeautifulSoup để phân tích HTML
        soup = BeautifulSoup(html, 'html.parser')

        # Tìm tất cả các thẻ <a> có class là "text-truncate d-block"
        links = soup.find_all('a', class_='text-truncate d-block')

        # Lặp qua các thẻ <a> và mở trình duyệt mới với đường dẫn được tạo
        for link in links:
            address = link.text
            address_url = 'https://polygonscan.com/address/' + address
            # Mở đường dẫn trong một trình duyệt mới
            webbrowser.open_new_tab(address_url)

    except Exception as e:
        print(f"Lỗi khi tìm kiếm cho {coin}: {e}")

# Đóng trình duyệt
driver.quit()
