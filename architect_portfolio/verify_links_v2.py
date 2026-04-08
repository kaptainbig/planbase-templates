import asyncio
from playwright.async_api import async_playwright
import os

async def verify():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()

        # Check index links - multiple project cards
        path = os.path.abspath('index.html')
        await page.goto(f'file://{path}')

        # Find all project links on index
        project_links = await page.eval_on_selector_all('a[href="obsidian_pavilion.html"]', "elements => elements.map(e => e.innerText.trim())")
        print(f"Project links found on index: {project_links}")

        # Check projects.html links
        path = os.path.abspath('projects.html')
        await page.goto(f'file://{path}')
        project_links_p = await page.eval_on_selector_all('a[href="obsidian_pavilion.html"]', "elements => elements.map(e => e.innerText.trim())")
        print(f"Project links found on projects.html: {project_links_p}")

        # Click one to confirm
        await page.click('text="The Obsidian Tower"')
        print(f"Clicked Obsidian Tower, current url: {page.url}")

        await browser.close()

if __name__ == "__main__":
    asyncio.run(verify())
