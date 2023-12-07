prerequisite: Install helm3 to install Ingress controller. 
You should have access to dockerHub to pull the images given for sample apps in deployment files or you can create docker images from code provided in service1 and service2 directories.
if you are using baremetal then make sure you have entry in /etc/hostname file for Ingress IP to resolve DNS.

STEPS: 

Create deployments,services and Ingress for app1 and app2
go to directory named Kubernetes and  create all the resources in one go using kubectl apply -f . OR use below command
kubectl create -f app1.deployment.yaml; kubectl create -f app2.deployment.yaml; kubectl create -f svc1.yaml; kubectl create -f svc2.yaml; kubectl create -f ingress-svc.yaml; kubectl create -f ingress.yaml; kubectl create -f nginx-deployment.yaml

Above commands with create deployments, svc and ingres controller for app1 and app2
check the output using kubectl get all command. It will show 3 replicas of each service, Ingress and svc.

STEPS FOR TESTING
lets first check direct services output without Ingress/loadbalancer.

1. Execute kubectl get svc, it will show cluster-IP for service1 and service2. Service1 will listen on port 8080 and service2 will listen on port 8081. Note down Cluster-IP of both services.

2. Test response for service1 using curl http://{{cluster-IP-of-service1}}:8080/path1
    e.g. suppose clusterip of service1 is 10.109.164.255 then full command will be 

    curl http://10.109.164.255:8080/path1 

    OUTPUT: This is Service1 Response!

3.  Test response for service2 using curl http://{{cluster-IP-of-service2}}:8081/path2
    e.g. suppose clusterip of service2 is 10.108.33.36 then full command will be 

    curl http://10.108.33.36:8081/path2 

    OUTPUT: This is Service2 Response!   

4. To check self-healing delete the pods, you will see it will be created automatically and ensure always 3 replicas of each service is running. 

5. If above scenarios are working. Now install nginx-ingress using helm. use below commands to install nginx-ingress

   helm repo add ingress-nginx https://kubernetes.github.io/ingress-nginx

   helm repo update
   
   helm install nginx-ingress ingress-nginx/ingress-nginx

   It will create deployment, pods, services, service-account and other resources in nginx-ingress namespace

6. Make entry in /etc/hostname file and check response from abc.com/path1 and abc.com/path2.


