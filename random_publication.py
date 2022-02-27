import math
import random
import pandas as pd


def main():
    randomed_publication = []
    amount = 0
    while amount != 200:
        var = random.randrange(2703, 4554)
        if (var in randomed_publication):
            continue
        else:
            randomed_publication.append(var)
            amount += 1
    print(randomed_publication)
    data = {"Publication_id": randomed_publication}
    df = pd.DataFrame(data, columns=["Publication_id"])
    df.to_excel(r'D:\random publication\random_publication.xlsx',
                index=False, header=True)


main()
