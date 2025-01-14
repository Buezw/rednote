from playwright.sync_api import sync_playwright
import time
import re
import os

# 文件路径，用于保存会话状态

def publish(img_path,title,body):
    session_file = r"session.json"
    with sync_playwright() as p:
        # 使用保存的会话状态文件创建新的上下文
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(storage_state=session_file)
        file_input_xpath = "xpath=/html/body/div[1]/div/div[2]/div/div[2]/main/div[3]/div/div/div[1]/div/div/div/div[1]/div[2]"
        # 打开页面，加载登录后的状态
        page = context.new_page()
        page.goto("https://creator.xiaohongshu.com/publish/publish?source=official")  # 替换为实际的目标页面 URL
        page.wait_for_selector(file_input_xpath, timeout=60000)
        page.locator(file_input_xpath).click()
        upload_address = 'xpath=/html/body/div[1]/div/div[2]/div/div[2]/main/div[3]/div/div/div[1]/div/div/div/div[2]/div[1]/div/input'
        page.locator(upload_address).set_input_files(img_path)
        page.locator('xpath=/html/body/div[1]/div/div[2]/div/div[2]/main/div[3]/div/div/div[1]/div/div/div/div/div[1]/div[1]/div[4]/div[1]/div/input').fill(title)
        #/html/body/div[1]/div/div[2]/div/div[2]/main/div[3]/div/div/div[1]/div/div/div/div/div[1]/div[1]/div[5]/div/div/div[1]/div
        tag_input = 'xpath=/html/body/div[1]/div/div[2]/div/div[2]/main/div[3]/div/div/div[1]/div/div/div/div/div[1]/div[1]/div[5]/div/div/div[1]/div'
        tag_clicker = 'xpath=/html/body/div[1]/div/div[2]/div/div[2]/main/div[3]/div/div/div[1]/div/div/div/div/div[1]/div[1]/div[1]/div[5]/div[4]/div/div[1]/ul/li[1]'
        page.locator(tag_input).fill(body)
        time.sleep(5)
        page.locator('xpath=/html/body/div[1]/div/div[2]/div/div[2]/main/div[3]/div/div/div[1]/div/div/div/div/div[2]/div/button[1]').click()
        #/html/body/div[1]/div/div[2]/div/div[2]/main/div[3]/div/div/div[1]/div/div/div/div/div[2]/div/button[1]
        time.sleep(5)
        page.screenshot(path="output.png")
        print("已发布！")

        browser.close()


def save_session():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()

        # 打开页面并登录（此处替换为实际的登录页面 URL）
        page = context.new_page()
        page.goto("https://creator.xiaohongshu.com/publish/publish?source=official")

        input("123")
        # 等待登录完成，确保页面已加载
        page.wait_for_load_state("networkidle")

        # 保存会话状态到文件
        context.storage_state(path=session_file)
        
        browser.close()

# 调用函数：首次运行时保存会话，以后可以直接加载
#save_session()  # 手动登录并保存会话
#rednote_publish()  # 使用保存的会话直接加载
