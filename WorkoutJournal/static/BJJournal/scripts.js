//
// let addSession = document.getElementsByClassName ('addSession')
// if(addSession) {
//     addSession.forEach(sessionClass => {
//         console.log(sessionClass)
//         sessionClass.addEventListener('change', (evt) => {
//             evt.currentTarget
//                 .querySelectorAll('.activeType')
//                 .forEach(element => {
//                     element.classList.remove("activeType")
//                 })
//
//             evt.target
//                 .closest('.count_icon')
//                 .classList.add("activeType");
//         }, true);
//     })
// }
//


if (document.readyState !== 'loading') {
   onClickColor()
    quickDateButtons()
}

function onClickColor() {
    let addSession = document.getElementsByClassName('addSession')
    if (addSession) {

        Array.from(addSession).forEach(sessionClass => {
            Array.from(sessionClass.querySelectorAll('.count_icon'))
                .forEach(count_icon => {

                    count_icon.addEventListener('click', (evt) => {
                        sessionClass.querySelectorAll('.activeType')
                            .forEach(element => {
                                element.classList.remove("activeType")
                                })

                        evt.target
                            .closest('.count_icon')
                            .classList.add("activeType");
                    }, true);

                }, true);
        })
    }
}
function quickDateButtons(){
     let todayBtn = document.querySelector('.today')
    let yesterdayBtn = document.querySelector('.yesterday')
    let datePicker = document.querySelector('.datepicker-input')
    let today = new Date()
    let yesterday =  new Date(Date.now() - 86400000)


    todayBtn.addEventListener('click', (evt) =>{
       datePicker.valueAsDate = today
    })

   yesterdayBtn.addEventListener('click', (evt) =>{
       datePicker.valueAsDate = yesterday
    })
}
function ro


