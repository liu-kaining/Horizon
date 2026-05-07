(function () {
  'use strict';

  /** Replace ⭐️ N/10 with a colored badge in h2, h3, and li elements */
  function processScoreBadges() {
    var scoreRe = /⭐️\s*(\d+(?:\.\d+)?)\/10/;
    var targets = document.querySelectorAll('.main-content h2, .main-content h3, .main-content li');
    targets.forEach(function (el) {
      var m = el.innerHTML.match(scoreRe);
      if (!m) return;
      var score = parseFloat(m[1]);
      var tier;
      if (score >= 9) tier = 'high';
      else if (score >= 7) tier = 'good';
      else if (score >= 5) tier = 'mid';
      else tier = 'low';
      el.innerHTML = el.innerHTML.replace(
        scoreRe,
        '<span class="score-badge" data-tier="' + tier + '">' + m[1] + '</span>'
      );
    });
  }

  /** Add semantic classes to tag lines, source lines, and background paragraphs */
  function markSemanticElements() {
    var paragraphs = document.querySelectorAll('.main-content p');
    paragraphs.forEach(function (p) {
      var text = p.textContent.trim();

      // Tag line: starts with Tags or 标签 (bold prefix rendered by Markdown)
      if (/^(Tags|标签)\s*:/.test(text)) {
        p.classList.add('tag-line');
        return;
      }

      // Source line: pattern like "source · site · date"
      if (/^(rss|reddit|github|hackernews|hn|telegram)\s*·/i.test(text)) {
        p.classList.add('source-line');
        return;
      }
    });
  }

  /** Set up EN/中文 language toggle as a page-level control */
  function setupLanguageToggle() {
    // Create toggle buttons
    var toggle = document.createElement('div');
    toggle.className = 'lang-toggle';

    var btnEn = document.createElement('button');
    btnEn.textContent = 'EN';
    btnEn.type = 'button';

    var btnZh = document.createElement('button');
    btnZh.textContent = '中文';
    btnZh.type = 'button';

    toggle.appendChild(btnEn);
    toggle.appendChild(btnZh);

    // Insert at top of body
    document.body.insertBefore(toggle, document.body.firstChild);

    // Read saved preference, default to zh
    var saved = null;
    try { saved = localStorage.getItem('horizon-lang'); } catch (e) { /* noop */ }
    var currentLang = saved === 'en' ? 'en' : 'zh';

    function updateButtons(lang) {
      if (lang === 'en') {
        btnEn.classList.add('active');
        btnZh.classList.remove('active');
      } else {
        btnZh.classList.add('active');
        btnEn.classList.remove('active');
      }
    }

    // Index page: toggle lang-section visibility
    var zhSection = document.getElementById('lang-zh');
    var enSection = document.getElementById('lang-en');

    function showSection(lang) {
      if (!zhSection || !enSection) return;
      if (lang === 'en') {
        enSection.classList.remove('hidden');
        zhSection.classList.add('hidden');
      } else {
        zhSection.classList.remove('hidden');
        enSection.classList.add('hidden');
      }
    }

    // Article page: redirect to the other language version
    function switchArticleLang(lang) {
      var path = window.location.pathname;
      var target = null;
      if (lang === 'en' && /-zh(?:\.html)?$/.test(path.replace(/\/$/, ''))) {
        target = path.replace(/-zh(\.html)?$/, '-en$1').replace(/-zh\/$/, '-en/');
      } else if (lang === 'zh' && /-en(?:\.html)?$/.test(path.replace(/\/$/, ''))) {
        target = path.replace(/-en(\.html)?$/, '-zh$1').replace(/-en\/$/, '-zh/');
      }
      if (target) window.location.href = target;
    }

    function setLang(lang) {
      currentLang = lang;
      updateButtons(lang);
      try { localStorage.setItem('horizon-lang', lang); } catch (e) { /* noop */ }
      if (zhSection && enSection) {
        showSection(lang);
      } else {
        switchArticleLang(lang);
      }
    }

    btnEn.addEventListener('click', function () { setLang('en'); });
    btnZh.addEventListener('click', function () { setLang('zh'); });

    // Initialize
    updateButtons(currentLang);
    if (zhSection && enSection) {
      showSection(currentLang);
    }
  }

  /** Home page: lightweight search over generated index */
  function setupHomeSearch() {
    var zhInput = document.getElementById('hz-search-input-zh');
    var enInput = document.getElementById('hz-search-input-en');
    var zhOut = document.getElementById('hz-search-results-zh');
    var enOut = document.getElementById('hz-search-results-en');
    if (!zhInput && !enInput) return; // not on home

    function esc(s) {
      return String(s)
        .replace(/&/g, '&amp;')
        .replace(/</g, '&lt;')
        .replace(/>/g, '&gt;')
        .replace(/"/g, '&quot;')
        .replace(/'/g, '&#039;');
    }

    function normalize(s) {
      return String(s || '').toLowerCase().trim();
    }

    function parseQuery(q) {
      q = normalize(q);
      if (!q) return { text: '', tags: [] };
      var tags = [];
      q.split(/\s+/).forEach(function (tok) {
        if (tok[0] === '#') tags.push(tok.slice(1));
      });
      return { text: q.replace(/#[^\s]+/g, '').trim(), tags: tags };
    }

    var index = null;
    var indexPromise = null;

    function loadIndex() {
      if (indexPromise) return indexPromise;
      var url = (window.HORIZON_BASEURL || '') + '/assets/search-index.json';
      indexPromise = fetch(url, { cache: 'no-store' })
        .then(function (r) { return r.ok ? r.json() : []; })
        .then(function (j) { index = Array.isArray(j) ? j : []; return index; })
        .catch(function () { index = []; return index; });
      return indexPromise;
    }

    function render(outEl, items, q) {
      if (!outEl) return;
      if (!q) { outEl.innerHTML = ''; return; }
      if (!items.length) {
        outEl.innerHTML = '<div class="meta">No matches.</div>';
        return;
      }
      var html = '<ul>';
      items.slice(0, 12).forEach(function (it) {
        var tags = (it.tags || []).map(function (t) { return '<code>#' + esc(t) + '</code>'; }).join(' ');
        var meta = esc(it.digest_date || '') + (it.score != null ? (' · ⭐️ ' + esc(it.score) + '/10') : '');
        html += '<li><a href="' + esc(it.digest_url) + '">' + esc(it.title) + '</a>'
          + '<div class="meta">' + meta + (tags ? (' · ' + tags) : '') + '</div></li>';
      });
      html += '</ul>';
      outEl.innerHTML = html;
    }

    function search(lang, q, outEl) {
      var parsed = parseQuery(q);
      if (!parsed.text && !parsed.tags.length) { render(outEl, [], ''); return; }
      loadIndex().then(function () {
        var text = parsed.text;
        var tags = parsed.tags.map(normalize);
        var res = (index || []).filter(function (it) {
          if (lang && it.lang && it.lang !== lang) return false;
          var hay = normalize(it.title) + ' ' + normalize((it.tags || []).join(' '));
          if (text && hay.indexOf(text) === -1) return false;
          if (tags.length) {
            var itTags = (it.tags || []).map(normalize);
            for (var i = 0; i < tags.length; i++) {
              if (itTags.indexOf(tags[i]) === -1) return false;
            }
          }
          return true;
        });
        render(outEl, res, q);
      });
    }

    function debounce(fn, ms) {
      var t = null;
      return function () {
        var args = arguments;
        clearTimeout(t);
        t = setTimeout(function () { fn.apply(null, args); }, ms);
      };
    }

    var onZh = debounce(function (e) { search('zh', e.target.value, zhOut); }, 120);
    var onEn = debounce(function (e) { search('en', e.target.value, enOut); }, 120);

    if (zhInput) {
      zhInput.addEventListener('input', onZh);
      zhInput.addEventListener('focus', function () { loadIndex(); });
    }
    if (enInput) {
      enInput.addEventListener('input', onEn);
      enInput.addEventListener('focus', function () { loadIndex(); });
    }
  }

  document.addEventListener('DOMContentLoaded', function () {
    processScoreBadges();
    markSemanticElements();
    setupLanguageToggle();
    setupHomeSearch();
  });
})();
