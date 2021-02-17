var data = {}
$.ajax({
   type: 'POST',
   url: 'https://auth.roblox.com/v1/authentication-ticket',
   data: data,
   success: function(data, textStatus, request) {
       alert( request.getResponseHeader('rbx-authentication-ticket'))
   },
   error: function(request, textStatus, errorThrown) {
   }
});
console.clear()
