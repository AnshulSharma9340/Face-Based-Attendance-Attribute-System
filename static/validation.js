// validation.js
// Generic form validation logic for Face-Based Attendance System

document.addEventListener('DOMContentLoaded', () => {
    'use strict';

    // Fetch all the forms we want to apply custom Bootstrap validation styles to
    const forms = document.querySelectorAll('.needs-validation');

    // Loop over them and prevent submission
    Array.from(forms).forEach(form => {
        form.addEventListener('submit', event => {
            if (!form.checkValidity()) {
                event.preventDefault();
                event.stopPropagation();
            }

            form.classList.add('was-validated');
        }, false);
    });

    // Optional: Real-time validation feedback on input
    const inputs = document.querySelectorAll('input, select, textarea');
    inputs.forEach(input => {
        input.addEventListener('input', () => {
            if (input.checkValidity()) {
                input.classList.remove('is-invalid');
                input.classList.add('is-valid');
            } else {
                input.classList.remove('is-valid');
                // Don't add is-invalid immediately on input to avoid annoyance, 
                // but if it was already marked invalid by submit, keep it valid/invalid dynamic
                if (input.parentElement.classList.contains('was-validated')) {
                     input.classList.add('is-invalid');
                }
            }
        });
    });
});
