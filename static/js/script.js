// Below from Code Institutes CodeStar project
document.addEventListener("DOMContentLoaded", function () {
    let messages = document.getElementById('msg');

    for (message in messages) {
        if (messages) {
            setTimeout(function () {
                let alert = new bootstrap.Alert(messages);
                alert.close()
            }, 3000);
        }
    }
})