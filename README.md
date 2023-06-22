# Simple ATM Controller for Bear Robotics

The flow in this ATM controller:\
Insert Card => PIN number => Select Account => See Balance/Deposit/Withdraw

## How to run it

1. Clone this repository where you want.\
   `git clone https://github.com/InhyeongPark/simple-ATM.git`
2. Run main.py by doing\
   `python main.py`

## About Code

### main.py

The result can be checked on this main.py file

### BankAccount.py

This one creates a BankAccount class with the account number. The balance starts from $0.
It can check the current balance of the account and deposit as well.
It can also withdraw a given amount from the account. It will return -1 if the amount exceeds the current balance or 1 if not.

### Client.py

This one creates a Client class with first name, last name, and password.
It also has a dictionary with the key as the account number and the value as the account.

## Setup

<img src="https://github.com/InhyeongPark/simple-ATM/blob/main/img/setup.png" alt="Setup" style="width: 350px;">
There are two clients: Michel Lee and Paul Park.<br>
They have one card each, and the password is 7777 and 8888.<br>
Michel Lee has two accounts. The number of the first account is 111111111, and the next one is 222222222.<br>
Paul Park has one account with the 333333333.<br>

## Start

<img src="https://github.com/InhyeongPark/simple-ATM/blob/main/img/img1.png" alt="Setup" style="width: 400px;">
1. By pressing 1, this code will think of it as inserting the card.

---

<img src="https://github.com/InhyeongPark/simple-ATM/blob/main/img/img2.png" alt="Setup" style="width: 400px;">
Before we started, we made two cards. Therefore, you can choose one of them. Let's say we select the first one.

---

<img src="https://github.com/InhyeongPark/simple-ATM/blob/main/img/img3.png" alt="Setup" style="width: 400px;">
Now, we need to type in the password. If the password is correct, it will show the client's name and tell us to choose the account number.

---

<img src="https://github.com/InhyeongPark/simple-ATM/blob/main/img/img4.png" alt="Setup" style="width: 400px;">
If we type in the correct number, it will give us four actions.

---

<img src="https://github.com/InhyeongPark/simple-ATM/blob/main/img/img5.png" alt="Setup" style="width: 400px;">
If we click 1, it will give us the balance and return.

---

<img src="https://github.com/InhyeongPark/simple-ATM/blob/main/img/img6.png" alt="Setup" style="width: 400px;">
If we click 2, it will add the amount to the balance and return.

---

<img src="https://github.com/InhyeongPark/simple-ATM/blob/main/img/img7.png" alt="Setup" style="width: 400px;">
If we click 3 but withdraw more than the current balance, it will fail and return.

---

<img src="https://github.com/InhyeongPark/simple-ATM/blob/main/img/img8.png" alt="Setup" style="width: 400px;">
If we click 3 and withdraw less than the current balance, it will show the current balance and return.

---

<img src="https://github.com/InhyeongPark/simple-ATM/blob/main/img/img9.png" alt="Setup" style="width: 400px;">
When we click 0, then it will quit this service.
