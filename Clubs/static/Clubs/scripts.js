const showModal = () => {
    let modalContainer = document.querySelector('#leaveClub')
    let leaveBtn = document.querySelector('.leaveBtn')
    if (modalContainer){
        leaveBtn.addEventListener('click', evt =>{
            // modalContainer.style.display = "block"
        })
}
}

const hoverCircle = () =>{
    let imgCircle = document.querySelector('.imgCircle')
    let circleOnHover = document.querySelector('.circleOnHover')
    if(imgCircle && circleOnHover){
        imgCircle.addEventListener('mouseover', (evt) =>{
            circleOnHover.classList.add('onHoverfilter')

        })

        imgCircle.addEventListener("mouseleave", (evt) => {
            circleOnHover.classList.remove('onHoverfilter')
      });
     }
}
const messageSuccess = () =>{
      let savedWrap = document.querySelector('.savedWrap')
    if (savedWrap){
        setTimeout(fade_out, 4200);
    function fade_out() {
        savedWrap.remove()
    }

    }
}


allFunctions()
if (document.readyState !== 'loading') {
    allFunctions()
}

document.body.addEventListener('htmx:afterOnLoad', event=>{
    allFunctions()
})
function allFunctions(){
    hoverCircle()
    messageSuccess()
    showModal()
}
