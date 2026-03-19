import { motion } from 'framer-motion';
import {
  TrendingUp, DollarSign, Users, BarChart3, Clock, ArrowRight
} from 'lucide-react';

const changes = [
  {
    label: 'Max Income Level',
    current: 'HK$30,000',
    proposed: 'HK$40,000',
    change: '+33%',
    icon: TrendingUp,
    color: 'text-indigo-600',
    iconBg: 'bg-indigo-100',
  },
  {
    label: 'Min Income Level',
    current: 'HK$7,100',
    proposed: 'HK$10,000',
    change: '+41%',
    icon: DollarSign,
    color: 'text-indigo-600',
    iconBg: 'bg-indigo-100',
  },
  {
    label: 'Max Monthly Contribution',
    current: 'HK$1,500',
    proposed: 'HK$2,000',
    change: '+33%',
    icon: BarChart3,
    color: 'text-indigo-600',
    iconBg: 'bg-indigo-100',
  },
];

const stats = [
  { value: '2.6M+', label: 'Employees Registered', icon: Users, color: 'text-emerald-600' },
  { value: 'HK$1.55T', label: 'Net Asset Value', icon: DollarSign, color: 'text-blue-600' },
  { value: '13 Years', label: 'Since Last Adjustment', icon: Clock, color: 'text-amber-600' },
];

function App() {
  return (
    <div className="w-full h-screen bg-white text-gray-900 flex flex-col items-center justify-center p-10 font-sans overflow-hidden">
      <div id="slide-content" className="flex flex-col items-center w-full max-w-6xl">
        {/* Title row with branding */}
        <motion.div
          initial={{ opacity: 0, y: -20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.6 }}
          className="w-full flex items-center justify-between mb-6"
        >
          <div className="flex-1" />
          <div className="text-center">
            <h1 className="text-4xl font-extrabold tracking-tight mb-2">
              <span className="text-indigo-600">MPF</span> Contribution Cap: <span className="text-indigo-600">33% Increase</span> Proposed
            </h1>
            <p className="text-gray-500 text-base max-w-2xl mx-auto">
              Current vs proposed thresholds after 13 years without adjustment
            </p>
          </div>
          <div className="flex-1 flex justify-end self-start">
            <div className="flex items-center gap-1">
              <img src="/tadreamk_logo.svg" alt="TadReamk" className="w-11 h-11" />
              <span className="text-2xl text-gray-600 font-medium">TadReamk.com</span>
            </div>
          </div>
        </motion.div>

        {/* Current → Proposed comparison cards */}
        <div className="w-full grid grid-cols-3 gap-4 mb-5">
          {changes.map((c, i) => (
            <motion.div
              key={c.label}
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ delay: 0.2 + i * 0.1, duration: 0.5 }}
              className="bg-gray-50 border border-gray-200 shadow-sm rounded-xl p-5 hover:scale-105 transition-transform"
            >
              <div className="flex items-center gap-2 mb-3">
                <div className={`${c.iconBg} p-2 rounded-lg`}>
                  <c.icon className={`w-5 h-5 ${c.color}`} />
                </div>
                <span className="text-sm font-bold text-gray-700">{c.label}</span>
              </div>
              <div className="flex items-center gap-2 mb-1">
                <span className="text-lg font-bold text-gray-400 line-through">{c.current}</span>
                <ArrowRight className="w-4 h-4 text-gray-400" />
                <span className={`text-xl font-extrabold ${c.color}`}>{c.proposed}</span>
              </div>
              <span className="text-xs font-semibold text-rose-500 bg-rose-50 px-2 py-0.5 rounded-full">{c.change}</span>
            </motion.div>
          ))}
        </div>

        {/* Supporting stats */}
        <div className="w-full grid grid-cols-3 gap-4">
          {stats.map((s, i) => (
            <motion.div
              key={s.label}
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ delay: 0.6 + i * 0.1, duration: 0.5 }}
              className="flex items-center gap-3 bg-white border border-gray-100 rounded-lg px-4 py-3"
            >
              <s.icon className={`w-5 h-5 ${s.color} flex-shrink-0`} />
              <div>
                <p className={`text-lg font-extrabold ${s.color}`}>{s.value}</p>
                <p className="text-xs text-gray-500">{s.label}</p>
              </div>
            </motion.div>
          ))}
        </div>

        {/* Footer */}
        <motion.p
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ delay: 1.2, duration: 0.6 }}
          className="mt-5 text-xs text-gray-400 text-center"
        >
          Source: MPFA Proposal · SCMP, March 2026
        </motion.p>
      </div>
    </div>
  );
}

export default App;
