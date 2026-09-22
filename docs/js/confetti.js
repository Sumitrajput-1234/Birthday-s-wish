/* =========================================================
   confetti.js — lightweight canvas confetti (no deps)
   Confetti.burst(x, y, n)   — radial explosion at a point
   Confetti.rain(ms)         — celebratory rain from the top
   ========================================================= */
(function () {
  'use strict';

  var canvas, ctx, W, H, dpr;
  var parts = [];
  var raf = null;
  var running = false;

  var COLORS = ['#ff5c8a', '#ff8fab', '#ffb3c6', '#ffd166', '#f7b267', '#ffffff', '#f472b6', '#e0447c', '#a78bfa', '#7dd3fc'];

  function resize() {
    dpr = Math.min(window.devicePixelRatio || 1, 2);
    W = window.innerWidth;
    H = window.innerHeight;
    canvas.width = W * dpr;
    canvas.height = H * dpr;
    canvas.style.width = W + 'px';
    canvas.style.height = H + 'px';
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
  }

  function rand(a, b) { return a + Math.random() * (b - a); }

  function makePart(x, y, opts) {
    opts = opts || {};
    var ang = opts.angle !== undefined ? opts.angle : rand(0, Math.PI * 2);
    var sp = opts.speed !== undefined ? opts.speed : rand(2.5, 7.5);
    return {
      x: x, y: y,
      vx: Math.cos(ang) * sp + (opts.vx || 0),
      vy: Math.sin(ang) * sp + (opts.vy !== undefined ? opts.vy : rand(-5, -1)),
      g: rand(0.08, 0.16),
      size: rand(5, 11),
      rot: rand(0, Math.PI * 2),
      vr: rand(-0.2, 0.2),
      color: COLORS[(Math.random() * COLORS.length) | 0],
      shape: Math.random() < 0.22 ? 'heart' : (Math.random() < 0.5 ? 'rect' : 'circle'),
      life: 0,
      ttl: opts.ttl || rand(90, 160),
      flutter: rand(0, Math.PI * 2)
    };
  }

  function drawHeart(p) {
    var s = p.size * 0.62;
    ctx.beginPath();
    ctx.moveTo(p.x, p.y + s * 0.3);
    ctx.bezierCurveTo(p.x - s, p.y - s * 0.7, p.x - s * 0.5, p.y - s * 1.4, p.x, p.y - s * 0.5);
    ctx.bezierCurveTo(p.x + s * 0.5, p.y - s * 1.4, p.x + s, p.y - s * 0.7, p.x, p.y + s * 0.3);
    ctx.closePath();
    ctx.fill();
  }

  function tick() {
    ctx.clearRect(0, 0, W, H);
    for (var i = parts.length - 1; i >= 0; i--) {
      var p = parts[i];
      p.life++;
      p.vy += p.g;
      p.vx *= 0.985;
      p.vy *= 0.992;
      p.x += p.vx + Math.sin(p.flutter + p.life * 0.06) * 0.6;
      p.y += p.vy;
      p.rot += p.vr;
      var fade = 1;
      if (p.life > p.ttl - 30) fade = (p.ttl - p.life) / 30;
      if (p.life >= p.ttl || p.y > H + 30) { parts.splice(i, 1); continue; }

      ctx.save();
      ctx.globalAlpha = Math.max(0, fade);
      ctx.fillStyle = p.color;
      ctx.translate(p.x, p.y);
      ctx.rotate(p.rot);
      if (p.shape === 'rect') {
        ctx.scale(1, Math.sin(p.flutter + p.life * 0.15) * 0.7 + 0.3);
        ctx.fillRect(-p.size / 2, -p.size / 3, p.size, p.size * 0.66);
      } else if (p.shape === 'circle') {
        ctx.beginPath();
        ctx.arc(0, 0, p.size / 2, 0, Math.PI * 2);
        ctx.fill();
      } else {
        drawHeart(p);
      }
      ctx.restore();
    }
    if (parts.length > 0) {
      raf = requestAnimationFrame(tick);
    } else {
      running = false;
      ctx.clearRect(0, 0, W, H);
    }
  }

  function ensure() {
    if (!running) { running = true; raf = requestAnimationFrame(tick); }
  }

  function burst(x, y, n, opts) {
    for (var i = 0; i < (n || 60); i++) parts.push(makePart(x, y, opts));
    ensure();
  }

  function rain(ms) {
    var t0 = Date.now();
    (function drop() {
      if (Date.now() - t0 < (ms || 2500)) {
        for (var i = 0; i < 4; i++) {
          parts.push(makePart(rand(0, W), -20, {
            angle: Math.PI / 2 + rand(-0.35, 0.35),
            speed: rand(1, 3.2),
            vy: rand(1, 4)
          }));
        }
        ensure();
        setTimeout(drop, 90);
      }
    })();
  }

  function bigCelebration() {
    burst(W * 0.5, H * 0.35, 90);
    burst(W * 0.2, H * 0.5, 50);
    burst(W * 0.8, H * 0.5, 50);
    rain(3200);
  }

  window.addEventListener('resize', resize);

  window.Confetti = {
    burst: burst,
    rain: rain,
    big: bigCelebration,
    _init: function (el) {
      canvas = el;
      ctx = canvas.getContext('2d');
      resize();
    }
  };
})();
