  ```

  374  git pull 
  375  ls
  376  cd 02-K8s/
  377  ls
  378  cd 07-HealthCheck/
  379  ls
  380  ll
  381  cat helloworld-deploy-custom.yaml
  382  ls
  383  ll
  384  vim helloworld-deploy-hc.yaml 
  385  kubectl apply -f helloworld-deploy-hc.yaml 
  386  kubectl get deploy 
  387  kubectl get pods 
  388  kubectl describe pod helloworld-deployment-585fb455cb-2bj8k
  389  kubectl describe pod mypythonwebapp
  390  kubectl get pods 
  391  kubectl get deploy
  392  kubectl expose deploy helloworld-deployment --type=NodePort
  393* kubectl 
  394  kubectl edit deploy helloworld-deployment
  395  kubectl get pods 
  396  kubectl describe pod helloworld-deployment-85f99c955-gtbnv
  397  kubectl edit deploy helloworld-deployment
  398  ls
  399  vim helloworld-deploy-custom.yaml 
  400  kubectl describe pod helloworld-deployment-85f99c955-gtbnv
  401  kubectl describe pod helloworld-deployment
  402  kubectl delete -f helloworld-deploy-hc.yaml 
  403  kubectl apply -f helloworld-deploy-custom.yaml 
  404  cat helloworld-deploy-custom.yaml 
  405  kubectl describe pod helloworld-deployment
  406  ls
  407  vim helloworld-deploy-readiness-healthcheck.yaml 
  408  ls
  409  kubectl get pods 
  410  kubectl delete -f helloworld-deploy-custom.yaml 
  411  kubectl apply -f helloworld-deploy-custom.yaml 
  412  kubectl delete -f helloworld-deploy-custom.yaml 
  413  kubectl apply -f helloworld-deploy-custom.yaml 
  414  kubectl delete -f helloworld-deploy-custom.yaml 
  415  kubectl apply -f helloworld-deploy-readiness-healthcheck.yaml 
  416  kubectl delete -f helloworld-deploy-custom.yaml 
  417  vim helloworld-deploy-custom.yaml 
  418  vim helloworld-deploy-readiness-healthcheck.yaml 
  419  kubectl apply -f helloworld-deploy-readiness-healthcheck.yaml 
  420  kubectl delete -f helloworld-deploy-readiness-healthcheck.yaml 
  421  ls
  422  vim pod-prob-exec.yaml 
  423  ls
  424  kubectl apply -f pod-prob-exec.yaml 
  425  kubectl describe pod liveness-exec
  426  kubectl exec -it liveness-exec -- cat /tmp/healthy
  427  kubectl exec -it liveness-exec -- sh 
  428  kubectl get pods 
  429  kubectl describe pod liveness-exec
  430  ls
  431  kubectl delete -f pod-prob-exec.yaml 
```
