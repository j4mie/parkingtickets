from django import template

register = template.Library()	
        
def _wrap_with_insensitive(string, target, before, after):
	lowercase_string = string.lower()
	lowercase_target = target.lower()
	target_length = len(target)
	index = lowercase_string.find(lowercase_target)
	
	if index < 0:
		return string
	else:
		return string[:index] + before + string[index:index + target_length] + after + string[index + target_length:]

@register.filter(name='strongify')       
def strongify(string, target):
	return _wrap_with_insensitive(string, target, '<strong>', '</strong>')