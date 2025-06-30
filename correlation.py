import pandas as pd

data = pd.read_csv('correlacion.csv')

if __name__ == "__main__":

    result = f'Correlación entre Rating e Installs: {float(data.corr().iloc[0].iloc[1])}'
    print(result)

