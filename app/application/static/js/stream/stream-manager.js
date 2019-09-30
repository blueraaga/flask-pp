document.addEventListener("DOMContentLoaded", function() {

    var i = 0;

    var source = new EventSource('http://127.0.0.1:7999/stream/message/sse');

    console.log(i++ + " ::: " + Date.now() + " With credentials? " + source.withCredentials);
    console.log(i++ + " ::: " + Date.now() + " Ready state: " + source.readyState);
    console.log(i++ + " ::: " + Date.now() + " URL: " + source.url);

    source.onopen = function() {
        console.log(i++ + " ::: " + Date.now() + " Connection Open now");
        console.log(i++ + " ::: " + Date.now() + " Ready state: " + source.readyState);
        // connectionOpen(true);
    };
    source.onerror = function () {
        console.log(i++ + " ::: " + Date.now() + " Connection Closed because of error now");
        // connectionOpen(false);
        console.log(i++ + " ::: " + Date.now() + " Ready state: " + source.readyState);
    };

    // source.addEventListener('connections', updateConnections, false);
    // source.addEventListener('requests', updateRequests, false);
    // source.addEventListener('uptime', updateUptime, false);
    source.addEventListener('ranstr', insertData, false);

    function insertData(event) {
        console.log(event.data);
        console.log(i++ + " ::: " + Date.now() + " [on message called from insertData]");
        mE = document.getElementById("stream-message");
        cE = document.createElement("p");
        cE.innerHTML = event.data;
        mE.prepend(cE);    
    }
    
    source.onmessage = function (event) {
    // a message without a type was fired
    console.log(event.data);
    console.log(i++ + " ::: " + Date.now() + " [on message called from onmessage]");
    document.getElementById("stream-message").prepend(event.data);
    };
});
