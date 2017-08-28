window.onload = function()
{	// Vertical
	
	var mask = document.getElementById('scroll-mask');
	var content = document.getElementById('scroll-content');
	var mask1 = document.getElementById('scroll-mask1');
	var content1 = document.getElementById('scroll-content1');
	
	new Dragdealer('scroll-bar',
	{
		horizontal: false,
		vertical: true,
		yPrecision: content.offsetHeight,
		animationCallback: function(x, y)
		{
			var margin = y * (content.offsetHeight - mask.offsetHeight);
			content.style.marginTop = String(-margin) + 'px';
		}
	});

	new Dragdealer('scroll-bar1',
	{
		horizontal: false,
		vertical: true,
		yPrecision: content1.offsetHeight,
		animationCallback: function(x, y)
		{
			var margin = y * (content1.offsetHeight - mask1.offsetHeight);
			content1.style.marginTop = String(-margin) + 'px';
		}
	});
}
