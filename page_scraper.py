import asyncio
from playwright.async_api import async_playwright


async def scrape_job_description(url):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36"
        context = await browser.new_context(user_agent=user_agent)
        page = await context.new_page()

        print('Heading to page')
        await page.goto(url)

        # Click the "See more" button to reveal the full job description.
        # This assumes the button is uniquely identifiable by its aria-label.
        await page.click('button[aria-label="Show more, visually expands previously read content above"]')

        # Wait for the content to load after clicking
        await page.wait_for_timeout(2000)  # adjust timeout as needed

        job_description_selector = '.description__text.description__text--rich'
        # Extract the job description text
        job_description = await page.inner_text(job_description_selector)

        await browser.close()

        print('Exiting scraper')
        return job_description


# This function will gather job descriptions
async def gather_descriptions(urls):
    tasks = [scrape_job_description(url) for url in urls]
    return await asyncio.gather(*tasks)

