# maxLCS

Code accompanying my bachelor's thesis on the maximum number of
distinct longest common subsequences of two strings.

The thesis studies

\[
D(t)=\max_{|X|+|Y|=t} d(X,Y),
\]

where \(d(X,Y)\) is the number of distinct longest common
subsequences of strings \(X\) and \(Y\).

## Requirements

The core code requires Python 3 and uses only the Python standard
library.

## Contents

- `lcs/count.py`
  - `countLCS(x, y)`: counts the distinct LCSs of two strings.

- `lcs/exhaust.py`
  - `D(t)`: searches for a pair of strings of combined length `t`
    with a maximum number of distinct LCSs.

- `lcs/upperboundDP.py`
  - `upperBoundDPTable(m, n)`: computes the three-dimensional
    dynamic-programming upper-bound table.
  - `D_ub3(m, n, l)`: returns the upper bound for fixed string
    lengths and LCS length.
  - `D_ub2(m, n)`: maximizes over the LCS length.
  - `D_ub(t)`: maximizes over pairs of string lengths with combined
    length `t`.

## Examples

Start Python from the repository root:

```python
from lcs.count import countLCS, L
from lcs.exhaust import D
from lcs.upperboundDP import D_ub

countLCS("abba", "baab")  # 4
L("abba", "baab")         # 2

D(8)                      # maximum and an extremal pair
D_ub(16)                  # refined upper bound

## Version used for the thesis

Release `v1.0-thesis`.
