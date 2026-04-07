import asyncio
from playwright.async_api import async_playwright
import os

async def verify():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()

        # Load index.html
        path = os.path.abspath('index.html')
        await page.goto(f'file://{path}')

        # Check title/brand
        brand = await page.text_content('.text-lg.font-bold')
        print(f"Brand found: {brand.strip()}")

        # Take light mode screenshot
        await page.screenshot(path='index_light.png')
        print("Captured index_light.png")

        # Toggle theme
        await page.click('.theme-toggle')
        # Wait for class change
        is_dark = await page.evaluate("() => document.documentElement.classList.contains('dark')")
        print(f"Is dark after toggle: {is_dark}")

        # Take dark mode screenshot
        await page.screenshot(path='index_dark.png')
        print("Captured index_dark.png")

        # Reload to check persistence
        await page.reload()
        is_dark_after_reload = await page.evaluate("() => document.documentElement.classList.contains('dark')")
        print(f"Is dark after reload: {is_dark_after_reload}")

        # Check mobile layout
        await page.set_viewport_size({"width": 375, "height": 812})
        await page.screenshot(path='index_mobile.png')
        print("Captured index_mobile.png")

        await browser.close()

if __name__ == "__main__":
    asyncio.run(verify())
