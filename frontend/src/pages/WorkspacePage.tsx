import { useParams } from 'react-router-dom'

export default function WorkspacePage() {
  const { workspaceId } = useParams()

  return (
    <div className="page">
      <h1>Workspace {workspaceId}</h1>
      
      <div className="card" style={{ marginTop: '40px' }}>
        <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '20px' }}>
          <h2>Linux Terminal</h2>
          <div style={{ display: 'flex', gap: '8px' }}>
            <button className="btn btn-primary">Start</button>
            <button className="btn btn-secondary">Stop</button>
            <button className="btn btn-secondary">Snapshot</button>
            <button className="btn btn-secondary">Restore</button>
          </div>
        </div>
        
        <div className="terminal-container">
          <p style={{ color: '#4ade80', padding: '16px' }}>
            $ Terminal will be rendered here using xterm.js<br />
            $ Connected to Ubuntu 22.04 LTS<br />
            $ Type 'help' for available commands
          </p>
        </div>
        
        <div style={{ marginTop: '20px', display: 'flex', gap: '16px' }}>
          <div style={{ flex: 1 }}>
            <h3>Workspace Info</h3>
            <p style={{ marginTop: '8px' }}>Status: <span style={{ color: '#4ade80' }}>Running</span></p>
            <p>Container ID: abc123def456</p>
            <p>Uptime: 2h 34m</p>
          </div>
          
          <div style={{ flex: 1 }}>
            <h3>AI Assistant</h3>
            <button className="btn btn-primary" style={{ marginTop: '8px', width: '100%' }}>
              🤖 Open AI Chat
            </button>
            <p style={{ marginTop: '8px', fontSize: '0.9em' }}>
              Get code suggestions, explanations, and debugging help
            </p>
          </div>
        </div>
      </div>
    </div>
  )
}
