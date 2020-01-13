#!/usr/bin/env python3
#
# author: andreasl
import numpy as np
import pandas as pd

def read_csv(path: str) -> pd.DataFrame:
    df = (pd
        .read_csv(
            path,
            engine='python',
            parse_dates=['date'],
            date_parser=lambda x: pd.datetime.strptime(x, '%Y-%m-%d'),
            sep=','))
    df = df.set_index(df.date)

    return df
