# CT-NAS [![PyPI version](https://badge.fury.io/py/ctnas.svg)](https://badge.fury.io/py/ctnas) ![Tests](https://github.com/innvariant/ctnas/workflows/Tests/badge.svg) [![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/) [![Python 3.7](https://img.shields.io/badge/python-3.7-blue.svg)](https://www.python.org/downloads/release/python-370/) [![Python 3.8](https://img.shields.io/badge/python-3.8-blue.svg)](https://www.python.org/downloads/release/python-380/)
This module contains an API access to a Neural Architecture Search dataset on a search space called "computational themes".
Such themes are small directed acyclic graphs (DAGs) with a vertex collapse condition.
This condition makes the left and the right graph in the picture being equivalent / isomorphic.

The dataset contains computations of feed-forward neural networks with different hidden structural priors based on these themes.
By this, you can search for connections between graph theoretic properties of the search space and computational properties of the neural network models. 

![Computational Themes](res/compthemes-three-examples.drawio.png)

## Installation
Via *poetry* (**recommended** for projects) using PyPi:
``poetry add ctnas``

Directly with *pip* from PyPi:
```bash
pip install ctnas
```

Via *conda* in your *environment.yml* (recommended for reproducible experiments):
```yaml
name: exp01
channels:
- defaults
dependencies:
- pip>=20
- pip:
    - ctnas
```

From public GitHub:
```bash
pip install --upgrade git+ssh://git@github.com:innvariant/ctnas.git
```

## Usage examples
```python
from ctnas.api import CTNASApi

api = CTNASApi()
print(api.get_datasets())
# Should give you:
# ['spheres-b8c16fd7', 'mnist', 'spheres-23aeba4d', 'spheres-bee36cd9',
#  'spheres-b758e9f4', 'spheres-0a19afe4', 'cifar10', 'spheres-6598864b']
```

```python
from ctnas.api import CTNASApi

api = CTNASApi()
print(api.get_graph_properties().head())
```
Gives you s.th. like:
> test_dev.py .                             graph_uuid  num_nodes  ...  degree_var  undir_ecc_var
0  6e302aa7-6208-42a9-b1e0-08ce6d9d83ba          6  ...    1.222222       0.222222
1  ecd9c934-90ae-460c-855f-90c0b24a4150          6  ...    0.666667       0.000000
2  d111e38f-3ed1-454f-9d0e-8ded0428c9d9          6  ...    1.000000       0.222222
3  d23cac47-047c-4ec6-aaa4-e393b2ebeccd          5  ...    0.640000       0.240000
4  c56bb6f8-a9ec-44db-8c17-37b166fb5b06          6  ...    0.888889       0.222222
> 
> [5 rows x 19 columns]

```python
import networkx as nx
import matplotlib.pyplot as plt
from ctnas.api import CTNASApi

api = CTNASApi()
graph = api.get_graph("0a1ded7d-677a-41f7-9361-c7079c8a34a7")
nx.draw(graph)
plt.show()
```


## Cite our work
```bibtex
@misc{stier2022ctnas,
    title={CT-NAS: Analysis of Hidden Structural Priors for Neural Architecture Search},
    author={Julian Stier and Michael Granitzer},
    year={2022}
}
```

## MinIO Policy
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": [
        "s3:GetObject"
      ],
      "Effect": "Allow",
      "Resource": [
        "arn:aws:s3:::homes/stier/ctnas/*"
      ]
    }
  ]
}
```
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": [
        "s3:GetObject"
      ],
      "Effect": "Allow",
      "Principal": {
        "AWS": [
          "*"
        ]
      },
      "Resource": [
        "arn:aws:s3:::homes/stier/ctnas/*"
      ],
      "Sid": ""
    }
  ]
}
```