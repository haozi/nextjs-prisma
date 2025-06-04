# from browser_use import Agent, Browser


from time import sleep

from browser_manager import close_browser, create_new_context, get_page_html

no_script_context = create_new_context(java_script_enabled=True)

urls = [
    # "https://www.baidu.com",
    {"url": "https://www.baidu.com", "context": no_script_context}
]

for item in urls:
    url, context = item["url"], item["context"]
    html = get_page_html(url, context=context)
    print(f"✅ 获取 {url} 成功", html)

close_browser()
