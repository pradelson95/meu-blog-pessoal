// ==========================================================================
// BASE DE DATOS LOCAL DE PUBLICACIONES (POSTS)
// ==========================================================================
const postsData = {
  "1": {
    title: "O que realmente está sob o nosso controle diante da tempestade",
    date: "18 de Agosto, 2026",
    content: `
      <blockquote>"Visto que ninguém sabe o que vai acontecer, quem lhe poderá dizer o que há de vir?" — Eclesiastes 8:7</blockquote>

      <p>Há nove meses, a minha realidade mudou. Um familiar próximo começou a enfrentar uma depressão profunda. No início, foi extremamente difícil, pois eu nunca tinha lidado ou convivido diretamente com alguém sofrendo com essa condição. É doloroso ver que a pessoa já não é a mesma de antes.</p>

      <p>Durante muito tempo, vi-me preso a pensamentos negativos: <em>"Por que isso está acontecendo comigo?", "O que eu fiz de errado?", "A vida antes era muito melhor", "Minha vida agora é um desastre"</em>. Eu estava tão focado na escuridão do problema que acabei esquecendo de enxergar as bençãos que ainda tinha e de procurar o lado positivo das situações.</p>

      <p>Nessa jornada, entendi na pele o sentido de Provérbios 17:17: <em>"O verdadeiro amigo ama em todos os momentos e se torna um irmão em tempos de aflição."</em> Tive o apoio inestimável de amigos verdadeiros que estiveram e continuam estando ao meu lado. Amigos assim são uma benção que nada no mundo pode substituir, nem mesmo todo o ouro do planeta.</p>

      <p>Aprendi que, quando estamos no meio de uma tempestade de problemas, o mais importante não é desistir nem se deixar levar pela força do vento, mas sim decidir como reagir a ela. Decidir que tipo de pessoa você escolherá ser diante das adversidades — é isso o que realmente está sob o seu controle.</p>
    `
  },
  "2": {
    title: "A verdadeira paciência: Aprender a esperar quando o tempo parece parar",
    date: "6 de Setembro, 2026",
    content: `
      <blockquote>"Alegrem-se na esperança. Suportem as dificuldades. Perseverem na oração." — Romanos 12:12</blockquote>

      <p>Passamos a vida inteira ouvindo falar sobre a paciência. Ouvimos conselhos, lemos frases motivacionais e achamos que entendemos o seu significado. No entanto, a verdade é que ninguém sabe realmente o que é a paciência até ser colocado em uma situação onde não há outra escolha a não ser esperar.</p>

      <p>Quando enfrentamos a doença prolongada de alguém que amamos, o peso emocional pode ser avassalador. Há dias em que parece que o tempo simplesmente parou. Olhamos para o relógio, para os meses que se passam, e a sensação é de que estamos estagnados, sem avançar um único passo. Nessas horas, a exaustão tenta nos convencer de que aquela dor durará para sempre.</p>

      <p>Mas essa percepção distorcida do tempo não é a realidade; é a desesperança e a ansiedade falando mais alto. Nada neste mundo dura para sempre — nem os momentos bons, nem as fases mais escuras e difíceis. A tempestade atual também passará.</p>

      <p>Uma das coisas que mais tem me fortalecido nesta jornada é observar a paciência de outras pessoas que estão enfrentando lutas semelhantes. Ver a resiliência de quem carrega fardos pesados e ainda assim continua caminhando me lembra de que não estou sozinho. Saber que outros compartilham dessa mesma batalha renova as minhas forças e me dá motivação para cultivar essa virtude todos os dias.</p>

      <p>Se você também está passando por um período em que os dias parecem infinitos, lembre-se: viva um dia de cada vez. Mantenha a esperança acesa, apoie-se naqueles que entendem a sua dor e confie que cada pequeno passo conta. O tempo continua avançando e, com ele, a renovação e a paz que tanto buscamos inevitavelmente chegarão.</p>
    `
  }
};

