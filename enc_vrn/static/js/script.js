document.addEventListener("DOMContentLoaded", function () {
        const fileUploader1 = document.getElementById('file-input-enc');
        if (fileUploader1) {
            fileUploader1.addEventListener('change', (event) => {
                const logoFiles = event.target.files;
                console.log('files', logoFiles);

                const feedback = document.getElementById('feedback1');
                feedback.innerHTML = `Файл загружен успешно`;
            });
        }
    }
);