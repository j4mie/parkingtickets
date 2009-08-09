

$(document).ready(function()
{


	/**
	 * Function called when a form is submitted
	 */
	window.heartCount = 7; 	
	
	
	var heartClick = function(img)
	{
	
		var votecount = $(img).attr("id");
		votecount = votecount.charAt(votecount.length-1);
		if(votecount>0) votecount = votecount/(window.heartCount-1);
		form = $("#loveform");
				
		// Get correct site for images and text
		var message = 'Love sent!';

		

		// Get the value of the "action" attribute from the form.
		// This is the url we need to POST to.
		var url = form.attr('action');
		
		// Make the ajax call
		$.ajax(
		{
			'type': 'POST',
			'url': url,
			'data' : {'vote':votecount}, 
			'success': function(data)
			{
				// Voted successfully						
				
				$('p.status').html(message + ' <a href="/" title="Get another tweet">Getting another tweet..</a>');
				
			},
			'error': function(xml_http_request)
			{
				if (xml_http_request.status == 403)
				{
					// Forbidden response, user has already voted
					$('p.status').html('You have already voted on this tweet. <a href="/" title="Get another tweet">Getting another..</a>');
				}
				else
				{
					// uh-oh, something else has happened
					$('p.status').text('Sorry, something went wrong. Getting another tweet..');
				}
			}
		});
		
		// Refresh the page to get another tweet
		window.setTimeout(function()
		{
			document.location.reload();
		}, 750);
	}
	
	$('form').submit(function() 
	{ 
		submit_vote(this); 
		return false;
	});
	
	
	var heartOver = function(img) {
	
		var descriptions = [
		"No love for you!",
		"Not feeling it",
		"You can have a little",
		"Loving on medium",
		"Feeling the love",
		"A whole lotta love",
		"A love supreme"];
		
		var hearton = "/static_media/images/heart.gif";
		var heartoff = "/static_media/images/heart-off.gif";
	
		var on = (img!=""); 
		
		for(var i = 0; i<window.heartCount;i++)
		{
			
			if(on)
			{
				$('#heart'+i).attr("src", hearton);
			}
			else
			{
				$('#heart'+i).attr("src", heartoff);
			}
			
			
			if($('#heart'+i).attr('id') == $(img).attr('id')) {
				on = false;
				heartnum = i; 
			}
		}
		//alert(descriptions[heartnum]);
		$('p.lovedesc').text(descriptions[heartnum]);
		
	}
	
	$('.votebuttons img')
		.hover(function() {
			heartOver(this);
		})
		.click(function() {
			heartClick(this);
		});
		
	$('.votebuttons').mouseleave(function() {
		$('.votebuttons img').attr('src', '/static_media/images/heart-off.gif');
		$('p.lovedesc').html("&nbsp;");
		
	});
	
	
});