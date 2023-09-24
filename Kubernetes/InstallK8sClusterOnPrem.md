Using KinD
----------

Have Docker install and ready

sudo apt update
sudo apt upgrade -y
curl -Lo ./kind https://github.com/kubernetes-sigs/kind/releases/download/v0.20.0/kind-linux-amd64
chmod +x ./kind
sudo mv ./kind /usr/local/bin/
kind create cluster --name <clusterName>        --->        To create single node cluster

kind delete cluster --name <clusterName>

Create the YAML file with below details:

kind: Cluster
apiVersion: kind.x-k8s.io/v1alpha4
nodes:
  - role: control-plane
  - role: worker
  - role: worker

kind create cluster --name <clusterName> --config ./<YAML file>         --->        To create 3 nodes cluster