document.addEventListener('DOMContentLoaded', function (){
    const backgrounds=[
        'pixil-frame-0.png',
        'pixil-frame-1.png',        
        'pixil-frame-2.png',
        'pixil-frame-3.png',
        'pixil-frame-4.png',
        'pixil-frame-5.png',
        'pixil-frame-6.png',  
    ];

    let index = 0;

    function changeBackground() {
        const backgroundElement = document.querySelector('.png')
        const nextIndex = (index + 1) % backgrounds.length;
        backgroundElement.computedStyleMap.backgroundImage = `url('/static/${backgrounds[nextIndex]}`;
        index = nextIndex;
    }

    setInterval(changeBackground, 5000);
})