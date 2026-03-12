# React Slide Template

## Project Structure

The `slides/` folder is a Vite + React + Tailwind + Framer Motion + Lucide React project:
```
slides/
├── package.json
├── vite.config.js
├── tailwind.config.js
├── postcss.config.js
├── index.html
└── src/
    ├── main.jsx
    ├── index.css
    └── App.jsx            # THE SLIDE — edit this file
```

## App.jsx Template

Edit `slides/src/App.jsx` with this structure:

```jsx
import { motion } from 'framer-motion';
import { Icon1, Icon2 } from 'lucide-react';

// Data defined outside the component

function App() {
  return (
    <div className="w-full h-screen bg-white text-gray-900 flex flex-col items-center justify-center p-10 font-sans overflow-hidden">
      <div id="slide-content" className="flex flex-col items-center w-full max-w-6xl">
        {/* Title row with branding */}
        <motion.div initial={{ opacity: 0, y: -20 }} animate={{ opacity: 1, y: 0 }} transition={{ duration: 0.6 }} className="w-full flex items-center justify-between mb-8">
          <div className="flex-1" />
          <div className="text-center">
            <h1 className="text-5xl font-extrabold tracking-tight mb-3">
              Slide <span className="THEME_ACCENT">Title</span>
            </h1>
            <p className="THEME_SUBTITLE text-lg max-w-2xl mx-auto">Subtitle</p>
          </div>
          <div className="flex-1 flex justify-end self-start">
            <div className="flex items-center gap-1">
              <img src="/tadreamk_logo.svg" alt="TadReamk" className="w-11 h-11" />
              <span className="text-2xl text-gray-600 font-medium">TadReamk.com</span>
            </div>
          </div>
        </motion.div>

        {/* Main content area */}
        <div className="w-full">
          {/* Cards, grids, hub, etc. */}
        </div>

        {/* Footer */}
        <motion.p initial={{ opacity: 0 }} animate={{ opacity: 1 }} transition={{ delay: 1.2, duration: 0.6 }} className="mt-8 text-xs THEME_FOOTER text-center">
          Brief footer note
        </motion.p>
      </div>
    </div>
  );
}

export default App;
```

Replace `THEME_ACCENT`, `THEME_SUBTITLE`, `THEME_FOOTER` with actual Tailwind classes from the chosen theme in [color-themes.md](color-themes.md).

**IMPORTANT**: The `<div id="slide-content">` wrapper is required — the export script uses it for cropping.

## Design Guidelines

- Use `motion.div` with staggered delays for entrance animations
- Add `hover:scale-105 transition-transform` on cards
- Keep text minimal — short labels, not sentences
- Branding (TadReamk logo + text) always top-right of the title row
- The `#slide-content` wrapper must have `w-full max-w-6xl` to prevent branding overflow
- Only use icons from [lucide-icons.md](lucide-icons.md). Do NOT guess icon names.

## Export

Export as PNG using Playwright:
```bash
python scripts/export_slides_images.py --url http://localhost:3009 --output <output_path>
```

Options:
- `--padding 30` — adjust padding around content (default: 20)
- `--width 2560 --height 1440` — larger viewport for higher resolution
- `--selector "#my-element"` — target a different element
