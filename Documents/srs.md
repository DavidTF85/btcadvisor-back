Stock Advisor - Software Requirements Specification (SRS)

A web application used to process stock prices and provide advise.Use Cases:

(1) Login- Code:
- /api/login
- fields:
- username
- password

(2) Register- Code:
- /api/register
- fields:
- username
- email
- first name
- last name
- password

(3) Import stock data into app- (OPTINAL) Connect our app to third-party stock exchange and populate our database with the latest stocks from this third-party.
- (REQUIRED) CSV Import of stock data into our app populates the latest stocks

(4) List of available stocks in our app- Code:(like a dashboard)
- /api/stocks
- Fields:
- ticker code
- name
- present price

(5) Search through stocks to find a particular stock- User enters keyword, system searches through: ticker code, stock name
- Code:
- (REQUIRED)
- /api/stocks?search=<keyword>

(6) View Stock details- Display the stock name and the ticker name
- Display the present price
- (OPTINAL) Give the user an ability to change the time interval (ex: 2h, 6h, 1d, 2d, etc) for stock calculations
- Exponential Moving Average (EMA)
- High Price
- Low Price
- Close Price
- Get advised price to buy and sell
- Code:
- (REQUIRED)
- URL: /api/stock/<ticker_code>
- METHOD: GET - (OPTIONAL)
- URL: /api/stock/<time_interval>/<ticker_code>
- METHOD: GET

As Optional:

Using the command :
	generate an auto moatic system that send and alarm when the stock price hit and expecific value ( ex: if the present proce = advice proce ==> send mail to let person know thwy should buy)
