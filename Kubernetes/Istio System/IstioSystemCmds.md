**Uninstall Istio-System**

`cd /istio-***/bin/`
`istioctl x uninstall --purge`
`kubectl delete namespace istio-system`


**Install Istio-System**

`curl -L https://istio.io/downloadIstio | sh -`
`cd /istio-***/bin/`
`istioctl x precheck`
`istioctl install --set profile=default -y` >   To install with default configuration
or
`istioctl install -f <path-to-config-yaml-file>`
`kubectl label namespace <namespace> istio-injection=enabled --overwrite`

https://istio.io/latest/docs/setup/