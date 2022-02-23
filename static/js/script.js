/*jshint esversion: 6 */
// Below partially from Code Institutes CodeStar project
document.addEventListener("DOMContentLoaded", function () {
    let messages = document.getElementById('msg');

        if (messages) {
            setTimeout(function () {
                let alert = new bootstrap.Alert(messages);
                alert.close();
            }, 3000);
        }
    
});