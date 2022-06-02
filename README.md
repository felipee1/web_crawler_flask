# flask_mongodb_dockerized_crawler

## Description
This code is for scrap links from a url using scrappy and Flask + MongoDB with docker.

## Environment

* python 3.8
* flask
* pymongo
* scrapy
* crochet
* docker

### Installing dependencies
This app are running in docker so first of all install docker 

[a Installation Guide](https://docs.docker.com/engine/install/)

after installed container so just run the command

`$ docker-compose up --build`

## Running App
### 
To run the app just run the command 

`$ docker-compose up --build`

and open you localhost at the gate 5000

[ Localhost:5000 ](http://localhost:5000/)

## Code Architecture
This app wasn't created based on a complex especific architecture, just devide the app in scrapy folder, app folder and inside the app folder divide the contents in template to html folder, static/styles to css and test to unit tests.

```
app/
    app/
        ststic/
            styles/
                error.css
                index.css
                list.css
                scraped.css
        template/
            error.html
            index.html
            list.html
            scraped.html
        test/
            test.py
        app.py
    crawler/
        crawler/
            spiders/
                __init__.py
                extractor.py
            __init__.py
            items.py
            middlewares.py
            pipelines.py
            settings.py
        scrapy.cfg
    docker-compose.yml
    Dockerfile
    README.MD
    requirements.txt
```


