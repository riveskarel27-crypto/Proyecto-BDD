import yfinance as yf
import pandas as pd

tickers_salud = [
    "BMY", "JNJ", "PFE", "MRK", "ABT",
    "LLY", "AMGN", "MDT", "UNH", "CVS",
    "CI", "BAX", "BDX", "SYK", "TMO"
]

datos = []

for ticker in tickers_salud:

    print("Descargando:", ticker)

    df = yf.download(
        ticker,
        start="1996-10-03",
        end="2026-10-03",
        interval="1d",
        auto_adjust=False,
        multi_level_index=False,
        progress=False
    )

    df = df.reset_index()

    df["Ticker"] = ticker

    datos.append(df)

precios = pd.concat(datos, ignore_index=True)

# Dejamos únicamente las columnas que nos interesan
precios = precios[
    ["Date", "Ticker", "Open", "High", "Low",
     "Close", "Adj Close", "Volume"]
]

# Cambiamos nombres para que sean cómodos en SQL
precios.columns = [
    "fecha",
    "ticker",
    "apertura",
    "maximo",
    "minimo",
    "cierre",
    "cierre_ajustado",
    "volumen"
]

precios.to_csv(
    "precios_salud.csv",
    index=False
)

print("\nLISTO")
print(precios.head())
print("\nNúmero de registros:", len(precios))
