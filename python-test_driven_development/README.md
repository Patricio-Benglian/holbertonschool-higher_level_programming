## Test Syntax

```
The ``{filename}`` module
======================

Using ``{function}``
-------------------

    >>> {function} = __import__('{filename}').{function}
    
    >>> {function}()
    {expected output}
```

*** Make sure these tests cover as many possible edge cases imaginable. ***

To test: ``` python3 -m doctest -v ./tests/1-my_list.txt | tail -2 ```
Remove ``` | tail -2 ``` to see entire output

## Common Test Cases

- Function with no arguments passed
- Cases for all exceptions raised
- During arithmetic, passing float('inf')
- Passing None as argument
- When function has optional arguments, leave that argument blank