// ==========================================================================
// SELECCIÓN DE ELEMENTOS DEL DOM
// ==========================================================================
const feedView = document.getElementById('feed-view');
const detailView = document.getElementById('detail-view');
const backBtn = document.getElementById('back-btn');

const articleTitle = document.getElementById('article-title');
const articleDate = document.getElementById('article-date');
const articleContent = document.getElementById('article-content');

// Elementos de la sección de comentarios
const commentForm = document.getElementById('comment-form');
const commentInput = document.getElementById('comment-input');
const commentsList = document.getElementById('comments-list');

let currentPostId = null;

// ==========================================================================
// FUNCIONES DE CONTROL DE VISTAS Y ARTÍCULOS
// ==========================================================================
function showFeed() {
  detailView.classList.remove('active');
  feedView.classList.add('active');
  window.scrollTo({ top: 0, behavior: 'smooth' });
}

function showArticle(postId) {
  const post = postsData[postId];
  if (!post) return;

  currentPostId = postId;
  articleTitle.textContent = post.title;
  articleDate.textContent = post.date;
  articleContent.innerHTML = post.content;

  // Carga los comentarios guardados en localStorage para este post
  loadComments(postId);

  feedView.classList.remove('active');
  detailView.classList.add('active');
  window.scrollTo({ top: 0, behavior: 'smooth' });
}

// ==========================================================================
// GESTIÓN DE COMENTARIOS ANÓNIMOS (LOCALSTORAGE)
// ==========================================================================
function loadComments(postId) {
  const allComments = JSON.parse(localStorage.getItem('blog_comments')) || {};
  const postComments = allComments[postId] || [];

  commentsList.innerHTML = '';

  if (postComments.length === 0) {
    commentsList.innerHTML = '<p class="no-comments">Nenhum comentário ainda. Seja o primeiro a comentar!</p>';
    return;
  }

  postComments.forEach(comment => {
    const card = document.createElement('div');
    card.className = 'comment-card';

    const header = document.createElement('div');
    header.className = 'comment-header';

    const author = document.createElement('span');
    author.className = 'comment-author';
    author.textContent = comment.author;

    const date = document.createElement('span');
    date.className = 'comment-date';
    date.textContent = comment.date;

    header.appendChild(author);
    header.appendChild(date);

    const text = document.createElement('p');
    text.className = 'comment-text';
    text.textContent = comment.text; // .textContent previene vulnerabilidades XSS

    card.appendChild(header);
    card.appendChild(text);

    commentsList.appendChild(card);
  });
}

commentForm.addEventListener('submit', (e) => {
  e.preventDefault();

  const text = commentInput.value.trim();
  if (!text || !currentPostId) return;

  const newComment = {
    author: "Anônimo",
    date: new Date().toLocaleDateString('pt-BR', {
      day: '2-digit',
      month: 'short',
      year: 'numeric'
    }),
    text: text
  };

  const allComments = JSON.parse(localStorage.getItem('blog_comments')) || {};
  if (!allComments[currentPostId]) {
    allComments[currentPostId] = [];
  }

  allComments[currentPostId].unshift(newComment);
  localStorage.setItem('blog_comments', JSON.stringify(allComments));

  commentInput.value = '';
  loadComments(currentPostId);
});

// ==========================================================================
// REGISTRO DE EVENTOS DE NAVEGACIÓN
// ==========================================================================
document.querySelectorAll('.post-card').forEach(card => {
  card.addEventListener('click', () => {
    const postId = card.getAttribute('data-id');
    showArticle(postId);
    history.pushState({ view: 'detail', id: postId }, '', `#post-${postId}`);
  });
});

backBtn.addEventListener('click', () => {
  showFeed();
  history.pushState({ view: 'feed' }, '', window.location.pathname);
});

window.addEventListener('popstate', (e) => {
  if (e.state && e.state.view === 'detail') {
    showArticle(e.state.id);
  } else {
    showFeed();
  }
});

window.addEventListener('DOMContentLoaded', () => {
  const hash = window.location.hash;
  if (hash.startsWith('#post-')) {
    const postId = hash.replace('#post-', '');
    showArticle(postId);
  }
});