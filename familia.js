
document.getElementById('quiz-familia').addEventListener('submit', async (e) => {
    e.preventDefault();
    const respostas = {
        p1: document.querySelector('input[name="p1"]:checked')?.value || '',
        p2: document.querySelector('input[name="p2"]:checked')?.value || ''
    };

    console.log('Respostas:', respostas);
    alert('Respostas coletadas! Como o GitHub Pages é estático, os dados devem ser enviados manualmente ao repositório em familia.json');
});
