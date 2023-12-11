Prerequisites 

1. You should have access to dockerHub to pull the images given for sample apps in deployment files or you can create docker images from code provided in service1 and service2 directories.
 2. Make sure you have an entry for abc.com against your Kubernetes node IP in /etc/hosts so that abc.com should resolve to node IP.
 e.g node-IP    nodename    abc.com

If you are using minikube then enable ingress addons using below command
minikube addons enable ingress

DEPLOYMENT STEPS: 
1. Go to Kubernetes directory

2. First deploy ingress controller using nginx-deployment.yaml because it will create ingress-nginx namespace and other resources. use below command 
kubectl create -f nginx-deployment.yaml
It will create ingress-nginx-controller pod and other resources in namespace named ingress-nginx

3. Create deployments,services and Ingress for app1 and app2 using below command
kubectl create -f app1.deployment.yaml; kubectl create -f app2.deployment.yaml; kubectl create -f svc1.yaml; kubectl create -f svc2.yaml; kubectl create -f ingress.yaml

Above commands will create deployments, svc for app1 and app2 and ingress in namespace named ingress-nginx.
check the output using kubectl get all -n ingress-nginx command. It will show 3 replicas for each apps named service1 and service2 are up a, svc and Ingress.

4. Make an entry for abc.com against your Kubernetes node IP in /etc/hosts so that abc.com should resolve to node IP.
 e.g node-IP    nodename    abc.com

TESTING PREREQUISITES 

1. Make sure both apps app1, app2 and ingress-nginx-controller pods are running.

2. Make sure you have an entry for abc.com against your Kubernetes node IP in /etc/hosts so that abc.com should resolve to node IP.
 e.g node-IP    nodename    abc.com
  
3. Note down ingress-nginx-controller NodePort number by executing below command
   kubectl get svc ingress-nginx-controller -n ingress-nginx  (This number should be between 30000 to 32767)

TESTING STEPS:

1. Execute below curl command to check app1 response. In below examples I am assuming        NodePort number is 30824
    curl http://abc.com:30824/path1 

  OUTPUT: Hello, This is Service1 Response!

  NOTE : change NodePort number with your NodePort  ( Noted in TESTING PREREQUISITES step3  )

2. Execute below curl command to check app2 response.
    curl http://abc.com:30824/path2

  OUTPUT: Hello, This is Service2 Response!    


4. To check self-healing delete the pods, you will see it will be created automatically and ensure always 3 replicas of each service is running. 





