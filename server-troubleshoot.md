### Check the status of server (using curl)
```commandline
curl -I http://example.com
```

### Nginx
If nginx is running but showing _internal error (error 50x)_, 
the first thing to do is to check the error messages.
```commandline
less /var/log/nginx/error.log
```
If the error is permission denied:  
- make sure user nginx already has access to the file
- if it already has access, then maybe it has something to do with
SELinux. If so, then [here is the reference](https://www.nginx.com/blog/using-nginx-plus-with-selinux/)

### Gunicorn  
If we just migrated the server sometimes the sock file generated
from gunicorn is missing. To solve it, we can generate it again
by running gunicorn:
```commandline
sudo systemctl start gunicorn
```