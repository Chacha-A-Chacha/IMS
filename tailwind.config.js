/** @type {import('tailwindcss').Config} */

const defaultTheme = require('tailwindcss/defaultTheme')

module.exports = {
  future: {
    // removeDeprecatedGapUtilities: true,
    // purgeLayersByDefault: true,
  },
  purge: [],
  theme: {
    extend: {
      fontFamily: {
        sans: ['Inter var', ...defaultTheme.fontFamily.sans],
      },
    },
  },
  variants: {},
  plugins: [
    // require('@tailwindcss/ui'),
  ],
}


// module.exports = {
//   content: [
//     './app/templates/**/*.{html, js}',  // Path to your Flask templates
//   ],
//   theme: {
//     extend: {},
//   },
//   plugins: [],
// }

