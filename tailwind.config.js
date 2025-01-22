/** @type {import('tailwindcss').Config} */
module.exports = {
  darkMode: 'class', // or'media' or 'class'
  darkMode: 'media', // or'media' or 'class'
  mode: 'jit',
  purge: {
    enabled: true,
  },
  content: [
    "./src/**/*.{html,js}",
    './templates/**/*.html',
     './node_modules/flowbite/**/*.js',
     './templates/view/base.html',
     './templates/includes/nav.html',
     './edimars/templates/core/index.html',
     
  ],
  theme: {
    extend: {},
  },
  plugins: [require('flowbite/plugin')],
}

