<!--
scripts.tpl - All GAS-specific Javascript
Copyright (C) 2011-2017 Vas Vasiliadis <vas@uchicago.edu>
University of Chicago
-->

<!-- Handle events on file select control -->
<script type="text/javascript">
$(document).on('change', '.btn-file :file', function() {
  var input = $(this),
      numFiles = input.get(0).files ? input.get(0).files.length : 1,
      label = input.val().replace(/\\/g, '/').replace(/.*\//, '');
  input.trigger('fileselect', [numFiles, label]);
});

$(document).ready( function() {
  $('.btn-file :file').on('fileselect', function(event, numFiles, label) {
    var input = $(this).parents('.input-group').find(':text'),
        log = numFiles > 1 ? numFiles + ' files selected' : label;
        
    if( input.length ) {
      input.val(log);
    } else {
      if( log ) alert(log);
    }      
  });
});

// Disable submit button until file is selected
$(document).ready( function(){
  $('input:file').change( function(){
    if ($(this).val()) {
      $('input:submit').attr('disabled',false);
      // or, as has been pointed out elsewhere:
      // $('input:submit').removeAttr('disabled'); 
    } 
  });
});
</script>

<!-- Enable some JS effects -->
<script type="text/javascript">
// Modal and alert box handling
$(document).ready(function(){
	// Add the alert div
	$("#alert-div").html('<div id="alert-fading-message" class="alert alert-info alert-block"><button type="button" class="close" data-dismiss="alert">&times;</button><h4 class="alert-headline"></h4><span class="alert-message"></span></div>');
	// Hide the alert div
	$("div#alert-fading-message").hide();
});

// Animates in-line alerts to make them fade away after a short delay (default 5 sec.)
function fadeAlertDiv(timeoutDelay, redirectUrl) {
	timeoutDelay = typeof timeoutDelay !== 'undefined' ? timeoutDelay : 5000;
	redirectUrl = typeof redirectUrl !== 'undefined' ? redirectUrl : window.location.href;
	window.setTimeout(function() {
		$('#alert-fading-message').animate({
			opacity: 0.25,
			height: 'toggle'
		}, {duration: 2000});
		window.location.href = redirectUrl;
	}, timeoutDelay);
}
</script>

<!-- ADD STRIPE JS CODE BELOW -->
