#startApache.sh
EXPOSED_APACHE_PORT=8001
docker rm -f my-running-apache
docker build -t my-php-app .
docker run -dit --publish $EXPOSED_APACHE_PORT:80 --name my-running-apache my-php-app
echo " ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
echo "|     BUILD COMPLETE... STARTING APACHE           |" 
echo "|           Apache Port: $EXPOSED_APACHE_PORT                     |" 
echo " ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
