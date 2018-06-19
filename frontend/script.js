function get_articles() {
	
$.ajax({ url: "http://127.0.0.1:8000/article/",
        context: document.body,
        crossDomain: true,
        "method": "GET",
        success: function(data){
 			var inHTML = "<tr><th>Title</th><th>Content</th><th>Author</th><th>votes</th></tr>";
 			$.each(data, function(index, value){
    		var newItem = "<tr><td>"+ value.title + "</td><td>"+ value.content + "</td><td>"+ value.author + "</td><td>"+value.vote+"</td>"+"<td><button id = "+value.id+" onClick = upvote("+value.id+","+value.vote+")>Upvote</button></td>"+"</tr>"
    		inHTML += newItem;

			});
			// inHTML+="</ul>";
			$("#d").html(inHTML);

        }
    });

	}

function upvote(id,vote){
			id_str = id.toString()
			vote_str = (vote+1).toString()
$.ajax({ url: "http://127.0.0.1:8000/article/",
        context: document.body,
        crossDomain: true,
        "method": "PATCH",

		"data": {
		    "id": id_str,
		    "vote": vote_str
		  } ,
		         success: function(data){
		         	console.log(data)
 			get_articles();
        }
    });

}

$( "#articlecreate" ).submit(function( event ) {
	  event.preventDefault();
	
	var frm = $('#articlecreate');
	// console.log($('#articlecreate').data,">>>>>>>>>>")
$.ajax({ url: "http://127.0.0.1:8000/article/",
        context: document.body,
        crossDomain: true,
        data : frm.serialize(),
        "method": "POST",
		         success: function(data){
 			$(location).attr("href","/");

        },
        error:function(data){
        	console.log(data)
        }
    });
  

});


$(document).ready(function(){
	get_articles()
});

