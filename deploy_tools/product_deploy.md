
# Deploy

# in server install gunicorn 

''''
pip install gunicorn
''''

start gunicorn 
''''
gunicorn app_name.wsgi:application
''''

# collect static 

pythin manage.py collectstatic --noinput

chage nginx conf 

''''
server {
	listen 80;
	server_name: you_domain_name;
	
	location /static {
		alias /home/_you_user_name_/sites/_you_domain_name_/static;
		}

	location / {
		proxy_pass http://localhost:8000;
		}
}
''''

restart nginx 

''''
sudo systemctl reload nginx
gunicorn app_name.wsgi:application
''''

in local server

''''
STANDING_SERVER = your_domain_name python manage.py test functional_tests
''''

