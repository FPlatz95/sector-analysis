import requests
import pandas as pd
from io import StringIO

data = {
        "table": "LBESK22",
        "format": "CSV",
        "variables": [
            {
                "code": "BRANCHEDB071038",
                "values": [
                    "TOT"
                ]
            },
            {
                "code": "TAL",
                "values": [
                    "1010"
                ]
            },
            {
                "code": "Tid",
                "values": [
                    "2008K1",
                    "2025K2"
                ]
            },
        ]
    }

r = requests.post("https://api.statbank.dk/v1/data", json=data)
csv_buffer = StringIO(r.text)

df = pd.read_csv(csv_buffer,sep=";")
print(df)
