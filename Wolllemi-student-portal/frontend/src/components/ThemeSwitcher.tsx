import React from 'react';
import { useTheme } from '../hooks/useTheme';
import { GlassWater, Zap, CircleSlash, WaveTriangle } from 'lucide-react';

const ThemeSwitcher: React.FC = () => {
  const { theme, setTheme } = useTheme();

  const themes: { id: 'liquid-glass' | 'neon' | 'curves' | 'wave'; label: string; icon: any }[] = [
    { id: 'liquid-glass', label: 'Liquid Glass', icon: <GlassWater size={20} /> },
    { id: 'neon', label: 'Neon', icon: <Zap size={20} /> },
    { id: 'curves', label: 'Curves', icon: <CircleSlash size={20} /> },
    { id: 'wave', label: 'Wave', icon: <WaveTriangle size={20} /> },
  ];

  return (
    <div className="fixed top-4 right-4 flex gap-2 p-2 bg-theme-primary/10 rounded-theme backdrop-blur-md">
      {themes.map((t) => (
        <button
          key={t.id}
          onClick={() => setTheme(t.id)}
          className={`p-2 rounded-theme transition-all ${
            theme === t.id ? 'bg-theme-accent text-white' : 'hover:bg-theme-primary/20'
          }`}
          title={t.label}
        >
          {t.icon}
        </button>
      ))}
    </div>
  );
};

export default ThemeSwitcher;
