# Vamos criar dois arquivos HTML e dois arquivos JSON simulando a aplicação separada.

familia_html = '''
<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Quiz da Família - AEE</title>
<link rel="stylesheet" href="style.css">
<script defer src="familia.js"></script>
</head>
<body>
  <div class="container">
    <h1>Quiz da Família</h1>
    <form id="quiz-familia">
      <div class="pergunta">
        <p>1. Você considera o atendimento AEE importante para o desenvolvimento do seu filho(a)?</p>
        <label><input type="radio" name="p1" value="Sim"> Sim</label>
        <label><input type="radio" name="p1" value="Não"> Não</label>
      </div>
      <div class="pergunta">
        <p>2. Você sente que recebe informações suficientes sobre o progresso do seu filho(a)?</p>
        <label><input type="radio" name="p2" value="Sim"> Sim</label>
        <label><input type="radio" name="p2" value="Não"> Não</label>
      </div>
      <button type="submit">Enviar Respostas</button>
    </form>
  </div>
</body>
</html>
'''

familia_js = '''
document.getElementById('quiz-familia').addEventListener('submit', async (e) => {
    e.preventDefault();
    const respostas = {
        p1: document.querySelector('input[name="p1"]:checked')?.value || '',
        p2: document.querySelector('input[name="p2"]:checked')?.value || ''
    };

    console.log('Respostas:', respostas);
    alert('Respostas coletadas! Como o GitHub Pages é estático, os dados devem ser enviados manualmente ao repositório em familia.json');
});
'''

professor_html = '''
<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Quiz do Professor/Atendimento AEE</title>
<link rel="stylesheet" href="style.css">
<script defer src="professor.js"></script>
</head>
<body>
  <div class="container">
    <h1>Quiz do Professor/Atendimento AEE</h1>
    <form id="quiz-professor">
      <div class="pergunta">
        <p>1. Você considera que o AEE contribui para o aprendizado dos alunos com deficiência?</p>
        <label><input type="radio" name="p1" value="Sim"> Sim</label>
        <label><input type="radio" name="p1" value="Parcialmente"> Parcialmente</label>
        <label><input type="radio" name="p1" value="Não"> Não</label>
      </div>
      <div class="pergunta">
        <p>2. Há recursos e suporte suficientes para realizar o atendimento AEE?</p>
        <label><input type="radio" name="p2" value="Sim"> Sim</label>
        <label><input type="radio" name="p2" value="Não"> Não</label>
      </div>
      <button type="submit">Enviar Respostas</button>
    </form>
  </div>
</body>
</html>
'''

professor_js = '''
document.getElementById('quiz-professor').addEventListener('submit', async (e) => {
    e.preventDefault();
    const respostas = {
        p1: document.querySelector('input[name="p1"]:checked')?.value || '',
        p2: document.querySelector('input[name="p2"]:checked')?.value || ''
    };

    console.log('Respostas:', respostas);
    alert('Respostas coletadas! Como o GitHub Pages é estático, os dados devem ser enviados manualmente ao repositório em professor.json');
});
'''

familia_json = '[\n  {\n    "p1": "Sim",\n    "p2": "Sim"\n  }\n]'
professor_json = '[\n  {\n    "p1": "Sim",\n    "p2": "Não"\n  }\n]'

# Gravando os arquivos simulados.
with open('familia.html', 'w', encoding='utf-8') as f:
    f.write(familia_html)
with open('familia.js', 'w', encoding='utf-8') as f:
    f.write(familia_js)
with open('familia.json', 'w', encoding='utf-8') as f:
    f.write(familia_json)

with open('professor.html', 'w', encoding='utf-8') as f:
    f.write(professor_html)
with open('professor.js', 'w', encoding='utf-8') as f:
    f.write(professor_js)
with open('professor.json', 'w', encoding='utf-8') as f:
    f.write(professor_json)

'Arquivos gerados: familia.html, familia.js, familia.json, professor.html, professor.js, professor.json'