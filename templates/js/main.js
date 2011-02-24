$(document).ready(function() {

  function send(msg) {
    document.title = "null";
    document.title = msg;
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
          send($('#text-msg').val());
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
  
  //toggle favicon
  $(".fav-icon").click(function(){
    src = $(this).attr('src');
    if (src == 'img/fav.png'){
      $(this).attr('src','img/unfav.png')
    } else {
      $(this).attr('src','img/fav.png')
    }
  });

  //toggle retweet icon
  $(".retweet-icon").click(function(){
    src = $(this).attr('src');
    if (src == 'img/retweet.png'){
      $(this).attr('src','img/retweeted.png')
    } else {
      $(this).attr('src','img/retweet.png')
    }
  });
  
  //fill in the message box with RT text
  $(".rt-icon").click(function(){
    text = ''
    id = $(this).parents("div.post").attr('id');
    if (id != '') {
      var username = $('#'+id+' .username').text()
      var body = $('#'+id+' .text-body').text()
      var text = 'RT: @'+ username + " "+ jQuery.trim(body)
    }
    $('#text-msg').val(text);
    $("#write").click()
  })
  
  

  $('.username').click(function() {
    alert('clique no username.');
  });
  
  $('.timeago').click(function() {
    alert('clique no tempo.');
  });
  
});
