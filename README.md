# imasenhf.github.io

Personal research homepage for Haifeng Wu (IMASEN), published as a static GitHub Pages site.

## Structure

```text
.
├── index.html
├── assets/
│   ├── css/
│   │   └── style.css
│   └── images/
├── favicon.ico
├── CNAME
└── README.md
```

The site uses semantic HTML and a standalone CSS file. It has no build step and no external front-end dependencies. Local resources use relative paths so the site can be served from the repository root or a project subpath.

## Local preview

From the repository root:

```powershell
python -m http.server 8000
```

Open <http://localhost:8000/> in a browser. Stop the server with `Ctrl+C`.

## GitHub Pages

The repository is ready for a root-directory GitHub Pages deployment:

1. In the repository settings, open **Pages**.
2. Select **Deploy from a branch**.
3. Select the `main` branch and the `/ (root)` folder.
4. Save the setting.

The `CNAME` file declares the custom domain `plastocyanin.org`. DNS is managed separately and is not changed by this repository.
