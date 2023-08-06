# lakai

Lakai is a wrapper around [Lark][] that provides a convenient API.

  [Lark]: https://github.com/lark-parser/lark

## Installation

    $ pip install lakai

## Usage

```py
import lakai
grammar = r"""
    %ignore /\s+/
    %import common.INT
    ?atom: INT
    ?!product: atom | product "*" atom | product "/" atom
    ?!sum: product | sum "+" product | sum "-" product
"""
parser = lakai.from_string(grammar, start="sum")
tree = parser.parse("1 + 3 * 2 + 4 / 2")
lakai.pprint(tree)
```

Gives

```
sum
    sum
        INT: '1'
        PLUS: '+'
        product
            INT: '3'
            STAR: '*'
            INT: '2'
    PLUS: '+'
    product
        INT: '4'
        SLASH: '/'
        INT: '2'
```

To evaluate the expression, you can use a `lakai.Transformer`:

```py
import operator

class Computer(lakai.Transformer):
    operators = {"/": operator.truediv, "*": operator.mul, "-": operator.sub, "+": operator.add}

    def visit_INT(self, leaf: lakai.Leaf) -> int:
        return int(leaf.value)

    def visit_product(self, node: lakai.Node[Any]) -> int:
        return self.operators[node.children[1].value](node.children[0], node.children[2])

    visit_sum = visit_product

assert Computer().visit(tree) == 9
```


To use Lakai with a Lark standalone parser:

```py
import lakai
from ._standalone import Lark_Standalone
parser = lakai.Lakai(Lark_Standalone())
```
