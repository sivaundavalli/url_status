import requests


def responses():
    urls = ['https://httpstat.us/200', 'https://httpstat.us/503']

    for i in urls:
     try:
            r = requests.get(i,timeout=0.5)
            r.raise_for_status()
            resp_time = (r.elapsed.total_seconds() * 1000)
            print(resp_time)
            print("sample_external_url_up{{url=\"{urls} \"}}""  = 1".format(urls=i))
            print("sample_external_url_response_ms{{url=\"{} \"}}""  {}".format(i,resp_time))
     except requests.exceptions.HTTPError as err01:
        # print("HTTP error: ", err01)
        # print("response time ", (round(r.elapsed.total_seconds(),3) * 1000))
        print("sample_external_url_up{{url=\"{urls}\"}}""  = 0".format(urls=i))
        print("sample_external_url_response_ms{{url=\"{} \"}}""  {}".format(i, (round(r.elapsed.total_seconds(),3) * 1000)))

responses()
