import httpx, aiofiles, asyncio
import requests, time, re, os

headers = {
    'cookie': "",
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0'
}

reg = re.compile('/staticdata/down/.*?.zip')
img_reg = re.compile('src="(/staticdata/.*?)"')

async def download_problem(contest_id, problem_id):
    problem_rul = f'https://sim.csp.thusaac.com/api/contest/{contest_id}/problem/{problem_id}/config'

    async with httpx.AsyncClient(headers=headers) as client:
        problem_config = await client.get(problem_rul)
        problem_config = problem_config.json()['config']
        description_id = problem_config['description']
        title = problem_config['title']

        description_url = f'https://sim.csp.thusaac.com/staticdata/{description_id}.description'
        description = await client.get(description_url)
        text = description.text

        attachment = reg.findall(text)
        if attachment:
            attachment = attachment[0]
            file_name = f'CSP/examples/{attachment.split("/")[-1]}'
            text = text.replace(attachment, file_name)
            file_url = 'https://sim.csp.thusaac.com' + attachment
            res = await client.get(file_url)
            async with aiofiles.open(file_name, 'wb') as f:
                await f.write(res.content)

        images = img_reg.findall(text)
        if images:
            for image in images:
                file_name = f'CSP/attachments/{image.split("/")[-1]}'
                text = text.replace(image, file_name)
                file_url = "https://sim.csp.thusaac.com" + image
                res = await client.get(file_url)
                async with aiofiles.open(file_name, "wb") as f:
                    await f.write(res.content)
                    
        async with aiofiles.open(f'CSP/CSP{contest_id}-{problem_id+1}_{title}.md', 'w', encoding='utf-8') as f:
            await f.write(text)


async def main():
    os.makedirs("./CSP", exist_ok=True)
    os.makedirs("./CSP/attachments", exist_ok=True)
    os.makedirs("./CSP/examples", exist_ok=True)
    tasks = []
    for contest_id in range(34, 0, -1):
        for problem_id in range(5):
            tasks.append(download_problem(contest_id, problem_id))
    print('Downloading...', end='')
    await asyncio.gather(*tasks)  # x 只能await gather
    print('Done!')

asyncio.run(main())
