import pandas as pd 

df = pd.read_csv ("https://raw.githubusercontent.com/mateuspestana/datasets_aulas/main/ukraine.csv")
print(df.head(10)) # Disponibilizando apenas os 10 primeiros valores.
