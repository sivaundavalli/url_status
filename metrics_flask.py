from flask import Flask
import requests

app = Flask(__name__)

@app.route("/")

def route():
    return "please go to /metrics to see the metrics"

global result
@app.route("/metrics")


def calculate_metrics():
  urls = ['https://httpstat.us/200', 'https://httpstat.us/503']
  for i in urls:
      r = requests.get(i,timeout=0.09)
      status_code = r.status_code
      resp_time = (round(r.elapsed.total_seconds(), 3) * 1000)
      if status_code == 200:
       result1 = "<h2> sample_external_url_up{{url=\"{urls} \"}}""  =  1 <br> sample_external_url_response_ms{{url={urls}}}"  "= [{resp}]</h2>".format(urls=i,resp=resp_time)
      else:
       result2 =("<h2> sample_external_url_up{{url = {urls}}}"  "= 0 <br>  sample_external_url_response_ms{{url={urls}}}"  "= [{resp}]</h2>".format(urls=i, resp=resp_time))
  return  (result1+result2)

if __name__ == '__main__':
    app.run(debug=True)
