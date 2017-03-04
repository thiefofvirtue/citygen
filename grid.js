$(document).ready(function() {
	'use strict';
	$('#genButton').hover(
		function() {
			$(this).addClass('active');
			}, 
		function() {
			$(this).removeClass('active');
			}
		);
	$('#genButton').click(function() {
		var $gridCols = $('#columnsBox').val();
		var $gridRows = $('#rowsBox').val();
		$('#gridContainer').height($gridRows * 100 + 'px');
		$('#gridContainer').width($gridCols * 100 + 'px');
		$('#gridContainer').css("border","3px solid black");
		for (var i = 0; i < $gridRows; i++) {
			$('#gridContainer').append('<div class="row"></div>');
			}
		while ($gridCols > 0) {
			$('.row').append('<div class="column"></div>');
			$gridCols--;
		}
	});
});
