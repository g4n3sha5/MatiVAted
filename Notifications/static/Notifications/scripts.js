let url = `ws://${window.location.host}/ws/socket-server/`
const mySocket = new WebSocket(url)

mySocket.onmessage = function (e) {
    let data = JSON.parse(e.data)
    console.log('Data:', data)
}