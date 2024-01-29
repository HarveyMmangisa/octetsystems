module.exports = {
    theme: {
       extend: {
         keyframes: {
           slide: {
             '0%': { transform: 'translateX(-100%)' },
             '100%': { transform: 'translateX(100%)' }
           }
         },
         animation: {
           slide: 'slide 5s ease-in-out infinite'
         }
       }
    },
    variants: {},
    plugins: []
   }