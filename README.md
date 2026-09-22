# 💝 Muskan's Birthday Surprise — Deploy Guide (2 minute ka kaam)

Ye interactive birthday card hai — exactly reel wali HeartCraft style:
**gift open → balloons pop → candles blow out (mic se!) → cake cut → photos → love letter → finale**

Ye folder me kya-kya hai:

```
muskan-birthday/
├── docs/                 ← ye POORA website hai (GitHub Pages isse host karega)
│   ├── index.html
│   ├── css/style.css
│   ├── js/app.js  audio.js  confetti.js
│   └── photos/  (3 photos)
└── .github/
    └── workflows/deploy.yml   ← GitHub Actions deploy file (zaroori hai!)
```

## Step 1 — Files repo me daalo (Robocopy)

Zip extract karo (e.g. `D:\` pe). Phir **Command Prompt** (normal, admin nahi chahiye) kholo
aur in 2 commands chalao. **Apne folder paths ke hisaab se D:\... badal lena:**

```bat
robocopy D:\muskan-birthday\docs D:\Birthday-s-wish\docs /E
robocopy D:\muskan-birthday\.github D:\Birthday-s-wish\.github /E
```

> Tip: `D:\Birthday-s-wish` = tumhari repo ka local folder (jo git clone se aaya hai).
> `.github` ek hidden folder hai — robocopy ise bhi copy karega, tension mat lo.

## Step 2 — Push karo

```bat
cd /d D:\Birthday-s-wish
git add .
git commit -m "Muskan's interactive birthday surprise"
git push
```

## Step 3 — GitHub Pages ON karo (ek baar ka kaam)

1. Browser me jao: `https://github.com/Sumitrajput-1234/Birthday-s-wish`
2. Upar **Settings** tab → left menu me **Pages**
3. "Build and deployment" → **Source** me: **GitHub Actions** select karo → Done
4. Kuch nahi karna — push hote hi workflow khud chal jayega.
   (Actions tab me dekh sakte ho, ~1 min me green ✔ aayega)

## Step 4 — Link leke Muskan ko surprise karo 🎉

```
https://sumitrajput-1234.github.io/Birthday-s-wish/
```

Link WhatsApp/Instagram pe bhejo. Wo phone pe kholegi — app install nahi, login nahi,
bas ek tap. Candles ke scene me wo **mic me hawa degi** aur candles bujh jayengi. 💨

## Notes

- Music + saare sounds code me hi bane hain (koi file nahi) — "Happy Birthday" melody
  gift open hote hi shuru hogi. Top-right 🎵 se mute kar sakti hai.
- Agar link kaas na aaye toh: Settings → Pages me "GitHub Actions" select hua hai ya nahi
  check karo — ye sabse aam galti hai.
- Koi cheez change karni ho (naam, letter, photos) toh `docs/index.html` aur
  `docs/js/app.js` (upar CONFIG me) edit karke dobara push kar dena.
