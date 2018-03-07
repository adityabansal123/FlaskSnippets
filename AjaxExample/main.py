# Create a Simple Calculator Application.
# Three input fields, Two number fields,One select box to point addition or subtraction etc.

# Add the ajax script to interact with the server(flask framework).It is an button click event.

<script type="text/javascript">
$(document).ready(function(){
  //sbtn is id of submit button
  $('#sbtn').click(function(event){
    /*Act on the event*/
    $.ajax({
      url: 'ajaxcalc', //server url
      type: 'POST', //passing data as post method
      dataType: 'json', //returning data as json
      data: {input1:$('#in1').val(),input1:$('#in1').val(),operator:$('#operator').val()}, ///form values
      success:function(json)
      {
        alert(json.result); //response from server given as alert message
      }
    });
  });
});
</script>

# create a flask script to catch all the input field values.
@app.route('/ajaxcalc', methods=['POST', 'GET'])
def ajaxcalc():
  if request.method == 'POST':
    input1 = int(request.form['input1'])
    input2 = int(request.form['input2'])
    operation = int(request.form['operator'])
    result = 0
    
    if operation==1:
      result = input1 + input2
    else if operation==2:
      result = input1 - input2
    else if operation==3:
      result = input1 * input2
    else if operation==4:
      result = input1 / input2
    json.dumps({"result":result})
  else:
    return "Error"
