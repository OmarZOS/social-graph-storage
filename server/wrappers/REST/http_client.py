

import httpx

async def send_data(destination,data):
    res = await httpx.post(destination,data)
    return res

