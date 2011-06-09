$(document).ready(function() {

  function send(msg) {
    document.title = "null";
    document.title = msg;
  }
  
  function hide_show(show){
    $("#river").find('.active').fadeOut();
    $("#"+show+"_timeline").delay(400).fadeIn();
    $("#river").find('.active').removeClass("active");
    $("#"+show+"_timeline").addClass("active")

    $("#sidebar").find('.selected').removeClass("selected");
    $("#"+show).addClass("selected")

  }

  /*
    Tabs functions
  */
  $("#home").click(function(){
    hide_show(this.id)
  });

  $("#mentions").click(function(){
    hide_show(this.id)
  });

  $("#direct").click(function(){
    hide_show(this.id)
  });

  $("#search").click(function(){
    hide_show(this.id)
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
