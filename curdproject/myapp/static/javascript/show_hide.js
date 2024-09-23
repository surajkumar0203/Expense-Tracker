const show=(event,id)=>{
    const inputFields=document.getElementById(id);
    const showsrc=event.getAttribute('data-show-src');
    inputFields.type='text'
    event.src=showsrc
    event.alt=showsrc
}
const hide=(event,id)=>{
    const inputFields=document.getElementById(id);
    const hidesrc=event.getAttribute('data-hide-src');
    inputFields.type='password'
    event.src=hidesrc
    event.alt=hidesrc
}

