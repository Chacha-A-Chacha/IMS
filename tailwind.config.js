/** @type {import('tailwindcss').Config} */

module.exports = {
  content: [
    "./app/templates/**/*.html",
    "./app/static/src/**/*.js"
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}

//npx tailwindcss -i .app/static/src/main.css -o .app/static/css/output.css --watch