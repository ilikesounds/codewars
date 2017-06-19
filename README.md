# codewars

This repo contains all solutions to Codewars Katas as I complete them. Each kata is on it's own branch. Descriptions of the katas are listed below.

---
#### Reverse or Rotate :
TBD


#### Sequence Sum :
TBD

#### [Are they the same?] [ATTS] :

Given two arrays `a` and `b` write a function comp(a, b) that checks whether the two arrays have the "same" elements, with the same multiplicities. "Same" means, here, that the elements in `b` are the elements in `a` squared, regardless of the order.

_Examples_ :
```python
a = [121, 144, 19, 161, 19, 144, 19, 11]
b = [121, 14641, 20736, 361, 25921, 361, 20736, 361]
```

`comp(a, b)` returns true because in `b` 121 is the square of 11, 14641 is the square of 121, 20736 the square of 144, 361 the square of 19, 25921 the square of 161, and so on. It gets obvious if we write `b`'s elements in terms of squares:

```python
a = [121, 144, 19, 161, 19, 144, 19, 11]
b = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
```

If we change the first number to something else, `comp` may not return true anymore:

```python
a = [121, 144, 19, 161, 19, 144, 19, 11]
b = [132, 14641, 20736, 361, 25921, 361, 20736, 361]
```

`comp(a,b)` returns false because in `b` 132 is not the square of any number of `a`.

[ATTS]: https://www.codewars.com/kata/550498447451fbbd7600041c/train/python "Codewars: Are They The Same?"
