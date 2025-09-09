import threading
import re
from pathlib import Path
import pandas as pd

# pake regex untuk kata-katanya
WORD_RE = re.compile(r"[A-Za-z']+")

# global variable agar bisa diakses dari dalam fungsi maupun dari main 
jumlahKata = {}
lock = threading.Lock()

# menghitung jumlah kata dalam file (fungsi)
def HitungKataDalamFile(files):
    lokal = {}
    for fname in files:
        text = Path(fname).read_text(encoding="utf-8", errors="ignore").lower()
        for w in WORD_RE.findall(text):
            lokal[w] = lokal.get(w, 0) + 1
    # gabungkan ke global variabel dengan lock
    with lock:
        for w, c in lokal.items():
            jumlahKata[w] = jumlahKata.get(w, 0) + c

if __name__ == "__main__":
    # contoh file
    files = ["a.txt", "b.txt", "c.txt"]

    # bagi kerja ke 2 thread
    mid = len(files)//2
    t1 = threading.Thread(target=HitungKataDalamFile, args=(files[:mid],))
    t2 = threading.Thread(target=HitungKataDalamFile, args=(files[mid:],))

    # Start + join
    t1.start(); t2.start()
    t1.join(); t2.join()
    
    df = pd.DataFrame(sorted(jumlahKata.items(), key=lambda kv: kv[1], reverse=False));

    # Print hasil
    print(df.to_string())

