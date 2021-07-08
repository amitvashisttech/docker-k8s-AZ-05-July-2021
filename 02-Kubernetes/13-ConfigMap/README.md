```
  807  kubectl get configmap
  808  kubectl edit configmap
  809  kubectl get configmap
  810  kubectl describe configmap 
  811  kubectl edit configmap
  812  kubectl edit configmap -o yaml
  813  ls
  814  cd 02-K8s/
  815  ls
  816  cd 13-ConfigMap/
  817  ls
  818  vim reverseproxy.conf 
  819  ls
  820  kubectl create configmap --help
  821  kubectl get configmap
  822  kubectl create configmap nginx-config --from-file=reverseproxy.co nf --dry-run -o yaml 
  823  kubectl create configmap nginx-config --from-file=reverseproxy.conf --dry-run -o yaml 
  824  kubectl create configmap nginx-config --from-file=reverseproxy.conf --dry-run -o yaml  > nginx-config-configMap.yaml
  825  ls
  826  kubectl apply -f nginx-config-configMap.yaml
  827  kubectl get configmap
  828  kubectl describe configmap
  829  ls
  830  history > README.md
```
