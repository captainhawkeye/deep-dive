kubectl create ns argocd

kubectl apply -f https://raw.githubusercontent.com/argoproj/argo-cd/v2.4.7/manifests/install.yaml -n argocd

kubectl patch svc argocd-server -n argocd -p '{"spec": {"type": "LoadBalancer"}}'

sudo apt install jq -y

export ARGOCD_SERVER=`kubectl get svc argocd-server -n argocd -o json | jq --raw-output '.status.loadBalancer.ingress[0].hostname'`

echo $ARGOCD_SERVER

export ARGO_PWD=`kubectl get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d`

echo $ARGO_PWD

