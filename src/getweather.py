import aiohttp
import tkinter as tk
import asyncio
async def get_weather(master=None):
    url=f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/Bristol"
    params = {
        "unitGroup": "metric",
        "include": "current",
        "key": "5H2F2M6K2X4E9LXKH7UP3DNMQ",
        "contentType": "json"
    }
    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params) as response:
            if response.status != 200:
                print('Unexpected status code:', response.status)
            jsonData = await response.json()
            current_temp = jsonData['currentConditions']['temp']
            current_temp = f"{current_temp}°C"
            print(current_temp)
            weather=tk.Label(master, text=current_temp, font=('calibri', 20))
            weather.pack(anchor='center', side=tk.LEFT, padx=100)
if __name__ == '__main__':
    win=tk.Tk()
    asyncio.run(get_weather(win))
