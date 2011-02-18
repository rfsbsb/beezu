function retweet(text) {
  if (text != '') {
    var username = $('#'+text+' .username').text()
    var body = $('#'+text+' .text-body').text()
    var text = 'RT: @'+ username + " "+ jQuery.trim(body)
  }
  $('#text-msg').val(text);
  $("#write").click()

}
  
$(document).ready(function() {

  function send(msg) {
    document.title = "null";
    document.title = msg;
    alert(msg)
  }

  /*
    Tabs functions
  */
  $("#home").click(function(){
    $("#mentions_timeline").fadeOut();
    $("#home_timeline").delay(400).fadeIn();
    $("button#home").addClass("selected")
    $("button#mentions").removeClass("selected");
  });

  $("#mentions").click(function(){
    $("#home_timeline").fadeOut();
    $("#mentions_timeline").delay(400).fadeIn();
    $("#mentions").addClass("selected")
    $("#home").removeClass("selected");
  });

  $("#direct").click(function(){
    alert("direct ok");
  });

  $("#search").click(function(){
    alert("search ok");
  });
  
  $("#write").click(function(){
    $('#message').dialog({
      modal: true,
      draggable: false,
      resizable: false,
      buttons: {
        "Enviar": function() {
          send("titulo");
          $(this).dialog("close");
        }
      }
    });
  });

  /*
    Hotkeys
  */
  $(document).shortkeys({
    'c': function () { $("#write").click(); }
  });

  
  
  /* 
    Baloon Functions
  */

  $('.post').dblclick(function() {
    alert('Clique duplo no balão.');
  });

  $(".post").hover(
    function () {
      $(this).find(".icons").show();
      $(this).find(".timeago").hide();
    }, 
    function () {
      $(this).find(".icons").hide();
      $(this).find(".timeago").show();
    }
  );


  $('.photo').click(function() {
    $('#profile').dialog({
      modal: true,
      draggable: false,
      resizable: false,
      buttons: {
        Ok: function() {
          $( this ).dialog( "close" );
        }
      }
    });
  });

  $('.username').click(function() {
    alert('clique no username.');
  });
  
  $('.timeago').click(function() {
    alert('clique no tempo.');
  });
  
});
