import asyncio
from page_scraper import scrape_job_description, gather_descriptions
from jd_extraction import analyze_job_description
from collections import Counter

# List of URLs to scrape
urls = [
    'https://www.linkedin.com/jobs/view/3744434861',
    'https://www.linkedin.com/jobs/view/3681740232',
    'https://www.linkedin.com/jobs/view/3729439901',
    'https://www.linkedin.com/jobs/view/3661305839',
    'https://www.linkedin.com/jobs/view/3754694999',
    'https://www.linkedin.com/jobs/view/3743328654',
    'https://www.linkedin.com/jobs/view/3737476691',
    'https://www.linkedin.com/jobs/view/3745689585',
    'https://www.linkedin.com/jobs/view/3743164336',
    'https://www.linkedin.com/jobs/view/3754701139',
    'https://www.linkedin.com/jobs/view/3738863806',
    'https://www.linkedin.com/jobs/view/3749204342'
]

# Use asyncio.run to execute the async function
job_descriptions = asyncio.run(gather_descriptions(urls))

appended_tools_list = []

# Analyze each job description
for description in job_descriptions:
    tools_and_languages = analyze_job_description(description)
    for tool in tools_and_languages.split(','):
        tool = tool.strip().lower()
        appended_tools_list.append(tool)

# count the number of times each tool or language appears
tool_counts = Counter(appended_tools_list)

# print the results in sorted order
for tool, count in sorted(tool_counts.items(), key=lambda item: item[1], reverse=True):
    print(f'{tool}: {count}')
