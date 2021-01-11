# ocr-test
pancard OCR text detection

### To run the project locally 
Pre-requisite docker docker-compose

```
docker-compose build
docker-compose up
```
Can add you .env file or else the django secret key will be set to default in setting.py.

> visit http://localhost:8000/pancard/ to upload a pancard

command to push to heroku
```
docker build -t registry.heroku.com/thawing-beach-69423/web .
docker push registry.heroku.com/thawing-beach-69423/web
heroku container:release -a thawing-beach-69423 web
```
