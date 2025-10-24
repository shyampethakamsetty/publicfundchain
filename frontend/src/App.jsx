
import React from 'react';
import Dashboard from './components/Dashboard';

function App() {
  return (
    <div className="min-h-screen bg-gray-50">
      <header className="p-4 bg-white shadow">
        <h1 className="text-2xl font-semibold">PublicFundChain</h1>
      </header>
      <main className="p-6">
        <Dashboard />
      </main>
    </div>
  );
}

export default App;
