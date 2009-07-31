$(document).ready(function()
{
	/**
	 * Function called when a form is submitted
	 */
	var submit_vote = function(form)
	{
		// Get jQuery object for the form
		form = $(form);
		button = form.find('p input.button');
		
		// Get the value of the "action" attribute from the form.
		// This is the url we need to POST to.
		url = form.attr('action');
		
		// Make the ajax call
		$.ajax(
		{
			'type': 'POST',
			'url': url,
			'success': function(data)
			{
				// Voted successfully				
				button.css('background-image', 'url(/static_media/images/tick.png)').blur();
			},
			'error': function(xml_http_request)
			{
				if (xml_http_request.status == 403)
				{
					// Forbidden response, user has already voted
					button.css('background-image', 'url(/static_media/images/cross.png)').blur();
					$('p.status').text('You have already voted on this tweet');
				}
				else
				{
					// uh-oh, something else has happened
				}
			}
		});
	}
	
	$('form').submit(function() 
	{ 
		submit_vote(this); 
		return false;
	});
});