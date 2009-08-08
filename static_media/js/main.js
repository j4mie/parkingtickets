$(document).ready(function()
{
	/**
	 * Function called when a form is submitted
	 */
	var submit_vote = function(form)
	{
		// Get jQuery object for the form
		var form = $(form);
		var button = form.find('input.button');
		var form_id = form.attr('id');
		
		// Get correct site for images and text
		if (form_id == 'love')
		{
			var size = 'big';
			var message = 'Love sent!';
		}
		else if (form_id == 'ignore')
		{
			var size = 'small';
			var message = 'Ignored.';
		}
		else // must be 'irrelevant'
		{
			var size = 'small';
			var message = 'Flagged, thanks.';
		}
		
		// Get the value of the "action" attribute from the form.
		// This is the url we need to POST to.
		var url = form.attr('action');
		
		// Make the ajax call
		$.ajax(
		{
			'type': 'POST',
			'url': url,
			'success': function(data)
			{
				// Voted successfully						
				button.css('background-image', 'url(/static_media/images/tick_' + size + '.gif)').blur();
				$('p.status').html(message + ' <a href="/" title="Get another tweet">Getting another tweet..</a>');
				$('form')
					.filter(function (index)
					{
						return $(this).attr('id') != form.attr('id');
					})
					.css('opacity', '0.2');
			},
			'error': function(xml_http_request)
			{
				if (xml_http_request.status == 403)
				{
					// Forbidden response, user has already voted
					button.css('background-image', 'url(/static_media/images/cross.gif)').blur();
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
});