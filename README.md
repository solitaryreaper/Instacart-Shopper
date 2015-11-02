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

## Web Pages/API's/DB
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
 
4. Django Admin API : http://159.203.92.24:8000/admin/instacart_shopper/applicant/
    * Username : admin, Password : admin
    * 
5.  DB Schema : https://github.com/solitaryreaper/Instacart-Shopper/tree/master/shopper/instacart_shopper/migrations
    * Auto-generated using Django database migrations.

## Scalability
The following ideas can help in scaling the analytics component for faster response time, even when the data size explodes.
  1. **Caching**
    Since the funnel API is an expensive grouping API, we can cache the results of this API for faster response times. Django 
    has support for many caching mechanisms like Memcached etc. for the same. Depending on the staleness requirements of the 
    API, we can tune the cache eviction policy.

  2. **Date-based Indexing and database partitioning**
    We also want to optimize the time taken for running the date-range queries. This can be done by creating index on the date 
    column. Also, date-based paritioning of the database might help speed up the query , depending on the nature of executed        queries.

## Screenshots
Screenshots for the various web application states and API's have been hosted here : https://github.com/solitaryreaper/Instacart-Shopper/tree/master/screenshots

## Testing
This application has been tested with Python 2.7.5 and Django 1.8.5

## TODO
1. Add support for configuration for different environments.
2. Better UI design experience.
3. Add test cases.
