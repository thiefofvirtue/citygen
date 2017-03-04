// JavaScript Document
$(document).ready(function() {
		'use strict';
	//Sets empty terrain array
	var terrains = [];
	
	// Makes the generator button have and remove the Active css class
	$('#genButton').hover(
		function() {
			$(this).addClass('active');
			}, 
		function() {
			$(this).removeClass('active');
			}
		);
	
	//Tries to take value of input button and adds to div
	$('#addTer').click(function(){
			terrains.push('#terraIn').val();
			$('#target').append(terrains);
		
	});

	
});