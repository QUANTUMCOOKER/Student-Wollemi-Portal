import React from 'react';
import ThemeSwitcher from '../components/ThemeSwitcher';
import { LogIn } from 'lucide-react';

const LandingPage: React.FC = () => {
  const handleGoogleLogin = () => {
    // In a real environment, this would call the backend /auth/google/login
    // For this prototype, we simulate the redirect
    window.location.href = 'http://localhost:8000/auth/google/login';
  };

  return (
    <div className="flex flex-col items-center justify-center min-h-screen p-4 text-center">
      <ThemeSwitcher />
      
      <div className="glass-morphism p-12 rounded-theme max-w-2xl w-full border-theme-primary shadow-glow">
        <h1 className="text-5xl font-bold mb-4 bg-gradient-to-r from-theme-primary to-theme-accent bg-clip-text text-transparent">
          Wolllemi Student Portal
        </h1>
        <p className="text-xl mb-8 opacity-80">
          Your modern gateway to academic excellence for Years 7-12.
        </p>
        
        <button
          onClick={handleGoogleLogin}
          className="flex items-center gap-3 px-8 py-4 bg-theme-primary text-white rounded-theme font-semibold hover:scale-105 transition-transform shadow-lg"
        >
          <LogIn size={24} />
          Sign in with Google
        </button>
        
        <div className="mt-12 grid grid-cols-2 md:grid-cols-4 gap-4 text-sm font-medium">
          <div className="p-4 rounded-theme bg-theme-secondary/20">Academic Schedules</div>
          <div className="p-4 rounded-theme bg-theme-secondary/20">Grade Tracking</div>
          <div className="p-4 rounded-theme bg-theme-secondary/20">Assignments</div>
          <div className="p-4 rounded-theme bg-theme-secondary/20">Resource Library</div>
        </div>
      </div>
    </div>
  );
};

export default LandingPage;
