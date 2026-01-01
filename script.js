document.addEventListener('DOMContentLoaded', () => {
    // --- Dark/Light Theme Switcher ---
    const themeToggleBtn = document.getElementById('theme-toggle');
    const htmlElement = document.documentElement;

    // Load initial theme from localStorage or default to system preference
    const savedTheme = localStorage.getItem('theme');
    if (savedTheme) {
        htmlElement.setAttribute('data-theme', savedTheme);
    } else {
        const systemPrefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
        htmlElement.setAttribute('data-theme', systemPrefersDark ? 'dark' : 'light');
    }

    themeToggleBtn.addEventListener('click', () => {
        const currentTheme = htmlElement.getAttribute('data-theme');
        const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
        
        htmlElement.setAttribute('data-theme', newTheme);
        localStorage.setItem('theme', newTheme);
        
        // Dynamic feedback icon rotation (handled via CSS transition)
    });


    // --- Clipboard Copier & Toast System ---
    const copyButtons = document.querySelectorAll('.copy-btn');
    const toast = document.getElementById('toast');
    let toastTimeout;

    copyButtons.forEach(btn => {
        btn.addEventListener('click', async () => {
            const textToCopy = btn.getAttribute('data-copy');
            const isEmail = textToCopy.includes('@');
            
            try {
                await navigator.clipboard.writeText(textToCopy);
                showToast(isEmail ? 'Email copied to clipboard!' : 'Phone number copied!');
            } catch (err) {
                console.error('Failed to copy text: ', err);
                showToast('Could not copy automatically. Please select and copy.');
            }
        });
    });

    function showToast(message) {
        // Reset animation/timeout if toast is already visible
        clearTimeout(toastTimeout);
        toast.textContent = message;
        toast.classList.add('show');

        toastTimeout = setTimeout(() => {
            toast.classList.remove('show');
        }, 2500);
    }


    // --- Skill Filtering Logic ---
    const filterButtons = document.querySelectorAll('.filter-btn');
    const skillGroups = document.querySelectorAll('.skill-category-group');

    filterButtons.forEach(btn => {
        btn.addEventListener('click', () => {
            // Update active state on buttons
            filterButtons.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');

            const filterValue = btn.getAttribute('data-filter');

            skillGroups.forEach(group => {
                const groupType = group.getAttribute('data-skill-type');
                
                if (filterValue === 'all' || filterValue === groupType) {
                    group.classList.remove('hidden');
                } else {
                    group.classList.add('hidden');
                }
            });
        });
    });


    // --- Print / PDF Generation Trigger ---
    const printBtn = document.getElementById('print-btn');
    printBtn.addEventListener('click', () => {
        window.print();
    });
});
