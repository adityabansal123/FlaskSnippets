#HTML CODE
<input type="text" name="country" id="autocomplete" class="form-control" placeholder="Enter Country Name" />
Jquery Plugin to achieve Autocomplete from DevBridge
<script type="text/javascript" src="src/jquery.autocomplete.js"></script>

#JQuery Code
$("autocomplete").autocomplete({
        //lookup: countries,
        serviceUrl: 'autocomplete',   //tell the script where to send requests
        type:'POST',
        width:450,     //set width
        //callback just to show its working
        onSelect: function(suggestion){
          $('#selection').html('You selected: ' + suggestion.value + ', ' + suggestion.data);
        },
        showNoSuggestionNotice: true,
        noSuggestionNotice: 'Sorry, no matching results',
});

#Flask Script
@app.route('/ajaxautocomplete', methods=[POST,GET])
def ajaxautocomplete():
  result = ''
  if request.method == 'POST':
    query = request.form['query']
    try:
      with connection.cursor() as cursor:
        sql="select country_code data,country_name value from  countries where country_name like '%"+query+"%'"
        cursor.execute(sql)
        result = cursor.fetchall()
    finally:
      a=2
    return json.dumps({"suggestions":result})
  else:
    return "oops"
