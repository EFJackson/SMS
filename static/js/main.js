if($(document).width() > 768){
	var h = $('.content').height() / 2;
	$('#contact').nextAll('div').css({'margin-bottom':'800px'})
	var tri = $('.tri-l');

	$('.content').scroll(function(){
		if($('#contact').offset().top < h){
			tri.animate({'margin-top':'6.8em'}, 200);
		}
		else if($('#events').offset().top < h){
	        tri.animate({'margin-top':'3.8em'}, 200);
	    }
	    else {
	    	tri.animate({'margin-top':'0.8em'}, 200);
	    }
	});
}

$(document).ready(function(){
	$('.trigger').click(function(event){
		event.preventDefault();
		$(this).parent('p').prevAll('.short:first').slideToggle(function(){
			$(this).is(':visible') ? '(Read less)' : 'Read more here!';
		});
		$(this).parent('p').prevAll('.long:first').slideToggle(function(){
			$('.trigger').html($(this).is(':visible') ? '(Read less)' : 'Read more here!');
		});
	});
});