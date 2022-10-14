$(document).ready(function () {

	function readURL(input) {
		if (input.files && input.files[0]) {
			var reader = new FileReader();

			reader.onload = function (e) {
				$('#selected_image')
					.attr('src', e.target.result)
					.width(176)
					.height(176);
			}
			reader.readAsDataURL(input.files[0]);
		}
	}

	$('#imagefile').change(function () {
		readURL(this);
	});


	$("form#analysis-form").submit(function (event) {
		event.preventDefault();

		var imagefile = $('#imagefile')[0].files;

		if (!imagefile.length > 0) {
			alert("Please select a file to analyze!");
		}
		else {
			$("button#analyze-button").html("Analyzing..");
			$("button#analyze-button").prop("disabled", "true");

			var fd = new FormData();
			fd.append('file', imagefile[0]);

			var loc = window.location;

			$.ajax({
				method: 'POST',
				async: true,
				url: loc.protocol + '//' + loc.hostname + ':' + loc.port + '/analyze',
				data: fd,
				processData: false,
				contentType: false,
			}).done(function (data) {
				window.location.href = `/result?id=${data.product_id}`
			}).fail(function (e) {
				console.log("Fail Request!");
				console.log(e);
			});
		};
		console.log("Submitted!");
	});
});
