from playwright.sync_api import sync_playwright
import os
from google_trends.replace import replace
from rednote_publisher import publish



def take_screenshot_of_html(html_path, output_image):
    with sync_playwright() as p:
        # 启动浏览器
        browser = p.chromium.launch(headless=True)  # 设置headless=False可以看到浏览器界面
        page = browser.new_page()


        # 构造本地HTML文件的路径

        local_url = f"file://{html_path}"

        # 打开本地HTML文件
        page.goto(local_url)
        body = page.locator('xpath=/html/body/div')
        # 截图
        body.screenshot(path=output_image)

        # 关闭浏览器
        browser.close()

date, body = replace()
output_image = 'E:\\OneDrive\\Gits\\rednote\\google_trends\\screenshot.png'
html_path = "E:\\OneDrive\\Gits\\rednote\\google_trends\\filled_index.html"
output_path = os.path.abspath('screenshot.png')
# 执行截图功能 
take_screenshot_of_html(html_path, output_image)
publish(output_image,date,body)