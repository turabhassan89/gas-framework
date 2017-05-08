<!--
subscribe.tpl - Get user's credit card details to send to Stripe service
Copyright (C) 2011-2017 Vas Vasiliadis <vas@uchicago.edu>
University of Chicago
-->

%include('views/header.tpl')
<!-- Captures the user's credit card information and uses Javascript to send to Stripe -->

<div class="container">
	<div class="page-header">
		<h2>Subscribe</h2>
	</div>

	<p>You are subscribing to the GAS Premium plan. Please enter your credit card details to complete your subscription.</p><br />


</div> <!-- container -->

%rebase('views/base', title='GAS - Subscribe')