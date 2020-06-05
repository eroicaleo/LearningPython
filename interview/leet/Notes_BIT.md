
# Topcoder notes

## Notation

* `f[i]`: frequency at index `i`
* `c[i]`: cumulative frequency from 1 to i, i.e. `f[1]+...+f[i]`
* `tree[i]`: define later
* `f[0] = c[0] = tree[0] = 0`

## Basic idea

* idx be an index of BIT, `r` is the position of the least significant
  non-zero bit of idx. `tree[idx] = f[idx-2^r+1]+...+f[idx]`

## Read cumulative frequency

```python
    def read(self, idx):
        s = 0
        while idx:
            s += self.tree[idx]
            idx -= (idx & -idx)
        return s
```

## Change the frequency at some position

```python
    def update(self, idx, val):
        while idx <= self.MaxIdx:
            self.tree[idx] += val
            idx += (idx & -idx)
```

## Read the frequency at idx

* The idea is like this: calculate the cumsum[idx] and cumsum[idx-1]
* Then `f[i] = cumsum[idx]-cumsum[idx-1]`
* But you don't have to compute the whole `cumsum[idx]` and `cumsum[idx-1]`
* Let `idx = a1(~b)` and `idx-1 = a0b`, `b` is a all 1 string.
* `cumsum[idx] = cumsum[a0(~b)]+tree[idx]`
* `cumsum[idx-1] = cumsum[a0(~b)]+tree[]+...+tree[]`

* For example: `idx = 12 = 1100, idx-1 = 11 = 1011`
    * cumsum[12] = tree[1100] + tree[1000]
    * cumsum[11] = tree[1011] + tree[1010] + tree[1000]

```python
    def readSingle(self, idx):
        s = self.tree[idx]
        if idx > 0:
            z = idx - (idx & -idx)
            idx -= 1
            while idx != z:
                s -= self.tree[idx]
                idx -= (idx & -idx)
        return s
```

## Scaling the entire tree 

## Get the frequency

* This is version of binary search

```python
    def find(self, cumFre):
        idx, bitMask = 0, 1
        while bitMask <= self.MaxIdx:
            bitMask <<= 1
        bitMask >>= 1

        while bitMask > 0:
            tIdx = idx + bitMask
            bitMask >>= 1
            if tIdx > MaxIdx:
                continue
            if cumFre == self.tree[tIdx]:
                return tIdx
            elif cumFre > tree[tIdx]:
                idx = tIdx
                cumFre -= tree[tIdx]
        return idx if cumFre == 0 else -1
```

## Some variants

* `493_Reverse_Pairs.py`

# Typical problems in Leetcode

* `493_Reverse_Pairs.py`
* `315_Count_of_Smaller_Numbers_After_Self.py`
* `327_Count_of_Range_Sum.py`
