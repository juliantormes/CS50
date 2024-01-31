document.addEventListener('DOMContentLoaded', (event) => {
    var items = document.querySelectorAll('.circle a');

    // Adjusting the radius based on the new size of the globe icon
    var radius = 45; // This value might need fine-tuning based on the exact size of your globe icon and the desired distance of the social icons from the center

    for (var i = 0, l = items.length; i < l; i++) {
        // Positioning the social icons based on the radius
        items[i].style.left = (50 - radius * Math.cos(-0.5 * Math.PI - 2 * (1 / l) * i * Math.PI)).toFixed(4) + "%";
        items[i].style.top = (50 + radius * Math.sin(-0.5 * Math.PI - 2 * (1 / l) * i * Math.PI)).toFixed(4) + "%";
    }

    document.querySelector('.menu-button').onclick = function (e) {
        e.preventDefault();
        document.querySelector('.circle').classList.toggle('open');
    }
});