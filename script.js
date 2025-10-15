const buyBtn=document.getElementById('buyBtn');const modal=document.getElementById('modal');const year=document.getElementById('yr');if(year)year.textContent=(new Date()).getFullYear();
function openModal(){modal.setAttribute('aria-hidden','false')}function closeModal(){modal.setAttribute('aria-hidden','true')}
buyBtn.addEventListener('click',openModal);modal.addEventListener('click',e=>{if(e.target===modal)closeModal()});window.addEventListener('keydown',e=>{if(e.key==='Escape')closeModal()});
