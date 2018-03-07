#### Dropzone JS -> Used for AJAX Image Uploading

## Steps Involved:
### 1. Create form with file as input.
```
<form action="upload" class="dropzone"></form>

```
### 2. Download and include dropzone js and css using the link
[Website](http://www.dropzonejs.com/)
[Github](https://github.com/enyo/dropzone/tree/master/dist)


### 3. Create server script to catch file and save them.
```
@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return ''
    return "ooooooppppppssss"
```

