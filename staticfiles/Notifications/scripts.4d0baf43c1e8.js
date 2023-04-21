// let url = `ws://127.0.0.1:8000/ws/notify/`
let url = `ws://${window.location.host}:8000/ws/notify/`

const mySocket = new WebSocket(url)

mySocket.onmessage = function (e) {
    let data = JSON.parse(e.data)
    console.log('Data:', data)
}