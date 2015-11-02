## Instacart-Shopper
This challenge is broken into two parts. The first part is implementing the public-facing site that a prospective Instacart Shopper would see when hearing about the opportunities that Instacart offers. The second is writing analytics to monitor the progress of shoppers through the hiring funnel.

## Application
The application has been hosted here : http://159.203.92.24:8000/instacart_shopper/

## Technologies
1. Python
2. Django

Used Django because it also provides an admin interface to manage the database data. Django or Ruby on rails are good MVC frameworks to use for such web-centric CRUD applications.

This web application is running against the default SQLITE database. But it can be configured to use any database in the backend because of Django's database abstraction layer.

This web application is also running use the default development server provided by Django. But it can be configured to use NGINX or other web servers to handle production workloads.

## Web Pages/API's
1. Landing Page : http://159.203.92.24:8000/instacart_shopper/
   * Returns proper validation messages if the input is invalid. For example, malformed email id or phone number.
   * Returns proper validation messages if the email or phone number is already present in the shopper database.
   * Uses Django session support to manage email based sessions for currently logged user.
   * Uses Django message support to communicate appropriate validation messages.

2. Funnel Report API : http://159.203.92.24:8000/instacart_shopper/funnel.json?start_date=START&end_date=END
    * This generates funnel report between the last monday <= start_date and next sunday >= end_date. The results are sorted by 
    chronological buckets to help easily visualize the correct date buckets.
    * Returns proper API error messages if the input is incorrect. For example, if date is incorrectly formatted or START date        is greater than END date. 
    * Example : http://159.203.92.24:8000/instacart_shopper/funnel.json?start_date=2014-01-01&end_date=2014-12-31

3. Data bootstrap API : http://159.203.92.24:8000/instacart_shopper/bootstrap/COUNT/
     * This API populates the database with COUNT random dummy shopper applicants.
    * Example : http://159.203.92.24:8000/instacart_shopper/bootstrap/10000/


