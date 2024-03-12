document.getElementById('pageSelect').addEventListener('change', function() {
    var selectedPage = this.value;
    document.querySelectorAll('.page').forEach(function(page) {
        page.classList.remove('active');
        if(page.id === selectedPage) {
            page.classList.add('active');
        }
    });
});
