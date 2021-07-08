```
  721  cd 12-Service-Discovery/
  722  ls
  723  cat secrets.yml 
  724  ls
  725  cat database.yaml 
  726  ls
  727  cat database-service.yml 
  728  kubectl apply -f secrets.yml 
  729  kubectl apply -f database.yaml 
  730  kubectl apply -f database-service.yml 
  731  kubectl get pods,secrets,svc
  732  cat database-service.yml 
  733  ls
  734  vim helloworld-db-app.yml 
  735  ls
  736  kubectl apply -f helloworld-db-app.yml 
  737  kubectl get pods 
  738  kubectl apply -f helloworld-app-service.yml 
  739  kubectl get pods,svc
  740  kubectl get pods 
  741  kubectl exec -it database -- mysql -u root -p 
  742  kubectl get svc 
  743  kubectl get pods 
  744  kubectl run -it busybox --image=busybox:1.28 --restart=Never -- sh 
  745  ls
  746  history 
  747  history > README.md
```
