
```yml
version: '3'
services:
  web:
    image: hcoco1/dashcoco1-flask:latest
    ports:
      - "5000:5000"
    environment:
      FLASK_ENV: development
      ```

docker pull hcoco1/dashcoco1-flask:latest

docker-compose up

docker-compose down


