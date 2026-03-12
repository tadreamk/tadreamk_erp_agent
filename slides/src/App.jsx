import { motion } from 'framer-motion';
import {
  Users, TrendingUp, DollarSign, Megaphone, Globe, BarChart3, Video
} from 'lucide-react';

const stats = [
  { icon: Users, label: 'Attendees', value: '550K+', color: 'text-purple-600', bg: 'bg-purple-100' },
  { icon: TrendingUp, label: 'Startups', value: '8,100+', color: 'text-violet-600', bg: 'bg-violet-100' },
  { icon: DollarSign, label: 'Investors', value: '2,300+', color: 'text-fuchsia-600', bg: 'bg-fuchsia-100' },
  { icon: Megaphone, label: 'Speakers', value: '770', color: 'text-indigo-600', bg: 'bg-indigo-100' },
  { icon: Globe, label: 'Countries', value: '70+', color: 'text-purple-600', bg: 'bg-purple-100' },
  { icon: BarChart3, label: 'Matchings', value: '1,400+', color: 'text-violet-600', bg: 'bg-violet-100' },
  { icon: Video, label: 'Media', value: '1,300+', color: 'text-fuchsia-600', bg: 'bg-fuchsia-100' },
];

function App() {
  return (
    <div className="w-full h-screen bg-white text-gray-900 flex flex-col items-center justify-center p-10 font-sans overflow-hidden">
      <div id="slide-content" className="flex flex-col items-center w-full max-w-6xl">
        <motion.div
          initial={{ opacity: 0, y: -20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.6 }}
          className="w-full flex items-center justify-between mb-8"
        >
          <div className="flex-1" />
          <div className="text-center">
            <h1 className="text-5xl font-extrabold tracking-tight mb-3">
              <span className="bg-gradient-to-r from-purple-600 to-violet-500 bg-clip-text text-transparent">
                JUMPSTARTER 2026
              </span>
            </h1>
            <p className="text-gray-500 text-lg max-w-2xl mx-auto">
              Asia&apos;s Leading Startup & Tech Event · AI & Sustainability
            </p>
          </div>
          <div className="flex-1 flex justify-end self-start">
            <div className="flex items-center gap-1">
              <img src="/tadreamk_logo.svg" alt="TadReamk" className="w-11 h-11" />
              <span className="text-2xl text-gray-600 font-medium">TadReamk.com</span>
            </div>
          </div>
        </motion.div>

        <motion.h2
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ delay: 0.15, duration: 0.4 }}
          className="text-sm font-bold text-slate-500 uppercase tracking-widest mb-4 self-start"
        >
          JUMPSTARTER in Numbers (2017–2025)
        </motion.h2>
        <div className="w-full grid grid-cols-4 gap-4">
          {stats.map((item, i) => (
            <motion.div
              key={item.label}
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ delay: 0.2 + i * 0.08, duration: 0.5 }}
              className="bg-purple-50 border border-purple-200 rounded-2xl p-5 flex flex-col items-center text-center hover:scale-105 transition-transform"
            >
              <div className={`${item.bg} p-3 rounded-xl mb-3`}>
                <item.icon className={`w-7 h-7 ${item.color}`} />
              </div>
              <span className="text-2xl font-bold text-gray-900 mb-1">{item.value}</span>
              <span className="text-gray-500 text-sm">{item.label}</span>
            </motion.div>
          ))}
        </div>

        <motion.p
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ delay: 1.2, duration: 0.6 }}
          className="mt-8 text-xs text-gray-400 text-center"
        >
          Mar 12–13, 2026 · Hall 5BC, HKCEC · jumpstarter.hk
        </motion.p>
      </div>
    </div>
  );
}

export default App;
