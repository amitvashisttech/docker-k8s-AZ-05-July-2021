```

  586  mkdir 09-Secrets
  588  cd 09-Secrets/
  589  ls
  590  echo  -n "AmitVashist" | base64
  591  echo  -n "Pass@wordls" | base64
  592  echo  -n "Pass@word1234" | base64
  593  kubectl create secret --help
  594  kubectl create secret generic mytest  --help        
  595  kubectl create secret generic my-secret --from-literal=key1=supersecret --from-literal=key2=topsecret
  596  kubectl get secrets 
  597  kubectl describe secrets my-secret
  598  kubectl edit secrets my-secret
  599  ls
  600  kubectl create secret generic my-secret2 --from-literal=key1=supersecret --from-literal=key2=topsecret --dry-run
  601  kubectl get secrets 
  602  kubectl create secret generic my-secret2 --from-literal=key1=supersecret --from-literal=key2=topsecret --dry-run -o yaml
  603  kubectl create secret generic my-secret2 --from-literal=key1=supersecret --from-literal=key2=topsecret --dry-run -o yaml > my-secret2.yaml
  604  ls
  605  cat my-secret2.yaml 
  606  cp -rf my-secret2.yaml my-prod-secret.yaml 
  607  ls
  608  vim my-prod-secret.yaml 
  609  ls
  610  kubectl create -f my-prod-secret.yaml 
  611  kubectl get secrets 
  612  kubectl describe secrets  my-prod-key
  613  kubectl edit secrets  my-prod-key
  614  vim helloworld-secret-volume.yaml
  615  ls
  616  kubectl create -f helloworld-secret-volume.yaml 
  617  kubectl get pods 
  618  kubectl describe pod helloworld-deployment-79bdf544bd-4gh66
  619  kubectl get pods 
  620  kubectl exec -it helloworld-deployment-79bdf544bd-4gh66 -- /bin/sh
  621  ls
  622  kubectl get pods 
  623  kubectl get pods -o wide 
  624  kubectl exec -it helloworld-deployment-79bdf544bd-bwwl6 -- /bin/sh
  625  ls
  626  history | grep -i secrets 
  627  history | grep -i secrets  > README.md
  628  ls
  629  cd ..
  630  ls
  631  cd ..
  632  ls
  633  git add . ; git commit -m "09-Secrets"; git push 
  634  history 
  635  history | grep -i base
  636  history | grep -i base >> 02-Kubernetes/09-Secrets/README.md 
  637  vim 02-Kubernetes/09-Secrets/README.md 
  638  ls
  639  history >  02-Kubernetes/09-Secrets/README.md 
```
