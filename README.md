#  MiGS Payment Gateway for python
### Overview
This code will help you to generate a working URL to redirect the customer to the payment gateway using the 2-Party Payment Model that MiGS user to pay a prespecified amount.

## Getting Started

### Prerequisites
Just clone the project and make sure you have installed python on your OS.

### Usage
Just replace **vpc_Merchant**, **vpc_AccessCode** and **vpc_SecureHash** with your values, then:
```
> python main.py
```
### SHA-256 HMAC hashing
Don't worry about the required hashing calculation!
I am doing it for you using the SHA-256 algorithm in the required way by the MiGS to generate the **vpc_SecureHash** value.


## Important Note
For **vpc_Amount**. values Its value must not contain any decimal points, thousands separators or currency symbols. For example:
> $12.50 is expressed as 1250

## Built With
[Python 2.7](https://www.python.org/download/releases/2.7/)

## Authors
[Rabii Desouki](https://www.linkedin.com/in/rabii-desouki/)





