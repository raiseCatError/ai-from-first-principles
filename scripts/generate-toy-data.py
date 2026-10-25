"""Generate openly usable synthetic regression data, never downloaded private data."""
import csv
import random
from pathlib import Path
r=random.Random(17)
p=Path(__file__).resolve().parents[1]/'exercises'/'week-01'/'toy_regression.csv'
with p.open('w',newline='') as f:
    w=csv.writer(f);w.writerow(['x','y'])
    for i in range(100):
        x=i/10
        w.writerow([round(x,4),round(2.5*x-1+r.gauss(0,.35),4)])
print(f'Wrote {p}')
