const coinCard=document.querySelectorAll('.coin-display-card');
const alertButton=document.querySelectorAll('.set-alert-button')
const alertOverlay=document.querySelector('#set-alerts-overlay');
const closeAlert=document.querySelector('#set-alerts-overlay button')
const coinList=document.querySelector('#coins-listing')


// Close Set Alerts Overlay
closeAlert.addEventListener('click',()=>{
    alertOverlay.style.width='0';
    alertOverlay.style.visibility='hidden';
    // coinList.style.overflowY='scroll';
})
// Show set alerts option on hover
for(let card of coinCard){
    card.addEventListener('mouseenter',(event)=>{
        let tempTarget=event.target.querySelector('.set-alert-button');
        tempTarget.style.width='110px';
        tempTarget.style.visibility='visible';
    })

    card.addEventListener('mouseleave',(event)=>{
        let tempTarget=event.target.querySelector('.set-alert-button');
        tempTarget.style.width='0px';
        tempTarget.style.visibility='hidden';
    })
}

// Open alert overlay
for(let button of alertButton){
    button.addEventListener('click',(event)=>{
        alertOverlay.style.width='100%';
        alertOverlay.style.visibility='visible';
        console.log(event.target.offsetTop);
        // coinList.style.overflowY='hidden';
    })
}