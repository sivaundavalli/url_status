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
      
      
