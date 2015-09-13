$(document).ready(function(){

	console.log("loaded");
	var itemList=[];
	$(".remove").hide();
	$(".select").click(function(){
		var pk=this.id;
		console.log(pk);
		itemList.push(pk);
		console.log(itemList);
		$(this).hide();
		var npk="#-"+pk;
		$.ajax({
            type: "POST",
            url: "/",
            data: {"itemId": pk},
            success: function(data) {
                console.log(data.pk);
                $(npk).fadeIn();		
            }
			});

	});


	$(".remove").click(function(){
		var pk=this.id;
		console.log(pk);
		itemList.push(pk);
		//console.log(itemList);
		$(this).hide();

		var id=pk.slice(1);
		console.log(id);
		var npk="#"+id;
		$(npk).fadeIn();
		$.ajax({
            type: "POST",
            url: "/delete/",
            data: {"itemId": id},
            success: function(data) {
                console.log(data.pk);
                console.log("deleted");
          
            }
			});

	});

	$(".uncurate").click(function(){
		var id=this.id;
		$.ajax({
            type: "POST",
            url: "/delete/",
            data: {"itemId": id},
            success: function(data) {
                console.log(data.pk);
                console.log("deleted");
          
            }
			});
	})

	// CSRF code
    function getCookie(name) {
        var cookieValue = null;
        var i = 0;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (i; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    $.ajaxSetup({
        crossDomain: false, // obviates need for sameOrigin test
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type)) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });




});