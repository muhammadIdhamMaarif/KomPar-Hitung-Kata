# KomPar Hitung Kata

**KomPar Hitung Kata** (an abbreviation of *Komputasi Paralel: Menghitung Kata*) is a lightweight Python project that demonstrates how to perform parallel word counting across multiple text files.  
By leveraging Python’s built‑in `threading` module and regular expressions, this project reads a collection of files, counts the occurrence of each word, and presents the results as a tidy table using `pandas`.  
It was created as a simple example for the *Computer Architecture/Parallel Programming* course and is designed to be easy to understand and extend.

## ✨ Features

| Feature | Description |
| --- | --- |
| **Multi‑threaded processing** | Utilises Python’s `threading` module to divide the workload between two threads, speeding up word counting on large text files. |
| **Regex‑based tokenisation** | Uses a regular expression (`[A‑Za‑z']+`) to cleanly extract words from text, ignoring punctuation and numbers. |
| **Customisable input** | The list of files to process can easily be modified in `main.py` or passed programmatically, allowing you to analyse any collection of `.txt` files. |
| **Tidy output** | Results are aggregated into a `pandas.DataFrame` and printed as a table sorted by frequency, making it straightforward to inspect or save. |
| **Jupyter notebook** | An interactive notebook (`Kompar_Menghitung_Kata.ipynb`) walks through the code step‑by‑step, includes explanatory markdown cells, and can be executed live for experimentation. |

## 🗂️ Repository structure

├── main.py                   
├── Kompar_Menghitung_Kata.ipynb  
└── a.txt, b.txt, c.txt       

---

````
## 🛠️ Requirements

- Python 3.7 or higher
- `pandas` for tabular output

You can install the single dependency with `pip`:

```bash
pip install pandas
````

> **Note**: The `threading` and `re` modules used in this project are part of the Python standard library and require no extra installation.

## 🚀 Usage

### Run the script

The quickest way to get started is to run the provided script against the example files:

```bash
# clone this repository or download the files
git clone https://github.com/muhammadIdhamMaarif/KomPar-Hitung-Kata.git
cd KomPar-Hitung-Kata

# ensure pandas is available
pip install pandas

# run the program
python main.py
```

The script will read the list of filenames defined near the bottom of `main.py` (by default `a.txt`, `b.txt` and `c.txt`), spawn two threads to process the files in parallel, and output a table of word counts sorted by frequency.
To analyse your own files, modify the `files` list in `main.py` accordingly.

### Use the Jupyter notebook

If you prefer an interactive explanation, open the notebook in Jupyter:

```bash
jupyter notebook Kompar_Menghitung_Kata.ipynb
```

The notebook includes markdown cells describing each step, and code cells you can execute to see intermediate results. It’s a great way to tinker with the regular expression, adjust the threading strategy, or visualise the resulting word frequencies.

## 📈 Example output

Running the script on the provided sample files yields the following top 10 most common words:

```text
Word	Count
a	75
and	65
to	63
the	59
we	43
segmentation	37
of	32
model	31
in	31
for	26
```

These counts are derived from the combined contents of `a.txt`, `b.txt`, and `c.txt`, which are excerpts from research papers.
Your own inputs will naturally produce different distributions.

## 🧠 How it works

At its core, `main.py` defines a function `HitungKataDalamFile(files)` that:

1. Reads each file’s contents into memory using `Path(fname).read_text()`.
2. Converts text to lowercase and extracts all words via a compiled regular expression (`WORD_RE`).
3. Maintains a local dictionary (`lokal`) counting occurrences within the current thread’s subset of files.
4. Uses a global dictionary (`jumlahKata`) protected by a thread lock (`lock`) to merge local counts safely.

Two threads are created to process halves of the file list concurrently. Once both threads finish, the accumulated dictionary is converted into a `pandas.DataFrame`, sorted, and printed.
Feel free to experiment with more threads or alternative concurrency models such as `multiprocessing` for CPU‑bound workloads.

## 📚 Extending the project

This repository is intentionally simple, making it a great foundation for learning or experimentation. Here are a few ideas for extending it:

* **Additional preprocessing** – implement stop‑word removal or stemming to focus on meaningful terms.
* **Large‑scale datasets** – modify the thread allocation to handle hundreds of files or explore asynchronous I/O for even faster throughput.
* **Data visualisation** – use libraries like `matplotlib` or `seaborn` to create bar charts or word clouds from the result DataFrame.
* **Command‑line interface** – wrap the script in an argument parser (`argparse`) to allow specifying input files and number of threads at runtime.

## 📜 License

This project is shared for educational purposes. If you wish to use it in a different context or redistribute it, please contact the repository owner for clarification.

## 🙏 Acknowledgements

The example texts included (`a.txt`, `b.txt`, `c.txt`) are excerpts from publicly available research papers and are used solely for demonstration.
The decorative banner was generated using an AI‑assisted tool.

---

Feel free to open an issue or submit a pull request if you spot an error or have ideas for improvements. Happy coding! 👩‍💻👨‍💻

