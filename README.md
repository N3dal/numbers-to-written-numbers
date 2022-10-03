# Numbers to Full-Written Number.

simple script to convert **'Integers'** and **'Floats'** to words
in simple words convert any number to the written form of it and
return it as **string**.

This project built with ![python](https://img.shields.io/badge/python-3.x-green) and ❤️.

**how it is works**:
`121 => "one hundred and twenty-one"`
`3.14 => "three point fourteen".`

### Usage:
``` py
    num2written("your-number-here")
```

### example:
```py
    written_number = num2written(1234)    
    print(written_number)
```


### Valid Inputs:
```py
    num2written(1234)
    num2written("1234")
    num2written(12_345)
    num2written("12_345")
    num2written("-11_625")
    num2written(-11_625)
```


### TODO:

- [ ] make gui app using either tkinter or gtk.
- [ ] make it work for **Floating points** numbers.
- [ ] make the script accept args from the **Terminal** directly.
