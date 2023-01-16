//
// const showNavbar = () => {
//     const toggle = document.querySelector('#header-toggle'),
//         nav = document.querySelector('#nav-bar'),
//         navName = document.querySelectorAll('.nav_name'),
//         myNavlist = document.querySelector('.nav_list'),
//         closeNavIcon = document.querySelector('.closeNavIcon')
//
//     if (toggle && nav && closeNavIcon ) {
//         closeNavIcon.addEventListener('click', () =>  {
//             toggleNav(nav, toggle,closeNavIcon, navName, myNavlist)
//         })
//
//         toggle.addEventListener('click', () => {
//             // show navbar
//             toggleNav(nav, toggle,closeNavIcon, navName, myNavlist)
//         })
//     }
// }
//
// const toggleNav = (nav, toggle, closeNavIcon, navName, myNavlist) =>{
//
//     nav.classList.toggle('show')
//     toggle.classList.toggle('d-none')
//     closeNavIcon.classList.toggle('d-none')
//     myNavlist.classList.toggle('align-items-center')
//
//     navName.forEach(el =>{
//         if (el.classList.contains('d-none')){
//             setTimeout(fade, 550);
//             function fade() {
//             el.classList.toggle('d-none')
//             }
//         }
//         else{
//              el.classList.toggle('d-none')
//         }
//
//           // el.classList.toggle('d-none')
//
//             })
// }
//
//
//
// /*===== LINK ACTIVE =====*/
// const colorClick = () =>{
//     const linkColor = document.querySelectorAll('.nav_link')
//     if (linkColor) {
//         linkColor.forEach(l => l.addEventListener('click', colorLink(linkColor)))
//     }
// }
//
// function colorLink(linkColor){
//     linkColor.forEach(l=> {
//         l.classList.remove('active')
//
//     })
//      if(this.classList === undefined) {return}
//     this.classList.add('active')
// }
//
// const chooseFile = (evt) => {
//     document.querySelector('.imageInput').click()
//
// }

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
}
