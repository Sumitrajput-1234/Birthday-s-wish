/* =========================================================
   app.js — Muskan's birthday surprise
   Scene flow:
   intro → balloons → candles (blow out) → cut cake → photos → letter → finale
   ========================================================= */
(function () {
  'use strict';

  /* ---------------- config ---------------- */

  var CONFIG = {
    name: 'Muskan',
    balloons: 9,
    candles: 5,
    photos: [
      { src: 'photos/photo1.jpg', caption: 'that smile I never get tired of' },
      { src: 'photos/photo2.jpg', caption: 'you, in your quiet beautiful moments' },
      { src: 'photos/photo3.jpg', caption: 'my favourite person, always' }
    ],
    letter: [
      'Dear Muskan,',
      '',
      'Happy birthday to the love of my life! Every moment with you feels like a dream come true. You light up my world with your laugh, your love, and your beautiful soul.',
      '',
      "I didn't know what I was missing until I met you. You make my life warmer and a thousand times happier.",
      '',
      "As you blow out your candles, know that you aren't just making a wish — you already fulfilled all of mine.",
      '',
      'Have the best day, birthday girl. Today is all about you, because so is my heart.',
      '',
      'Forever yours ♥'
    ].join('\n')
  };

  /* ---------------- scene manager ---------------- */

  var scenes = ['intro', 'balloons', 'candles', 'cut', 'photos', 'letter', 'finale'];
  var current = 'intro';
  var stage = document.getElementById('stage');
  var state = { popped: 0, total: 0, candlesLit: 0, candlesDone: false, micStream: null };

  function show(id) {
    if (id === current) return;
    current = id;
    scenes.forEach(function (s) {
      document.getElementById('scene-' + s).classList.toggle('active', s === id);
    });
    var enter = ENTERS[id];
    if (enter) enter();
  }

  /* ---------------- floating hearts backdrop ---------------- */

  (function hearts() {
    var box = document.getElementById('hearts');
    var glyphs = ['💗', '💖', '🤍', '', '🩷'];
    for (var i = 0; i < 14; i++) {
      var h = document.createElement('span');
      h.className = 'heart-f';
      h.textContent = glyphs[i % glyphs.length];
      h.style.left = Math.random() * 100 + 'vw';
      h.style.fontSize = (12 + Math.random() * 22) + 'px';
      h.style.setProperty('--o', (0.25 + Math.random() * 0.4).toFixed(2));
      h.style.setProperty('--sway', (Math.random() * 90 - 45) + 'px');
      var dur = 9 + Math.random() * 10;
      h.style.animationDuration = dur + 's';
      h.style.animationDelay = (-Math.random() * dur) + 's';
      box.appendChild(h);
    }
  })();

  /* ---------------- music toggle ---------------- */

  var musicBtn = document.getElementById('musicToggle');
  musicBtn.addEventListener('click', function () {
    Sound.setMusic(!Sound.isOn());
    musicBtn.classList.toggle('off', !Sound.isOn());
    if (Sound.isOn()) musicBtn.animate(
      [{ transform: 'scale(1)' }, { transform: 'scale(1.25)' }, { transform: 'scale(1)' }],
      { duration: 250 }
    );
  });

  /* =========================================================
     SCENE 0 — INTRO / GIFT
     ========================================================= */

  var ENTERS = {};

  ENTERS.intro = function () { /* animations already playing */ };

  function openGift() {
    var gift = document.getElementById('giftBox');
    if (gift.classList.contains('opened')) return;
    gift.classList.add('opened');
    Sound.start();
    Sound.pop();
    setTimeout(function () { Sound.chime(); }, 300);
    setTimeout(function () {
      Confetti.burst(window.innerWidth / 2, window.innerHeight * 0.42, 70);
      show('balloons');
    }, 700);
  }

  document.getElementById('giftBox')
    .addEventListener('click', openGift);
  document.getElementById('giftBox')
    .addEventListener('keydown', function (e) {
      if (e.key === 'Enter' || e.key === ' ') openGift();
    });

  /* =========================================================
     SCENE 1 — BALLOONS
     ========================================================= */

  var BALLOON_COLORS = ['#ff5c8a', '#ffb3c6', '#ffd166', '#a78bfa', '#7dd3fc', '#f472b6', '#5eead4', '#f7b267', '#e0447c'];

  function buildBalloons() {
    var field = document.getElementById('balloonField');
    field.innerHTML = '';
    state.popped = 0;
    state.total = CONFIG.balloons;
    updateCounter();

    var fh = field.offsetHeight || 400;
    for (var i = 0; i < state.total; i++) {
      var b = document.createElement('div');
      b.className = 'balloon';
      b.style.left = (6 + Math.random() * 84) + '%';
      b.style.setProperty('--c', BALLOON_COLORS[i % BALLOON_COLORS.length]);
      b.style.setProperty('--sw', (Math.random() * 50 - 25) + 'px');
      var dur = 8 + Math.random() * 6;
      b.style.setProperty('--dur', dur + 's');
      b.style.animationDelay = (-Math.random() * dur) + 's';
      b.innerHTML = '<div class="b-body"></div><div class="b-knot"></div><div class="b-string"></div>';

      (function (el) {
        el.addEventListener('pointerdown', function (e) {
          e.preventDefault();
          popBalloon(el);
        });
      })(b);
      field.appendChild(b);
    }
  }

  function popBalloon(el) {
    if (el.classList.contains('popped')) return;
    el.classList.add('popped');
    el.style.animationPlayState = 'paused';
    var r = el.getBoundingClientRect();
    Confetti.burst(r.left + r.width / 2, r.top + r.height / 2, 26, { ttl: 55 });
    Sound.pop();

    // little star flies
    var star = document.createElement('span');
    star.className = 'pop-star';
    star.textContent = Math.random() < 0.5 ? '✨' : '💥';
    star.style.left = (r.left + r.width / 2 - 10) + 'px';
    star.style.top = (r.top + r.height / 3) + 'px';
    star.style.position = 'fixed';
    star.style.setProperty('--dx', (Math.random() * 80 - 40) + 'px');
    star.style.setProperty('--dy', (-40 - Math.random() * 50) + 'px');
    document.body.appendChild(star);
    setTimeout(function () { star.remove(); }, 550);

    state.popped++;
    updateCounter();
    if (state.popped >= state.total) {
      setTimeout(function () {
        Confetti.big();
        Sound.chime();
        // send leftovers up
        document.querySelectorAll('.balloon:not(.popped)').forEach(function (x) {
          x.classList.add('balloon-leave');
        });
        setTimeout(function () { show('candles'); }, 1100);
      }, 350);
    }
  }

  function updateCounter() {
    var c = document.getElementById('balloonCounter');
    c.textContent = state.popped + ' / ' + state.total + ' popped';
    c.style.color = state.popped >= state.total ? 'var(--rose-500)' : '';
  }

  ENTERS.balloons = buildBalloons;

  /* =========================================================
     SCENE 2 — CANDLE BLOW
     ========================================================= */

  function buildCandles() {
    var row = document.getElementById('candlesRow');
    row.innerHTML = '';
    state.candlesLit = CONFIG.candles;
    state.candlesDone = false;
    state.micStream = null;

    // clean up the "Cut the cake" button from a previous run
    var actions = document.getElementById('candleActions');
    Array.prototype.slice.call(actions.querySelectorAll('button:not(#micBtn)')).forEach(function (b) {
      b.remove();
    });

    var colors = ['#ff9ec3', '#a78bfa', '#7dd3fc', '#ffd166', '#5eead4'];
    for (var i = 0; i < CONFIG.candles; i++) {
      var c = document.createElement('div');
      c.className = 'candle';
      c.style.setProperty('--cc', colors[i % colors.length]);
      c.innerHTML = '<div class="smoke"></div><div class="flame"></div><div class="wick"></div>';
      (function (el) {
        el.querySelector('.flame').addEventListener('pointerdown', function (e) {
          e.preventDefault();
          blowCandle(el);
        });
      })(c);
      row.appendChild(c);
    }

    var status = document.getElementById('micStatus');
    status.textContent = '';
    status.classList.remove('listening');
    document.getElementById('micBtn').disabled = false;
    document.getElementById('micBtn').style.display = '';
  }

  function blowCandle(el) {
    if (el.classList.contains('out') || state.candlesDone) return;
    el.classList.add('out');
    state.candlesLit--;
    Sound.whoosh();
    if (state.candlesLit <= 0) allCandlesOut();
  }

  function blowAll() {
    var candles = Array.prototype.slice.call(document.querySelectorAll('.candle:not(.out)'));
    candles.sort(function () { return Math.random() - 0.5; });
    state.candlesDone = true;
    stopMic();
    var i = 0;
    (function next() {
      if (i >= candles.length) { allCandlesOut(); return; }
      var el = candles[i++];
      el.classList.add('out');
      Sound.whoosh();
      setTimeout(next, 140);
    })();
  }

  function allCandlesOut() {
    state.candlesDone = true;
    stopMic();
    setTimeout(function () {
      Confetti.big();
      Sound.chime();
      var status = document.getElementById('micStatus');
      status.textContent = '🌟 Wish made! So close to the cake now…';
      status.classList.remove('listening');
      document.getElementById('micBtn').style.display = 'none';
      var btn = document.createElement('button');
      btn.className = 'btn btn-primary';
      btn.textContent = 'Cut the cake →';
      btn.style.marginTop = '12px';
      btn.addEventListener('click', function () {
        Sound.ding();
        show('cut');
      });
      document.getElementById('candleActions').appendChild(btn);
    }, 650);
  }

  /* ----- microphone blow detection ----- */

  var micAnalyser = null, micData = null, micLevelTimer = null, micHotTime = 0;

  function startMic() {
    var status = document.getElementById('micStatus');
    if (!navigator.mediaDevices || !navigator.mediaDevices.getUserMedia) {
      status.textContent = 'Mic not available here — just tap the flames!';
      return;
    }
    status.textContent = 'asking for microphone…';
    navigator.mediaDevices.getUserMedia({ audio: true }).then(function (stream) {
      state.micStream = stream;
      var c = ensureAudioForMic();
      if (!c) return;
      var src = c.createMediaStreamSource(stream);
      micAnalyser = c.createAnalyser();
      micAnalyser.fftSize = 512;
      micData = new Uint8Array(micAnalyser.frequencyBinCount);
      src.connect(micAnalyser);
      status.textContent = 'listening… now blow hard! 💨';
      status.classList.add('listening');
      micHotTime = 0;
      clearInterval(micLevelTimer);
      micLevelTimer = setInterval(function () {
        if (state.candlesDone) { stopMic(); return; }
        micAnalyser.getByteFrequencyData(micData);
        var sum = 0;
        for (var i = 2; i < 40; i++) sum += micData[i]; // low mids = breath
        var avg = sum / (38 * 255);
        if (avg > 0.16) {
          micHotTime += 60;
          if (micHotTime > 550) {
            clearInterval(micLevelTimer);
            status.textContent = '💨 yes! that\u2019s it!';
            blowAll();
          }
        } else if (micHotTime > 0) {
          micHotTime = Math.max(0, micHotTime - 30);
        }
      }, 60);
    }).catch(function () {
      status.textContent = 'No mic permission — no worries, tap each flame!';
      status.classList.remove('listening');
    });
  }

  // share the audio engine's context with the mic analyser
  function ensureAudioForMic() {
    return window.__getAudioCtx ? window.__getAudioCtx() : null;
  }

  function stopMic() {
    clearInterval(micLevelTimer);
    if (state.micStream) {
      state.micStream.getTracks().forEach(function (t) { t.stop(); });
      state.micStream = null;
    }
  }

  document.getElementById('micBtn').addEventListener('click', startMic);

  ENTERS.candles = buildCandles;

  /* =========================================================
     SCENE 3 — CUT CAKE
     ========================================================= */

  ENTERS.cut = function () {
    var cake = document.getElementById('cakeCut');
    var knife = document.getElementById('knife');
    cake.classList.remove('cutting');
    knife.classList.remove('sweep');
    var btn = document.getElementById('cutBtn');
    btn.disabled = false;
    btn.textContent = '🔪 Tap to cut';
  };

  document.getElementById('cutBtn').addEventListener('click', function () {
    var btn = this;
    btn.disabled = true;
    btn.textContent = 'happy birthday! 🎉';
    var knife = document.getElementById('knife');
    knife.classList.add('sweep');
    Sound.whoosh();
    setTimeout(function () {
      document.getElementById('cakeCut').classList.add('cutting');
      Sound.ding();
      Confetti.burst(window.innerWidth / 2, window.innerHeight * 0.5, 55);
    }, 550);
    setTimeout(function () { show('photos'); }, 2600);
  });

  /* =========================================================
     SCENE 4 — PHOTOS
     ========================================================= */

  var photoIdx = 0;

  function renderPhoto(animate) {
    var p = CONFIG.photos[photoIdx];
    var imgWrap = document.getElementById('photoImg');
    var frame = imgWrap.parentElement;
    var cap = document.getElementById('photoCaption');
    cap.style.opacity = 0;
    if (animate) frame.classList.remove('swap');
    setTimeout(function () {
      imgWrap.innerHTML = '<img src="' + p.src + '" alt="Muskan" />';
      frame.classList.add('swap');
      cap.textContent = '“' + p.caption + '”';
      cap.style.opacity = 1;
    }, animate ? 180 : 0);

    var dots = document.getElementById('photoDots');
    dots.innerHTML = '';
    CONFIG.photos.forEach(function (_, i) {
      var d = document.createElement('span');
      if (i === photoIdx) d.className = 'on';
      dots.appendChild(d);
    });
  }

  function nextPhoto() {
    if (photoIdx >= CONFIG.photos.length - 1) { show('letter'); return; }
    photoIdx++;
    renderPhoto(true);
    Sound.ding();
  }

  ENTERS.photos = function () {
    photoIdx = 0;
    renderPhoto(false);
  };

  document.getElementById('photoStage').addEventListener('click', nextPhoto);
  document.getElementById('photosNext').addEventListener('click', function () {
    Sound.chime();
    show('letter');
  });

  /* =========================================================
     SCENE 5 — LETTER (typewriter)
     ========================================================= */

  var typerTimer = null;

  ENTERS.letter = function () {
    var env = document.getElementById('envelope');
    env.classList.remove('open');
    var body = document.getElementById('letterBody');
    body.textContent = '';
    // remove the continue button left over from a previous run
    var oldActions = document.querySelector('#scene-letter .scene-actions');
    if (oldActions) oldActions.remove();
    // open after a beat, then type
    setTimeout(function () {
      env.classList.add('open');
      Sound.pop();
      setTimeout(startTyping, 900);
    }, 400);
  };

  function startTyping() {
    var body = document.getElementById('letterBody');
    var text = CONFIG.letter;
    var i = 0;
    clearInterval(typerTimer);
    typerTimer = setInterval(function () {
      i += 1 + (Math.random() < 0.25 ? 1 : 0);
      body.textContent = text.slice(0, i);
      var paper = body.closest('.letter-paper');
      if (paper) paper.scrollTop = paper.scrollHeight;
      if (i >= text.length) clearInterval(typerTimer);
    }, 34);
  }

  document.getElementById('envelope').addEventListener('click', function () {
    var env = this;
    if (!env.classList.contains('open')) {
      env.classList.add('open');
      Sound.pop();
      setTimeout(function () {
        if (document.getElementById('letterBody').textContent.length === 0) startTyping();
      }, 900);
    } else {
      // already open → jump to finale
      show('finale');
    }
  });

  // small "continue" button appears when the letter finishes typing
  var letterDoneAdded = false;
  (function loop() {
    requestAnimationFrame(loop);
    if (current !== 'letter') { letterDoneAdded = false; return; }
    if (letterDoneAdded) return;
    var body = document.getElementById('letterBody');
    if (body.textContent.length < CONFIG.letter.length - 2) return;
    letterDoneAdded = true;
    setTimeout(function () {
      var scene = document.getElementById('scene-letter');
      var actions = scene.querySelector('.scene-actions');
      if (!actions) {
        actions = document.createElement('div');
        actions.className = 'scene-actions';
        scene.appendChild(actions);
      }
      if (!actions.querySelector('button')) {
        var btn = document.createElement('button');
        btn.className = 'btn btn-primary';
        btn.textContent = 'One more thing... 🎂';
        btn.addEventListener('click', function () { show('finale'); });
        actions.appendChild(btn);
      }
    }, 450);
  })();

  /* =========================================================
     SCENE 6 — FINALE
     ========================================================= */

  ENTERS.finale = function () {
    Confetti.big();
    Sound.chime();
    var emojis = ['🎂', '', '', '💝', '✨', '🥳'];
    var el = document.getElementById('finaleEmoji');
    var i = 0;
    clearInterval(el._t);
    el._t = setInterval(function () {
      i = (i + 1) % emojis.length;
      el.textContent = emojis[i];
    }, 1400);
  };

  document.getElementById('replayBtn').addEventListener('click', function () {
    Sound.ding();
    // reset everything and restart from intro
    stopMic();
    clearInterval(typerTimer);
    show('intro');
    var gift = document.getElementById('giftBox');
    gift.classList.remove('opened');
    // re-enable intro fade animations
    document.querySelectorAll('#scene-intro .fade-up').forEach(function (f) {
      f.style.animation = 'none';
      f.offsetHeight; // reflow
      f.style.animation = '';
    });
  });

  /* ---------------- boot ---------------- */

  Confetti._init(document.getElementById('confetti'));
  show('intro');
})();
