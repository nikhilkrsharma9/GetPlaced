// Dropdown for Login and Register
document.querySelectorAll('nav > div').forEach(function(drop){
    drop.addEventListener('mouseenter', function(){
        this.querySelector('div').style.display = 'block';
    });
    drop.addEventListener('mouseleave', function(){
        this.querySelector('div').style.display = 'none';
    });
});