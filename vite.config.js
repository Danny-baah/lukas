import fs from 'fs';
import { resolve } from 'path';
import { defineConfig } from 'vite';

// Plugin 1: Strip all HTML comments from production output
function stripHtmlCommentsPlugin() {
  return {
    name: 'strip-html-comments',
    enforce: 'post',
    transformIndexHtml(html) {
      return html.replace(/<!--[\s\S]*?-->/g, '');
    },
  };
}

// Plugin 2: Support clean URLs (without .html) in local Vite dev server
function cleanUrlsDevPlugin() {
  return {
    name: 'clean-urls-dev',
    configureServer(server) {
      server.middlewares.use((req, res, next) => {
        if (req.url && !req.url.includes('.') && req.url !== '/') {
          const urlObj = new URL(req.url, 'http://localhost');
          const cleanPath = urlObj.pathname.replace(/\/$/, '');
          const extensionlessMap = {
            '/ueber-uns': '/ueber-uns.html',
            '/leistungen': '/leistungen.html',
            '/preise': '/preise.html',
            '/kontakt': '/kontakt.html',
            '/impressum': '/impressum.html',
            '/datenschutz': '/datenschutz.html',
            '/about': '/ueber-uns.html',
            '/services': '/leistungen.html',
            '/pricing': '/preise.html',
            '/contact': '/kontakt.html',
          };
          if (extensionlessMap[cleanPath]) {
            req.url = extensionlessMap[cleanPath] + urlObj.search + urlObj.hash;
          }
        }
        next();
      });
    },
  };
}

// Plugin 3: Post-build hook to create directory index files (e.g. dist/kontakt/index.html)
// Ensures clean URLs work on every FTP / static host regardless of server config
function cleanUrlsBuildPlugin() {
  return {
    name: 'clean-urls-build',
    closeBundle() {
      const distDir = resolve(import.meta.dirname, 'dist');
      const pages = ['ueber-uns', 'leistungen', 'preise', 'kontakt', 'impressum', 'datenschutz'];
      pages.forEach((page) => {
        const srcFile = resolve(distDir, `${page}.html`);
        const targetDir = resolve(distDir, page);
        if (fs.existsSync(srcFile)) {
          if (!fs.existsSync(targetDir)) {
            fs.mkdirSync(targetDir, { recursive: true });
          }
          fs.copyFileSync(srcFile, resolve(targetDir, 'index.html'));
        }
      });
    },
  };
}

export default defineConfig({
  plugins: [
    stripHtmlCommentsPlugin(),
    cleanUrlsDevPlugin(),
    cleanUrlsBuildPlugin(),
  ],
  build: {
    sourcemap: false, // Prevents exposing source files and computer paths in DevTools
    rollupOptions: {
      input: {
        main: resolve(import.meta.dirname, 'index.html'),
        ueberUns: resolve(import.meta.dirname, 'ueber-uns.html'),
        leistungen: resolve(import.meta.dirname, 'leistungen.html'),
        preise: resolve(import.meta.dirname, 'preise.html'),
        kontakt: resolve(import.meta.dirname, 'kontakt.html'),
        impressum: resolve(import.meta.dirname, 'impressum.html'),
        datenschutz: resolve(import.meta.dirname, 'datenschutz.html'),
        // Backward-compatible redirect pages
        about: resolve(import.meta.dirname, 'about.html'),
        services: resolve(import.meta.dirname, 'services.html'),
        pricing: resolve(import.meta.dirname, 'pricing.html'),
        contact: resolve(import.meta.dirname, 'contact.html'),
      },
    },
  },
});
