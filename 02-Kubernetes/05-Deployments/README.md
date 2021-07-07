  ```
  132  cd 02-Kubernetes/
  133  ls
  134  mkdir 05-Deployments
  135  ls
  136  cd 05-Deployments/
  137  vim helloworld.yaml
  138  ls
  139  kubectl get pods 
  140  kubectl create -f helloworld.yaml 
  141  kubectl get deploy
  142  kubectl get rs
  143  kubectl get pods
  144  kubectl scale --replicas=10 dc helloworld-deployment
  145  kubectl scale --replicas=10 deployment helloworld-deployment
  146  kubectl get pods
  147  kubectl scale --replicas=1 deployment helloworld-deployment
  148  kubectl get pods
  149  ls
  150  kubectl get deploy
  151  kubectl describe deploy helloworld-deployment
  152  kubectl get deploy
  153  kubectl scale --replicas=10 deployment helloworld-deployment
  154  kubectl get deploy
  155  kubectl get pods 
  156  kubectl describe deploy helloworld-deployment
  157  kubectl set image deployment helloworld-deployment k8s-demo=amitvashist7/k8s-tiny-web:2
  158  kubectl get pods 
  159  kubectl get pods -w
  160  watch -n .5 kubectl get pods 
  161  kubectl get pods 
  162  kubectl get deploy
  163  kubectl get rc
  164  kubectl get rs
  165  kubectl describe deploy helloworld-deployment
  166  kubectl get rs
  167  kubectl describe rs helloworld-deployment-558759896c
  168  kubectl get rs
  169  kubectl describe rs helloworld-deployment-78cf6987f9
  170  kubectl rollout status deploy helloworld-deployment
  171  kubectl set image deployment helloworld-deployment k8s-demo=amitvashist7/k8s-tiny-web:3
  172  kubectl rollout status deploy helloworld-deployment
  173  kubectl get rs
  174  watch -n .5 kubectl get pods 
  175  kubectl set image deployment helloworld-deployment k8s-demo=amitvashist7/k8s-tiny-web:4
  176  watch -n .5 kubectl get pods 
  177  kubectl get rs
  178  kubectl rollout undo deploy helloworld-deployment
  179  kubectl get rs
  180  watch -n .5 kubectl get pods 
  181  kubectl get rs
  182  kubectl rollout history deploy helloworld-deployment
  183  kubectl rollout history deploy helloworld-deployment --resvision=1
  184  kubectl rollout history deploy helloworld-deployment --revision=1
  185  kubectl rollout history deploy helloworld-deployment --revision=2
  186  kubectl rollout history deploy helloworld-deployment --revision=3
  187  kubectl rollout history deploy helloworld-deployment --revision=4
  188  kubectl rollout history deploy helloworld-deployment --revision=5
  189  kubectl get pods 
  190  kubectl  get rs 
  191  kubectl rollout history deploy helloworld-deployment
  192  kubectl set image deployment helloworld-deployment k8s-demo=amitvashist7/k8s-tiny-web --record
  193  kubectl get pods 
  194  kubectl get rs
  195  kubectl rollout history deploy helloworld-deployment
  196  kubectl set image deployment helloworld-deployment k8s-demo=amitvashist7/k8s-tiny-web:2 --record
  197  kubectl rollout history deploy helloworld-deployment
  198  kubectl rollout undo deploy helloworld-deployment
  199  kubectl rollout history deploy helloworld-deployment
  200  kubectl rollout undo deploy helloworld-deployment
  201  kubectl rollout history deploy helloworld-deployment
  202  kubectl rollout undo deploy helloworld-deployment --to-revision=4 --record
  203  kubectl rollout undo deploy helloworld-deployment --to-revision=4 
  204  kubectl rollout history deploy helloworld-deployment
  205  kubectl rollout undo deploy helloworld-deployment --to-revision=5
  206  kubectl rollout history deploy helloworld-deployment
  207  ls
  208  history > README.md
```
