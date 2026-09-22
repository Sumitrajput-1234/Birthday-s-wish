/* =========================================================
   audio.js — tiny WebAudio engine
   - "Happy Birthday" melody (synth, loops gently)
   - SFX: balloon pop, whoosh, sparkle chime, ding
   ========================================================= */
(function () {
  'use strict';

  var ctx = null;
  var master = null;
  var musicGain = null;
  var musicOn = true;
  var musicTimer = null;
  var musicStarted = false;

  function ensureCtx() {
    if (!ctx) {
      var AC = window.AudioContext || window.webkitAudioContext;
      if (!AC) return null;
      ctx = new AC();
      master = ctx.createGain();
      master.gain.value = 0.9;
      master.connect(ctx.destination);
      musicGain = ctx.createGain();
      musicGain.gain.value = 0.0;
      musicGain.connect(master);
    }
    if (ctx.state === 'suspended') ctx.resume();
    return ctx;
  }

  /* ---------------- music: happy birthday ---------------- */

  var N = {
    G4: 392.00, A4: 440.00, B4: 493.88, C5: 523.25, D5: 587.33,
    E5: 659.25, F5: 698.46, G5: 783.99, A5: 880.00
  };
  // [freq, beats]  (beat = 0.46s)
  var MELODY = [
    [N.G4, 0.75], [N.G4, 0.25], [N.A4, 1], [N.G4, 1], [N.C5, 1], [N.B4, 2], [0, 1],
    [N.G4, 0.75], [N.G4, 0.25], [N.A4, 1], [N.G4, 1], [N.D5, 1], [N.C5, 2], [0, 1],
    [N.G4, 0.75], [N.G4, 0.25], [N.G5, 1], [N.E5, 1], [N.C5, 1], [N.B4, 1], [N.A4, 3], [0, 1],
    [N.F5, 0.75], [N.F5, 0.25], [N.E5, 1], [N.C5, 1], [N.D5, 1], [N.C5, 3], [0, 2]
  ];
  var BEAT = 0.46;

  function note(freq, start, dur, dest, gainVal, type) {
    var o = ctx.createOscillator();
    var g = ctx.createGain();
    o.type = type || 'triangle';
    o.frequency.value = freq;
    g.gain.setValueAtTime(0.0001, start);
    g.gain.linearRampToValueAtTime(gainVal, start + 0.04);
    g.gain.exponentialRampToValueAtTime(0.0001, start + dur * 0.92);
    o.connect(g);
    g.connect(dest);
    o.start(start);
    o.stop(start + dur + 0.05);
  }

  function padChord(freqs, start, dur) {
    freqs.forEach(function (f) {
      note(f, start, dur, musicGain, 0.028, 'sine');
    });
  }

  function scheduleMelody() {
    var t = ctx.currentTime + 0.1;
    var total = 0;
    MELODY.forEach(function (m, i) {
      var f = m[0], b = m[1], d = b * BEAT;
      if (f > 0) {
        note(f, t + total, d * 1.05, musicGain, 0.16, 'triangle');
        note(f * 2, t + total, d * 0.9, musicGain, 0.045, 'sine'); // shimmer
      }
      total += d;
    });
    // soft backing: C - G - Am - F-ish pads
    padChord([261.63, 329.63, 392.00], t, total * 0.5);
    padChord([196.00, 246.94, 392.00], t + total * 0.5, total * 0.5);
    var loopMs = (total + 2.2) * 1000;
    musicTimer = setTimeout(scheduleMelody, loopMs);
    return loopMs;
  }

  function startMusic() {
    var c = ensureCtx();
    if (!c || musicStarted) return;
    musicStarted = true;
    if (musicOn) {
      musicGain.gain.cancelScheduledValues(c.currentTime);
      musicGain.gain.linearRampToValueAtTime(0.85, c.currentTime + 1.4);
      scheduleMelody();
    }
  }

  function setMusic(on) {
    musicOn = on;
    var c = ensureCtx();
    if (!c) return;
    if (on && !musicStarted) { startMusic(); return; }
    if (on) {
      musicGain.gain.cancelScheduledValues(c.currentTime);
      musicGain.gain.linearRampToValueAtTime(0.85, c.currentTime + 0.8);
      if (!musicTimer) scheduleMelody();
    } else if (musicStarted) {
      musicGain.gain.cancelScheduledValues(c.currentTime);
      musicGain.gain.linearRampToValueAtTime(0.0001, c.currentTime + 0.5);
      if (musicTimer) { clearTimeout(musicTimer); musicTimer = null; }
    }
  }

  /* ---------------- SFX ---------------- */

  function blip(freq, dur, type, gainVal, when) {
    var c = ensureCtx();
    if (!c) return;
    var t = c.currentTime + (when || 0);
    note(freq, t, dur || 0.12, master, gainVal || 0.2, type || 'sine');
  }

  function pop() {
    var c = ensureCtx();
    if (!c) return;
    var t = c.currentTime;
    // short noise burst
    var len = 0.07;
    var buf = ctx.createBuffer(1, ctx.sampleRate * len, ctx.sampleRate);
    var d = buf.getChannelData(0);
    for (var i = 0; i < d.length; i++) d[i] = (Math.random() * 2 - 1) * (1 - i / d.length);
    var src = ctx.createBufferSource();
    src.buffer = buf;
    var f = ctx.createBiquadFilter();
    f.type = 'bandpass';
    f.frequency.value = 1600;
    f.Q.value = 0.8;
    var g = ctx.createGain();
    g.gain.setValueAtTime(0.5, t);
    g.gain.exponentialRampToValueAtTime(0.001, t + len);
    src.connect(f); f.connect(g); g.connect(master);
    src.start(t);
    blip(660 + Math.random() * 220, 0.09, 'triangle', 0.18);
  }

  function whoosh() {
    var c = ensureCtx();
    if (!c) return;
    var t = c.currentTime;
    var len = 0.7;
    var buf = c.createBuffer(1, c.sampleRate * len, c.sampleRate);
    var d = buf.getChannelData(0);
    for (var i = 0; i < d.length; i++) d[i] = (Math.random() * 2 - 1) * Math.sin(Math.PI * i / d.length);
    var src = c.createBufferSource();
    src.buffer = buf;
    var f = c.createBiquadFilter();
    f.type = 'lowpass';
    f.frequency.setValueAtTime(400, t);
    f.frequency.exponentialRampToValueAtTime(2200, t + 0.5);
    var g = c.createGain();
    g.gain.setValueAtTime(0.32, t);
    g.gain.exponentialRampToValueAtTime(0.001, t + len);
    src.connect(f); f.connect(g); g.connect(master);
    src.start(t);
  }

  function chime() {
    [523.25, 659.25, 783.99, 1046.5].forEach(function (f, i) {
      blip(f, 0.5, 'sine', 0.14, i * 0.09);
    });
  }

  function ding() {
    blip(880, 0.3, 'sine', 0.2);
    blip(1318.5, 0.4, 'sine', 0.12, 0.05);
  }

  // expose context so the mic detector can share it
  window.__getAudioCtx = function () { return ensureCtx(); };

  window.Sound = {
    start: startMusic,
    setMusic: setMusic,
    isOn: function () { return musicOn; },
    pop: pop,
    whoosh: whoosh,
    chime: chime,
    ding: ding
  };
})();
