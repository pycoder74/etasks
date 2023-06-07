import aiohttp
import tkinter as tk
import asyncio
import numpy as np
import datetime as dt
from datetime import datetime
import urllib.request
import sys
import json

async def get_weather(master=None):
    try: 
      ResultBytes = urllib.request.urlopen("https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/Bristol?unitGroup=metric&elements=temp&include=current%2Cfcst&key=3UQS226XB878JKZZPG2JDJWDQ&contentType=json")
      
      # Parse the results as JSON
      jsonData = json.load(ResultBytes)
      ctemp = jsonData['currentConditions']
      ctemp = tk.Label(master, text=ctemp)
      ctemp.pack()
    except urllib.error.HTTPError  as e:
      ErrorInfo= e.read().decode() 
      print('Error code: ', e.code, ErrorInfo)
      sys.exit()
    except  urllib.error.URLError as e:
      ErrorInfo= e.read().decode() 
      print('Error code: ', e.code,ErrorInfo)
      sys.exit()
      
if __name__ == '__main__':
    win=tk.Tk()
    asyncio.run(get_weather(win))

