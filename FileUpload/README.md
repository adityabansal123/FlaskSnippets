# 1. Create a form with file as input.
<form action="upload" method="post" enctype="multipart/form-data">
  <input type="file" name="file'>
  <input type="submit" value="Upload">
</form>

# 2. Specify the location to save files.
UPLOAD_FOLDER = 'uploads/'

# 3. Specify the allowed extention.
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

# 4. Get the file using
file = request.files['file']

# 5. Save the file using.
file.save()
