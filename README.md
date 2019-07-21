#Instructions:

1. Go to url https://repl.it/@AhmadFaizal/PES
2. Login and open the repo
3. Do the Solve below mentioned problem statement and save
4. Share the link after you edit (when you edit and save it will create a fork of repo into your directory and hence will have a different url)


##Problem statement:

1. Create Following model structure and add admin

##Model Class (Tables)

###User - user default Django User
###Author - Custom Model bellow are fields and its type
- name - char with max length 25
- address ­-  text

###Book - Custom Model bellow are fields and its type
- title - char with max length 100
- description - text
- count - positive integer
- subscription_cost - positive integer
- topic - char with max length 20 
- author - array of reference to Author
 

###Subscriber - Custom Model bellow are fields and its type
- user - reference to User table
- address - text
- phone - phone number   

###Subscription - Custom Model bellow are fields and its type
- subscriber - reference to  Subscriber table
- book -  reference to  Book table
- borrowed_date - date( date of creaton)
- amount_paid - positive integer
- days - positive integer
- returned - Boolean


2. Create Django rest API List, Detailed, create, update, and delete view for all the above Models including User model
3. Create following API’s:
	*	List all books of specific author that are available in the library
	*	List all books given a topic (match topic case insensitive way)
	*	List all Subscribers  who didn’t return (returned=False) who’s subscription expired (expiry = borrowed_date  + days)
	*	Add attribute due_amount in Subscription detailed view (due_amount=(Book. subscription_cost* Subscription.days)  - Subscription.amount_paid)
	*	Make sure can add subscription only if there is book in library (books in library = Book.count – subscription of book that are not returned)