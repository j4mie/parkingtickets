$(document).ready(function()
{
	/**
	 * Function called when a form is submitted
	 */
	var submit_vote = function(form)
	{
		console.log('submitted');
		// Get jQuery object for the form
		var form = $(form);
		var button = form.find('input.button');
		
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
				button.css('background-image', 'url(/static_media/images/tick.png)').blur();
				$('p.status').html('<a href="/" title="Get another tweet">Get another tweet</a>');
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
					button.css('background-image', 'url(/static_media/images/cross.png)').blur();
					$('p.status').html('You have already voted on this tweet. <a href="/" title="Get another tweet">Get another.</a>');
				}
				else
				{
					// uh-oh, something else has happened
					$('p.status').text('Sorry, an error has occurred');
				}
			}
		});
	}
	
	$('form').submit(function() 
	{ 
		console.log('here');
		submit_vote(this); 
		return false;
	});
});