
* Trie: problem 336
    * problem 208
    * problem 212
    * problem 211
    * A very simple implementation with `dict` in [stackoverflow](https://stackoverflow.com/questions/11015320/how-to-create-a-trie-in-python)
      I and Stefan used this one in 211
    * The similar approach is also used in 472 and 648
    * Google's implementation: [github](https://github.com/google/pygtrie)

* Here is the way

```python
trie = {}
 for word in dict:
     current_dict = trie
     for c in word:
         current_dict = current_dict.setdefault(c, {})
     current_dict['_end_'] = '_end_'
 print(trie)
 def search(word):
     current_dict = trie
     for i, c in enumerate(word):
         if '_end_' in current_dict:
             return word[:i]
         elif not c in current_dict:
             break
         current_dict = current_dict[c]
     return word
```

* A similar but fancier approach I saw in awice's post of `648_Replace_Words.py`

```python
_trie = lambda: collections.defaultdict(_trie)
trie = _trie()
END = True
for root in roots:
    cur = trie
    for letter in root:
        cur = cur[letter]
    cur[END] = root

def replace(word):
    cur = trie
    for letter in word:
        if letter not in cur: break
        cur = cur[letter]
        if END in cur:
            return cur[END]
    return word
```

* Trie problem can add more information to a node, in addition to `_end_`
    * like `336_Palindrome_Pairs.py`, I added `_palindrome_` 
