let addSession = document.querySelector('.addSession')
if(addSession) {
    addSession.addEventListener('change', (evt) => {

        evt.currentTarget
            .querySelectorAll('.activeType')
            .forEach(element => {
                element.classList.remove("activeType")
            })

        evt.target
            .closest('.count_icon')
            .classList.add("activeType");
    }, true);
}

