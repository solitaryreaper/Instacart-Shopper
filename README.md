## Instacart-Shopper
This challenge is broken into two parts. The first part is implementing the public-facing site that a prospective Instacart Shopper would see when hearing about the opportunities that Instacart offers. The second is writing analytics to monitor the progress of shoppers through the hiring funnel.

## Application
The application has been hosted here : http://159.203.92.24:8000/instacart_shopper/

## Technologies
1. Python
2. Django

Used Django because it also provides an admin interface to manage the database data. Django or Ruby on rails are good MVC frameworks to use for such web-centric CRUD applications.

## Web Pages/API's
1. Landing Page : http://159.203.92.24:8000/instacart_shopper/
2. Funnel Report API : http://159.203.92.24:8000/instacart_shopper/funnel.json?start_date=<start_date>&end_date=<end_date>

    This generates funnel report between the last monday <= start_date and next sunday >= end_date.
    
    Example : http://159.203.92.24:8000/instacart_shopper/funnel.json?start_date=2014-01-01&end_date=2014-12-31

3. Data bootstrap API : http://159.203.92.24:8000/instacart_shopper/bootstrap/<count>/
   
    Example : http://159.203.92.24:8000/instacart_shopper/bootstrap/10000/


