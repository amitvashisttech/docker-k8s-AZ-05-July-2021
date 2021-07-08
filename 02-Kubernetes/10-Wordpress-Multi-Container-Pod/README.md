```  
656  vim wordpress-secrets.yml
  657  vim wordpress-service.yml
  658  vim wordpress-deployment.yml
  659  echo  -n "Pass@word1234" | base64
  660  echo  -n "password" | base64
  661  vim wordpress-secrets.yml 
  662  ls
  663  vim wordpress-service.yml 
  664  ls
  665  vim wordpress-deployment.yml 
  666  ls
  667  cd ..
  668  ls
  669  kubectl create -f 10-Wordpress-Multi-Container-Pod/
  670  kubectl get deploy,svc,pod
  671  kubectl get pod
  672  kubectl describe pod
  673  kubectl get deploy,svc,pod
  674  kubectl get pods 
  675  kubectl exec -it wordpress-deployment-7d4896594c-xdfxj -c mysql -- mysql -u root -p 
  676  ls
  677  kubectl delete -f 10-Wordpress-Multi-Container-Pod/
```


```
root@wordpress-deployment-7d4896594c-2rqpx:/var/www/html# diff wp-config-sample.php wp-config.php
23c23
< define('DB_NAME', 'database_name_here');
---
> define('DB_NAME', 'wordpress');
26c26
< define('DB_USER', 'username_here');
---
> define('DB_USER', 'root');
29c29
< define('DB_PASSWORD', 'password_here');
---
> define('DB_PASSWORD', 'password');
32c32
< define('DB_HOST', 'localhost');
---
> define('DB_HOST', '127.0.0.1');
```
