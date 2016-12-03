EXPOSED_GO_PORT=8002
docker rm -f my-running-go-app
docker build -t my-go-app .
docker run -dit --publish $EXPOSED_GO_PORT:8080 --name my-running-go-app my-go-app
echo " ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
echo "|     BUILD COMPLETE... STARTING GO               |" 
echo "|           Apache Port: $EXPOSED_GO_PORT                     |"
echo " ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
