import requests
import pandas as pd
from datetime import datetime, timedelta

url = "https://vegetablemarketprice.com/api/dataapi/market/noida/daywisedata"

# Specify start and end dates
start_date = datetime(2023, 12, 1)
end_date = datetime(2023, 12, 1)  # Adjust the end date as needed

desired_parameters = ["vegetablename", "price", "units", "shopingmallprice"]  # Replace with the actual parameter names you want

res = []

payload = ""
headers = {
    # Your headers here...
}

# Loop through the date range
current_date = start_date
while current_date <= end_date:
    querystring = {"date": current_date.strftime("%Y-%m-%d")}

    response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
    data = response.json()

    for item in data['data']:
        # Extract only the desired parameters from the item
        selected_data = {param: item.get(param) for param in desired_parameters}

        # Append to the result list
        res.append(selected_data)

    # Move to the next date
    current_date += timedelta(days=1)

# Create a DataFrame from the collected data
df = pd.DataFrame(res)
# print(df)

# Save the DataFrame to a CSV file
csv_filename = "vegetablefinal_dec23.csv"
df.to_csv(csv_filename, index=False)

print(f"Data saved to {csv_filename}")