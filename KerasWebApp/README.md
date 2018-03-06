## Usage
* Clone this repo
* Install requirements
* Run the script
* Check http://localhost:5000

## Customization

### Use your own model
Place your trained **.h5** file saved by model.save() under models directory. Check the **commented code** in app.py.
The file uses other pre-trained model

### Frontend
Modify files in **templates** and **static** directory.

## Deployment
To deploy it for public use, we need to have a public *linux server*.

### Run the app
Run the script and hide it in background.
```
$ python app.py
```
gunicorn can be used instead of gevent
```
$ gunicorn -b 127.0.0.1:5000 app:app
```

### Set up Nginx
TO redirect traffic to local app, configure Nginx *.conf* file.
```
server{
    listen 80;

    client_max_bosy_size 20M;

    location / {
        proxy_pass http://127.0.0.1:5000;
    }
}
```
