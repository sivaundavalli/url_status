The Current project contains multiple file that are responsible for querying and recording the response codes
This consists of multiple files. Here is the explanation of the files


1. metrics.py

      Link: https://github.com/sivaundavalli/url_status/blob/main/metrics.py

      This is the raw script that prints the contents to IDE console
      
      to run this script we need to have request module to be installed
      
      Output:
      
      The output of this script will look something like below
      
      sample_external_url_up{url="https://httpstat.us/200 "}  = 1
      
      sample_external_url_response_ms{url="https://httpstat.us/200 "}  432.879
      
      sample_external_url_up{url="https://httpstat.us/503"}  = 0
      
      sample_external_url_response_ms{url="https://httpstat.us/503 "}  451.0
      
2. metrics_flask.py

      Link: https://github.com/sivaundavalli/url_status/blob/main/metrics_flask.py
      
      The concept of uploading the metrics to a specfic endpoint has been implemented via the flask framework. it will spin up a webserver and expose the mentioned endpoint to see the return value if the function in flask
      
      Output:
       Serving Flask app "metrics_flask" (lazy loading)
     * Environment: production
       WARNING: This is a development server. Do not use it in a production deployment.
       Use a production WSGI server instead.
     * Debug mode: on
     * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
     * Restarting with stat
     * Debugger is active!
     * Debugger PIN: 200-928-016
     
     the output will be server on localhost:5000/metrics.
     you will be asked to redirected to /metrics if you browse localhost:5000
     
     The output contains the promentheus format for the URL up/down status and the response time
     
     PS: To Avoid the time out issue i have given the timeout as 1 second
     
3. Dockerfile

      Link: https://github.com/sivaundavalli/url_status/blob/main/Dockerfile
      
      This is the Docker file to build the image from the existing script. this will take the contents of      requirements.txt(https://github.com/sivaundavalli/url_status/blob/main/requirements.txt) and install those as a dependancy. the requirements are to install flask and requests module
      once the docker build is completed i had pushed that to docker hub and made it publicaly available and below command can be used to pull and run the docker image
      
      Docker Image command: docker run sivvaundavalli/metrics &
      
      Here is the sample output upon pulling and running the image
      
      $ docker ps 
   docker ps
   CONTAINER ID        IMAGE                             COMMAND                  CREATED              STATUS              PORTS               NAMES
   2bd9d2e44960        sivvaundavalli/metrics:version3   "python metrics_flas…"   About a minute ago   Up About a minute                       blissful_leavitt

    we can check the output from the container by logging into the conatainer and curling to the endpoint

    Command to login : docker exec -it <container_ID> /bin/bash
    
    Sample output from the curl inside the container
    
    curl -sb -H "Accept: application/json" "http://localhost:5000/metrics"
    127.0.0.1 - - [14/Oct/2020 16:14:57] "GET /metrics HTTP/1.1" 200 -
                                                                  <h2> sample_external_url_up{url="https://httpstat.us/200 "}  =  1 <br>     sample_external_url_response_ms{url=https://httpstat.us/200}= [135.0]</h2><h2> sample_external_url_up{url="https://httpstat.us/503 "}  =  0 <br> sample_external_url_response_ms{url=https://httpstat.us/503}= [157.0]</h2>
                                                                  
4.metrics_K8s.yaml

    Link: https://github.com/sivaundavalli/url_status/blob/main/metrics_K8s.yaml
  
    This is a Kubernetes deployment specfication file. once we run the abov file using the command kubectl create -f metrics_K8s.yaml or kubectl apply -f metrics_K8s.yaml
  
    Here is the sample output after successfull kubernetes spinning up the deployment and the pod
    
    kubectl get pods,deploy
    NAME                       READY   STATUS    RESTARTS   AGE
    pod/url-557b9df578-mfftw   1/1     Running   0          6s

    NAME                  READY   UP-TO-DATE   AVAILABLE   AGE
    deployment.apps/url   1/1     1            1           7s
    
    kubectl describe deploy url | grep -i image
    Image:        sivvaundavalli/metrics:version3

    PS: i have tested this on minikube 1.14.0, kubernetes 1.19 and docker 19.03.8
    
    

    





      
      
      
      
