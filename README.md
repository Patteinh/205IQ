# 205IQ 🧠

Welcome to **205IQ**.

This project involves using mathematical modeling to analyze IQ scores based on a normal distribution.

## Language and Tools 🛠️

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

- **Language:** Python
- **Compilation:** Via Makefile, including `re`, `clean`, and `fclean` rules.
- **Binary Name:** 205IQ

## Project Overview 🔎

The objective of 205IQ is to create a program that computes the probability of an individual having a specific IQ score, or a range of IQ scores, based on the normal distribution.

It involves calculating the percentage of people within certain IQ ranges.

### Key Features

- **Normal Distribution Analysis:** Calculate the probability of IQ scores using the normal distribution model.
- **IQ Score Calculation:** Provide statistics for specific IQ scores or ranges.
- **Command-Line Interface:** Design a user-friendly interface for input and result display.

### Usage

```
∼> ./205IQ -h
USAGE
    ./205IQ u s [IQ1] [IQ2]
DESCRIPTION
    u     mean
    s     standard deviation
    IQ1   minimum IQ
    IQ2   maximum IQ
```

### Exemples

```
∼> cat drawer.gnu
set terminal pngcairo
set output ‘image.png’
set nokey
plot ‘data’

∼> ./205IQ 100 15 > data
∼> head -n 2 data
0 0.00000
1 0.00000
∼> head -n 120 data | tail -n 10
110 0.02130
111 0.02033
112 0.01931
113 0.01827
114 0.01721
115 0.01613
116 0.01506
117 0.01399
118 0.01295
119 0.01192
∼> tail -n 2 data
199 0.00000
200 0.00000
2
```

## Installation and Usage 💾

1. Clone the repository.
2. Compile the program using the provided Makefile.
3. Run the program: `./205IQ u s [IQ1] [IQ2]`.
4. For detailed guidelines, refer to `205IQ.pdf`.

## License ⚖️

This project is released under the MIT License. See `LICENSE` for more details.
