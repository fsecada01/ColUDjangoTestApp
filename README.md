# Instructions:

1. Go to url https://repl.it/@AhmadFaizal/PES
2. Login and open the repo
3. Do the Solve below mentioned problem statement and save
4. Share the link after you edit (when you edit and save it will create a fork of repo into your directory and hence will have a different url)


## Problem statement:

1. Create Following model structure and add admin

## Model Class (Tables)

### User - user default Django User
### Author - Custom Model bellow are fields and its type
[x]  name - char with max length 25
[x] address ­-  text

### Book - Custom Model bellow are fields and its type
[x] title - char with max length 100
[x] description - text
[x] count - positive integer
[x] subscription_cost - positive integer
[x] topic - char with max length 20 
[x] author - array of reference to Author
 

### Subscriber - Custom Model bellow are fields and its type
[x] user - reference to User table
[x] address - text
[x] phone - phone number   

### Subscription - Custom Model bellow are fields and its type
[x] subscriber - reference to  Subscriber table
[x] book -  reference to  Book table
[x] borrowed_date - date( date of creaton)
[x] amount_paid - positive integer
[x] days - positive integer
[x] returned - Boolean


2. Create Django rest API List, Detailed, create, update, and delete view for all the above Models including User model
3. Create following APIs:
	[x]	List all books of specific author that are available in the library
	[x]	List all books given a topic (match topic case insensitive way)
	[ ]	List all Subscribers  who didn’t return (returned=False) who’s subscription expired (expiry = borrowed_date  + days)
	[ ]	Add attribute due_amount in Subscription detailed view (due_amount=(Book. subscription_cost[ ] Subscription.days)  - Subscription.amount_paid)
	[ ]	Make sure can add subscription only if there is book in library (books in library = Book.count – subscription of book that are not returned)