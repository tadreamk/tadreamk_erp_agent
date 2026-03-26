import { motion } from 'framer-motion';
import {
  UserCheck, HelpCircle, Zap, Cpu,
  CheckCircle, FileText, Calendar, CreditCard,
  Receipt, DollarSign, BookOpen, GitBranch,
  MessageSquare,
} from 'lucide-react';

const features = [
  {
    icon: UserCheck,
    title: '@Mention Ranking',
    desc: 'Frequency-ranked suggestions surface the right colleagues first',
    color: 'text-cyan-600',
    bg: 'bg-cyan-50 border-cyan-200',
    iconBg: 'bg-cyan-100',
  },
  {
    icon: HelpCircle,
    title: 'Question Markers',
    desc: 'Flag comments that need a response so nothing gets buried',
    color: 'text-teal-600',
    bg: 'bg-teal-50 border-teal-200',
    iconBg: 'bg-teal-100',
  },
  {
    icon: Zap,
    title: 'Real-Time Updates',
    desc: 'WebSocket broadcasts — new comments appear instantly for all viewers',
    color: 'text-sky-600',
    bg: 'bg-sky-50 border-sky-200',
    iconBg: 'bg-sky-100',
  },
  {
    icon: Cpu,
    title: 'AI Feedback',
    desc: 'Auto-generated narrative + action items on every task comment',
    color: 'text-indigo-600',
    bg: 'bg-indigo-50 border-indigo-200',
    iconBg: 'bg-indigo-100',
  },
];

const records = [
  { icon: CheckCircle, label: 'Tasks', color: 'text-cyan-600' },
  { icon: FileText, label: 'Applications', color: 'text-teal-600' },
  { icon: Calendar, label: 'Leave Requests', color: 'text-sky-600' },
  { icon: CreditCard, label: 'Payslips', color: 'text-indigo-600' },
  { icon: Receipt, label: 'Reimbursements', color: 'text-cyan-600' },
  { icon: DollarSign, label: 'Expenses', color: 'text-teal-600' },
  { icon: BookOpen, label: 'Technical Reports', color: 'text-sky-600' },
  { icon: GitBranch, label: 'Workflows', color: 'text-indigo-600' },
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
          className="w-full flex items-center justify-between mb-7"
        >
          <div className="flex-1" />
          <div className="text-center">
            <div className="flex items-center justify-center gap-3 mb-2">
              <MessageSquare className="w-9 h-9 text-cyan-600" />
              <h1 className="text-5xl font-extrabold tracking-tight">
                Comment <span className="text-cyan-600">Thread</span>
              </h1>
            </div>
            <p className="text-gray-500 text-lg max-w-2xl mx-auto">
              Contextual collaboration embedded in every record
            </p>
          </div>
          <div className="flex-1 flex justify-end self-start">
            <div className="flex items-center gap-1">
              <img src="/tadreamk_logo.svg" alt="TadReamk" className="w-11 h-11" />
              <span className="text-2xl text-gray-600 font-medium">TadReamk.com</span>
            </div>
          </div>
        </motion.div>

        {/* Feature cards */}
        <div className="w-full grid grid-cols-4 gap-4 mb-5">
          {features.map((f, i) => (
            <motion.div
              key={f.title}
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ delay: 0.2 + i * 0.1, duration: 0.5 }}
              className={`${f.bg} border rounded-xl p-4 hover:scale-105 transition-transform`}
            >
              <div className={`${f.iconBg} w-10 h-10 rounded-lg flex items-center justify-center mb-3`}>
                <f.icon className={`w-5 h-5 ${f.color}`} />
              </div>
              <p className={`text-sm font-bold ${f.color} mb-1`}>{f.title}</p>
              <p className="text-xs text-gray-500 leading-snug">{f.desc}</p>
            </motion.div>
          ))}
        </div>

        {/* Supported records */}
        <motion.div
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ delay: 0.7, duration: 0.5 }}
          className="w-full"
        >
          <p className="text-xs font-semibold text-gray-400 uppercase tracking-widest text-center mb-3">
            Attached to 8 record types
          </p>
          <div className="w-full grid grid-cols-8 gap-2">
            {records.map((r, i) => (
              <motion.div
                key={r.label}
                initial={{ opacity: 0, scale: 0.9 }}
                animate={{ opacity: 1, scale: 1 }}
                transition={{ delay: 0.8 + i * 0.05, duration: 0.4 }}
                className="bg-gray-50 border border-gray-200 rounded-lg p-3 flex flex-col items-center gap-1.5 hover:scale-105 transition-transform"
              >
                <r.icon className={`w-5 h-5 ${r.color}`} />
                <span className="text-xs text-gray-600 font-medium text-center leading-tight">{r.label}</span>
              </motion.div>
            ))}
          </div>
        </motion.div>

        {/* Footer */}
        <motion.p
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ delay: 1.3, duration: 0.6 }}
          className="mt-6 text-xs text-gray-400 text-center"
        >
          Polymorphic design · Soft delete · Flat chronological thread · Two-stage permission model
        </motion.p>

      </div>
    </div>
  );
}

export default App;
