// ==========================================================================
// BASE DE DATOS LOCAL DE PUBLICACIONES (POSTS)
// Objeto JS que funciona como repositorio central de contenidos
// ==========================================================================
const postsData = {
  // Entrada indexada con la clave/ID "1"
  "1": {
    title: "O que realmente está sob o nosso controle diante da tempestade", // Título completo del artículo
    date: "18 de Agosto, 2026", // Fecha formateada para mostrar en la interfaz
    content: `
      <blockquote>"Visto que ninguém sabe o que vai acontecer, quem lhe poderá dizer o que há de vir?" — Eclesiastes 8:7</blockquote>

      <p>Há nove meses, a minha realidade mudou. Um familiar próximo começou a enfrentar uma depressão profunda. No início, foi extremamente difícil, pois eu nunca tinha lidado ou convivido diretamente com alguém sofrendo com essa condição. É doloroso ver que a pessoa já não é a mesma de antes.</p>

      <p>Durante muito tempo, vi-me preso a pensamentos negativos: <em>"Por que isso está acontecendo comigo?", "O que eu fiz de errado?", "A vida antes era muito melhor", "Minha vida agora é um desastre"</em>. Eu estava tão focado na escuridão do problema que acabei esquecendo de enxergar as bençãos que ainda tinha e de procurar o lado positivo das situações.</p>

      <p>Nessa jornada, entendi na pele o sentido de Provérbios 17:17: <em>"O verdadeiro amigo ama em todos os momentos e se torna um irmão em tempos de aflição."</em> Tive o apoio inestimável de amigos verdadeiros que estiveram e continuam estando ao meu lado. Amigos assim são uma benção que nada no mundo pode substituir, nem mesmo todo o ouro do planeta.</p>

      <p>Aprendi que, quando estamos no meio de uma tempestade de problemas, o mais importante não é desistir nem se deixar levar pela força do vento, mas sim decidir como reagir a ela. Decidir que tipo de pessoa você escolherá ser diante das adversidades — é isso o que realmente está sob o seu controle.</p>
    ` // Cadena con etiquetas HTML integradas para renderizado estructurado
  },
  
  // Entrada indexada con la clave/ID "2"
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
// SELECCIÓN DE ELEMENTOS DEL DOM (DOCUMENT OBJECT MODEL)
// Guarda referencias directas a los elementos del HTML para manipularlos
// ==========================================================================
const feedView = document.getElementById('feed-view');       // Sección que contiene el listado de posts
const detailView = document.getElementById('detail-view');   // Sección que muestra la lectura completa
const backBtn = document.getElementById('back-btn');         // Botón interactivo para regresar al feed

const articleTitle = document.getElementById('article-title');   // Etiqueta H1 de la vista detallada
const articleDate = document.getElementById('article-date');     // Etiqueta TIME de la vista detallada
const articleContent = document.getElementById('article-content'); // Div contenedor del texto completo del post

// ==========================================================================
// FUNCIONES DE CONTROL Y NAVEGACIÓN ENTRE VISTAS
// ==========================================================================

/**
 * Muestra la vista principal (Feed) y oculta el artículo detallado
 */
function showFeed() {
  detailView.classList.remove('active'); // Retira la clase activa para ocultar el detalle
  feedView.classList.add('active');      // Agrega la clase activa para mostrar el feed
  window.scrollTo({ top: 0, behavior: 'smooth' }); // Realiza un desplazamiento suave al inicio de la página
}

/**
 * Carga los datos de un post en el DOM y cambia a la vista detallada
 * @param {string} postId - ID clave del post a cargar ("1", "2", etc.)
 */
function showArticle(postId) {
  // Busca el objeto del post en nuestra base de datos local usando su ID
  const post = postsData[postId];
  
  // Si el ID buscado no existe en la base de datos, cancela la ejecución
  if (!post) return;

  // Inyecta la información correspondiente dentro de las etiquetas HTML seleccionadas
  articleTitle.textContent = post.title;     // Asigna el título como texto plano (Seguro contra XSS)
  articleDate.textContent = post.date;       // Asigna la fecha como texto plano
  articleContent.innerHTML = post.content;   // Inyecta el HTML interno (Párrafos, citas, etc.)

  // Alterna las clases para cambiar de vista visible
  feedView.classList.remove('active');       // Oculta el feed
  detailView.classList.add('active');        // Muestra la vista de lectura completa
  window.scrollTo({ top: 0, behavior: 'smooth' }); // Desplaza suavemente hacia arriba
}

// ==========================================================================
// REGISTRO DE EVENTOS (EVENT LISTENERS)
// ==========================================================================

// Asigna a cada tarjeta de publicación la capacidad de responder al clic
document.querySelectorAll('.post-card').forEach(card => {
  card.addEventListener('click', () => {
    // Lee el atributo HTML 'data-id' asignado en la tarjeta
    const postId = card.getAttribute('data-id');
    
    // Ejecuta la función para mostrar la vista detallada
    showArticle(postId);
    
    // Registra la nueva navegación en el historial del navegador sin recargar la página
    // Actualiza la URL agregando el hash (ejemplo: #post-1)
    history.pushState({ view: 'detail', id: postId }, '', `#post-${postId}`);
  });
});

// Asigna la función de regreso al hacer clic en el botón "Voltar às publicações"
backBtn.addEventListener('click', () => {
  showFeed(); // Muestra el feed principal
  // Limpia el hash de la URL guardando el estado en el historial del navegador
  history.pushState({ view: 'feed' }, '', window.location.pathname);
});

// Maneja la navegación nativa del usuario (Botones "Atrás" / "Adelante" del navegador)
window.addEventListener('popstate', (e) => {
  // Comprueba si el estado guardado al navegar indica una vista de detalle
  if (e.state && e.state.view === 'detail') {
    showArticle(e.state.id); // Si existe, vuelve a cargar el artículo que estaba en pantalla
  } else {
    showFeed(); // Si no hay estado o indica feed, muestra la lista principal
  }
});

// Controla la carga inicial de la página cuando el usuario entra desde una URL directa con hash
window.addEventListener('DOMContentLoaded', () => {
  const hash = window.location.hash; // Obtiene el hash de la dirección (Ejemplo: "#post-2")
  
  // Verifica si la URL contiene el patrón de enlace a un artículo
  if (hash.startsWith('#post-')) {
    const postId = hash.replace('#post-', ''); // Extrae únicamente el número o ID ("2")
    showArticle(postId); // Carga directamente la lectura de dicho post
  }
});