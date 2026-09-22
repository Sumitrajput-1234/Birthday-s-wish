/* =========================================================
   audio.js — tiny WebAudio engine
   - Background: if docs/music/song.mp3 (or similar) exists,
     that MP3 plays (loop). Otherwise a soft original
     romantic instrumental (flute-style synth) plays.
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

  /* ---------------- optional MP3 support ---------------- */

  var MP3_CANDIDATES = [
    'music/song.mp3',
    'music/music.mp3',
    'music/o-sanam.mp3',
    'music/osanam.mp3'
  ];
  var mp3El = null;
  var mp3Active = false;

  (function findMp3() {
    var i = 0;
    (function tryNext() {
      if (i >= MP3_CANDIDATES.length) return;
      var url = MP3_CANDIDATES[i++];
      fetch(url, { method: 'HEAD' }).then(function (r) {
        if (r.ok) {
          mp3El = document.createElement('audio');
          mp3El.src = url;
          mp3El.loop = true;
          mp3El.preload = 'auto';
          mp3El.volume = 0.55;
          mp3Active = true;
        } else {
          tryNext();
        }
      }).catch(tryNext);
    })();
  })();

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

  /* ---------------- romantic instrumental (original) ---------------- */

  var N = {
    A3: 220.00, B3: 246.94, C4: 261.63, D4: 293.66, E4: 329.63,
    F4: 349.23, G4: 392.00, A4: 440.00, C5: 523.25, G5: 783.99, A5: 880.00
  };
  // gentle dreamy lead, [freq, beats] — 4 x 8-beat bars
  var MELODY = [
    [N.E4, 1], [N.G4, 1], [N.A4, 1.5], [N.G4, 0.5], [N.E4, 1], [N.D4, 1], [N.C4, 2],
    [N.D4, 1], [N.E4, 1], [N.F4, 1.5], [N.E4, 0.5], [N.D4, 1], [N.C4, 1], [N.A3, 2],
    [N.C4, 1], [N.D4, 1], [N.E4, 1.5], [N.D4, 0.5], [N.E4, 1], [N.G4, 1], [N.E4, 2],
    [N.D4, 1], [N.C4, 1.5], [N.B3, 0.5], [N.A3, 1], [N.C4, 1], [N.D4, 2], [0, 2]
  ];
  // soft backing pads, one chord per bar (8 beats)
  var CHORDS = [
    [220.00, 261.63, 329.63],  // Am
    [174.61, 220.00, 261.63],  // F
    [261.63, 329.63, 392.00],  // C
    [196.00, 246.94, 293.66]   // G
  ];
  var BEAT = 0.8;

  function note(freq, start, dur, dest, gainVal, type) {
    var o = ctx.createOscillator();
    var g = ctx.createGain();
    o.type = type || 'sine';
    o.frequency.value = freq;
    g.gain.setValueAtTime(0.0001, start);
    g.gain.linearRampToValueAtTime(gainVal, start + 0.07);
    g.gain.setValueAtTime(gainVal, start + dur * 0.55);
    g.gain.exponentialRampToValueAtTime(0.0001, start + dur * 0.98);
    o.connect(g);
    g.connect(dest);
    o.start(start);
    o.stop(start + dur + 0.1);
  }

  function padChord(freqs, start, dur) {
    freqs.forEach(function (f) {
      note(f, start, dur, musicGain, 0.03, 'sine');
    });
  }

  function scheduleMelody() {
    var t = ctx.currentTime + 0.1;
    var total = 0;
    MELODY.forEach(function (m) {
      var f = m[0], d = m[1] * BEAT;
      if (f > 0) {
        note(f, t + total, d * 1.08, musicGain, 0.16, 'sine');
        note(f * 2, t + total, d * 0.9, musicGain, 0.028, 'triangle'); // airy shimmer
      }
      total += d;
    });
    CHORDS.forEach(function (chord, i) {
      padChord(chord, t + i * 8 * BEAT, 8 * BEAT);
    });
    var loopMs = (total + 2.5) * 1000;
    musicTimer = setTimeout(scheduleMelody, loopMs);
    return loopMs;
  }

  function synthStart() {
    if (!ctx) return;
    musicGain.gain.cancelScheduledValues(ctx.currentTime);
    musicGain.gain.linearRampToValueAtTime(0.9, ctx.currentTime + 1.6);
    scheduleMelody();
  }

  function startMusic() {
    if (musicStarted) return;
    musicStarted = true;
    if (mp3Active && mp3El) {
      if (musicOn) {
        var p = mp3El.play();
        if (p && p.catch) p.catch(synthStart);
      }
      return;
    }
    ensureCtx();
    if (musicOn) synthStart();
  }

  function setMusic(on) {
    musicOn = on;
    if (musicStarted && mp3Active && mp3El) {
      if (on) {
        var p = mp3El.play();
        if (p && p.catch) p.catch(function () {});
      } else {
        mp3El.pause();
      }
      return;
    }
    var c = ensureCtx();
    if (!c) return;
    if (on && !musicStarted) { startMusic(); return; }
    if (on) {
      musicGain.gain.cancelScheduledValues(c.currentTime);
      musicGain.gain.linearRampToValueAtTime(0.9, c.currentTime + 0.8);
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
