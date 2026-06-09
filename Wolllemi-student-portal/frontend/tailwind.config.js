/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        theme: {
          primary: 'var(--color-primary)',
          secondary: 'var(--color-secondary)',
          accent: 'var(--color-accent)',
          background: 'var(--color-background)',
          text: 'var(--color-text)',
        }
      },
      borderRadius: {
        'theme': 'var(--radius-theme)',
      },
      boxShadow: {
        'glow': 'var(--shadow-glow)',
      }
    },
  },
  plugins: [],
}
