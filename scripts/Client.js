let socket = new WebSocket('ws://ptl-0fd55363-1c3e108f.libcurl.so/pentesterlab');

// socket is used for establishing persistent connection like games, streams

socket.onopen = (e) => {
	console.log(e);
	alert("Connection Established");
	socket.send("key");
}

socket.onmessage = (message) => {
	console.log(message.data);
}