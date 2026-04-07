import asyncio
from playwright.async_api import async_playwright
import os

async def verify():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()

        # Check index link
        path = os.path.abspath('index.html')
        await page.goto(f'file://{path}')
        await page.click('text="The Concrete Pavilion"')
        print(f"Clicked Concrete Pavilion, current url: {page.url}")

        # Check projects link
        path = os.path.abspath('projects.html')
        await page.goto(f'file://{path}')
        await page.click('text="The Obsidian Tower"')
        print(f"Clicked Obsidian Tower, current url: {page.url}")

        # Check obsidian pavilion dark mode
        await page.click('.theme-toggle')
        is_dark = await page.evaluate("() => document.documentElement.classList.contains('dark')")
        print(f"Obsidian Pavilion is dark: {is_dark}")
        await page.screenshot(path='obsidian_dark.png')

        await browser.close()

if __name__ == "__main__":
    asyncio.run(verify())
