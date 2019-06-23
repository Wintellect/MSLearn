$(function () {
    var url = "http://FQDN:8008/predict";

    // Handle clicks of the Analyze button
    $("#analyze-button").click(function() {
        // Get user input
        var text = $("#input-text").val();

        // Invoke model using REST call
        $.ajax({
            type: "GET",
            url: url + "?text=" + encodeURIComponent(text),
        }).done(function (data) {
            showResults(data);
        }).fail(function(xhr, status, err) {
            alert(status + " (" + err + ")");
        });
    });
});

function showResults(data) {
    alert(parseFloat(data).toFixed(4));
}