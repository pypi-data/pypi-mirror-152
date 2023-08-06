# Pandas Prototype

**_Love torturing data ? Cause if you torture the data it will confess! Feel the data talking to you #AliveData._**

A package with implementation of famous `Pandas` library in my way , allows you to visualize data using data tables.

![Pandas Prototype](https://sanmeet007.github.io/python-protos/images/pandas_prototype.png)

---

**Requires python version 3.10 or later**

<!--  Sample code  , pip install command -->

## General Overview

- Makes your data feel alive .
- You can filter , print , convert and do lot more with this.
- Uses prettytable , json , json2html like libraries under the hood for better functioning.
- Made by dev for devs and data scientists ^\_^
- Compatible with python version 3.10 or above

### Dependencies :

- `json2html` : for converting data_list to html table
- `prettytable` : for printing tables using ascii

### Getting started

To install this package use pip command:

```powershell
 pip install pandas_prototype
```

This is an example of how to use DataFrame class to pretty print tables and make your data alive.

1. Declaring a variable which stores the instance of the DataFrame class (i.e. now variable stores `DataFrame object`)

   ```python
   data = DataFrame(
       [
           {
               "id": 1,
               "body": "Hello wolrdEnim sunt ex cupidatat occaecat eiusmod aute .",
               "uuid": "ghjk3878j321134",
               "color": "red",
           },
           {
               "id": 2,
               "body": "Ex aute adipisicing esse do excepteur dolore. ",
               "uuid": "eihr8rhre8013nqfwe-9u",
           },
           {
               "id": 3,
               "body": "Elit consectetur nisi esse fugiat anim irure.",
               "uuid": "b08349m320m=-081",
           },
       ] , ["uuid" , "id" , "data"] , indexed=False
   )

   ```

1. Printing the DataFrame object to console

   ```python
   print(data)
   ```

---

## DataFrame Class :

This is the main class which is responsible for generating methods and atrributes which can be used for data filetering and other stuff.
It takes a list as paramter , this list is then processed by it's initializer where all the magic happens !

### Constructor parameters

```python
DataFrame(data_list , headers, **kwargs)
```

1.  data_list (param1) : The first parameter is the data list which must have a type of list. All the data objects are created from this list.

2.  headers (param2) : It is an `optional` parameter which basically controls the order of headers when printed.It must be a list type . By default the order of headers is sorted. To change this behaviour pass a list of headers which are basically the keys present in the data .Example :

    ```python
        data = DataFrame([
            {
                "id": 1,
                "data": "..."
            }
            {
                "id": 2,
                "data": "..."
            }
        ]  , ["id" , "data"]) # Try adding data first instead of id

    ```

    In this above example we are passing the order of the headers in a way the `id` appears first and all others heads comes after it. In above example if one or more keys are not present then they will be sorted in ascending order and then printed !

    > Note : The list which is passed must contain the exact head as keys of the list otherwise DataFrame will try to create a seperate coloumn for that head leading to corrupting the data.

3.  \*\*kwargs : These are optional parameters which can be send to the DataFrame constructor . Right now only one kwarg is supported named `indexed` which when set to true will print indexes with the DataFrame object.(By default set to false)

## DataFrame methods

- `data.to_list()` : returns the current DataFrame object in python list.
- `data.to_json()` : converts the current DataFrame object to json format.
- `data.to_html()` : converts the current DataFrame object to html table.
- `data.to_csv()` : converts the current DataFrame object to csv.
- `data.export()` : Exports your current to a file.

### Export method

This method when called on the DataFrame instance first converts the DataFrame object to specified format ( default `json` format if not specified ) and then dumps the data to output file whose name is passed as an argument .

Example:

```python
    data = DataFrame(...)
    data.export(file_name="filename" , format="json" , directory=".")
```

> Note : By default the file is written in current directory. You can change this behaviour by passing directory as kwarg to the method.

---

## Data attributes

### Basics :

These are basically the keys common to the all the items passed as a dict wrapped around list , these are generated on the fly and have thier own methods and comparsion operations these can be used to cycle through each element and find out a paricular element which statisfies the condition.

> NOTE : if one or two elements miss a certain key then the DataFrame initialzer generates it for you which is initialized with a value of `None`

Here's how these are generated :

```python
    data = DataFrame([{
        "id" : "some_value" ,
        "__attr": "..." # just an example
    }])
    # DataFrame's initializer generates these .id and other attrs automatically
    data.id
```

### Printing the attributes :

When a DataFrame attribute is printed it prints out the attributes in indexed order .

```python
    print(data.id)
```

---

## Data attribute operations & methods :

Here are some opertaions or methods you can use or call on attributes inorder to filter your data\*list. Remember these operations are methods are called for each item in the data\*list and then compared against the statement ... Hence returning a dataframe `_dbool` object which when used with `data[_dbool]` returns a filtered out items.

> To print the filtered data_list just use the simple print function . Example print(data)

### Comparison statements :

In general, a comparison statement is simply a statement in which two quantities or values are being compered. So , these are used to compare the attribute values automatically generated by the DataFrame initializer.

#### 1. Lesser than (<)

With < we can filter out those ids in data with a value lesser than the desired integer. Consider the example below , it returns a new DataFrame object with filtered ids :

```python
    data[data.id < 5]
```

#### 2. Lesser than equal to (<=)

With <= we can filter out those ids in data with a value lesser than the desired integer. Consider the example below , it returns a new DataFrame object with filtered ids :

```python
    data[data.id <= 5]
```

#### 3. Greater than (>)

With > we can filter out those ids in data with a value greater than the desired integer. Consider the example below , it returns a new DataFrame object with filtered ids :

```python
    data[data.id > int(5)]
```

#### 4. Greater than equal to (>=)

With >= we can filter out those ids in data with a value greater than or equal to the desired integer. Consider the example below , it returns a new DataFrame object with filtered ids :

```python
    desired_int = 1
    data[data.id  >= desired_int]
```

#### 5. Equals (==)

With == we can filter out those ids in data with a value equal to the desired left side value. Consider the example below , it returns a new DataFrame object with filtered colors:

```python
    desired_color = "red"
    x = data[data.color == desired_color]
    print(x)
```

> NOTE : If `data.id == 10` is prinited then a \_dbool object is printed.

### Using methods on attributes as statements :

#### 1. Ends with method

Returns the \_dbool object with only those index of color being true which ends the sepcific string or character

```python
    data.color.endswith("i")
```

#### 2. Starts with method

Returns the \_dbool object with only those index of color being true which starts the sepcific string or character

```python
    val = "r"
    data.color.startswith(val)
```

#### 3. Includes method

Returns the \_dbool object with only those index of color being true which includes the sepcific string or character

```python
    val = "ed"
    data.color.include(val)
```

### Chaining statements (Logical) :

#### 1. Logical and (&)

Performs basic `and` operation ,
& comapres two `\_dbool` object and returns a new `\_dbool` object which can be used against the orignal DataFrame object to get the desired items. Example:

```python
    # Note : The operator precedence is also important !
    print(data[(data.id == 1) & (data.color.icludes("ed")) ])
```

> Note : Use bitwise and (&) instead of logical and (and) operator to perform and logic.

#### 2. Logical or ( | )

Performs basic `or` operation ,
| comapres two `\_dbool` object and returns a new `\_dbool` object which can be used against the orignal DataFrame object to get the desired items. Example:

```python
    # Note : The operator precedence is also important !
    print(data[(data.id > 2) | (data.color.icludes("ed"))])
```

> Note : Use bitwise and (&) instead of logical and (and) operator to perform and logic.

---

## Inbuilt Objects & Classes:

- ### DataFrame boolean :

  The `_dbool` sub-class is used to create an object from it which is used for comparsion , logical statements and finally used by DataFrame to print only the values returned true

- ### DataFrame attribute :

  The `data.$attr` is an instance of DataFrame attribute class ( generated at run time )

---

#### Developer contact

_Email_ : ssanmeeet123@gmail.com

_For any quries feel free to contact ^\_^_

---

Thank you ;-)
