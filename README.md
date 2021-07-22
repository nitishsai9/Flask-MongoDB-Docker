# Flask-MongoDB-Docker

### Built With

* [Bootstrap](https://getbootstrap.com)
* [Docker](https://docs.docker.com/compose/gettingstarted/)
* [Flask](https://flask.palletsprojects.com/en/2.0.x/)
* [MongoDB](https://www.mongodb.com/)

### Installation


1. Build and run

   ```sh
   docker-compose build
   docker-compose up
   
   
   ```
2. Remove or Stop
   ```sh
   docker-compose down
   docker-compose down -v [will remove volumes]
   ```

   ```
3. Access in Browser
   ```sh
   
   http://localhost:80
   ```
   
4.  Test in cli
   ```sh
  curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"title":"xyz","desc":"xyz"}' \
  http://localhost:3000/
   ```
