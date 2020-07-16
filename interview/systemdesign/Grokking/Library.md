
# A library system

## Requirements and Goals of the System

* Functional Requirements:
    * Users should be able to search the book given name (Read)
    * Users should be able to checkout and return books (Write)

## Capacity Estimation and Constraints (Back-of-the-envelope)

* Read heavy, assume 10:1 read:write 
* Traffic estimates
    * Each student checkout / return 3 books per month ~ 0.1 books per day
    * 10000 students in the campus
    * 1000 checkout + 1000 return per day
    * 0.01 write / s
    * 0.1 read / s

## System APIs (System interface definition)

```python
checkout(user_info, isbn)
return(user_info, isbn)
search(user_info, isbn)
```

## DB Design (Defining data model)
