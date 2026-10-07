import requests
import pandas as pd
import datetime

url = "https://vegetablemarketprice.com/api/dataapi/market/noida/daywisedata"

start = datetime.date(2022, 2, 1)
end = datetime.date(2022, 2, 5)

delta = datetime.timedelta(days=1)
res = []

while(start <= end):
    headers = {
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.9",
    "Connection": "keep-alive",
    "Cookie": "_ga=GA1.1.1793791970.1705388786; JSESSIONID=C86FF9F12501A7D791368898B2438EF1; __gads=ID=f42df9f4e1935fbb:T=1705388785:RT=1705584686:S=ALNI_MZnD5lr3O4IK52Hn_9hfykh8_aM9Q; __gpi=UID=00000cdf20a26959:T=1705388785:RT=1705584686:S=ALNI_MZO_1axMVxhapkmQgOgPtzS1z2RtA; FCNEC=^%^5B^%^5B^%^22AKsRol-kTZg7-xNOu8X01HaW_GBgFKMdGnONVYNouAIj27xrfo5YzJM9fKt6nt-iTvl4U2g8lmoYGFvvRn5dvzNERKY3TJEL-tTxBJ1ivOwITvQW13cOqlC3-KRTjWEtAIXnSd2-jJs2m3ryUWc4HFpLAkRJGToGZA^%^3D^%^3D^%^22^%^5D^%^5D; _ga_2RYZG7Y4NC=GS1.1.1705584684.9.1.1705584811.0.0.0",
    "Referer": "https://vegetablemarketprice.com/market/noida/today",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "sec-ch-ua": "^\^Not_A",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "^\^Windows^^"
    }

    response = requests.request("GET", url, headers=headers, params=start)

    data = response.json()

    for p in data['data']:
        res.append(p)

    start += delta

df = pd.json_normalize(res)
print(df)