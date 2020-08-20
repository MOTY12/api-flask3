Steps:
*** python -m venv ./venv;source venv/bin/activate
*** pip3 install -r requirements.txt

How to run it 
1). Source venv/bin/activate
2). Python app/app.py
3). Open postman then request for data using(GET: 127.0.0.1:5000)
 
4). POST, PUT, GET, DELETE the request using the following url to request
 route{
      POST: /blog
      GET: /blogs; blog/<id>
      PUT: /blog/<id>
      DELETE: /blog/<id>
      
 }
