# Price-Comparison-Website

This project is a price comparison website where users can add products from various stores into a basket. The total cost for the items in the basket is calculated for each store. This helps user pick which store is cheapest to shop at based on the chosen items.

# Operation

## How to run the code and use the website
1.	Before starting the user should have visual studio installed.
2.	In Visual studio console, the user should type Pip install Django.
3.	After installing Django, the user should type Pip install pillow.
4.	Once the project code is downloaded along with Django and pillow modules and opened in Visual Studio Code the following command should be typed by the user into the Code Terminal “python manage.py runserver”, this command should provide a website link “http://127.0.0.1:8000/” which can be opened in the browser by entering it into the URL. 
5. If successful, the website will start on the home page. The usability of the website without creating an account is very limited, so the next step involves creating an account. On the navigation bar “log in” should be clicked, once on the login page under the big “Log In” button there’s a text saying “New? Sign in” this should be clicked to enter the registration page. A username and the password, and the password confirmation should be entered, if the user already exists or the password is wrong an error will show up and the fields will have to be filled out again. 
6.	If registering was successful the user should be redirected to the login page, the login fields should be filled out with the previously created username and the password.
7.	If the login was successful, the user should be redirected to the home page and their name should appear on the navigation bar “log out [user]” this indicates that the user is logged in. To log out simply click the “log out [user]” in the navigation bar.
8.	The home page shows 4 stores, the user should click on the stores they want to see on the contents page, and the selected stores should change colour and show a tick, once the stores are selected the user should click apply button underneath.  
9.	Now the user should find themselves on the contents page, this is where all of the items are displayed, the user should simply choose which items they like and click “Add To Basket” for each of them, if the user wants to add more than one of the item the user should click the “+” button to increase the quantity by one, similarly if the user wants to remove the item they should click the “-“ button if the quantity reaches 0 the “Add To Basket” button should appear again. 
10.	If the user wants to find a specific item its name,  store or category can be entered into the search bar at the top of the contents page underneath the navigation bar.
11.	If the user wants to filter the products, the blue hamburger menu in the top left corner should be clicked. Once clicked the side navigation bar will show up where the user can select which stores they want, the price range and even a specific item. The user should click the apply button once the filter fields are filled. 
12.	To see the items that are added the user should click on the basket icon in the navigation bar. The user should get redirected to a basket page, where all of the added items can be seen, and the quantity of the items can be increased or decreased, the user has two other options Continue shopping or find the cheapest price. “Continue shopping” button will take the user back to the contents page, whilst the “Find cheapest price” button will take the user to the price comparing page. 
13.	On the cheapest price page, the user can see the recommended items from the basket for each store and the overall price for it. This gives the user all of the information that they need to decide on where they would like to shop.  
