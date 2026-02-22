import { Link } from 'react-router-dom'

export default function HomePage() {
  return (
    <div className="page">
      <h1>🚀 Ghost Labs</h1>
      <p style={{ marginTop: '20px', fontSize: '1.2em' }}>
        Secure Collaborative Workspace with Persistent Linux Labs + AI Agent
      </p>
      
      <div style={{ marginTop: '40px', display: 'flex', gap: '16px', justifyContent: 'center' }}>
        <Link to="/login">
          <button className="btn btn-primary">Login</button>
        </Link>
        <Link to="/register">
          <button className="btn btn-secondary">Register</button>
        </Link>
      </div>
      
      <div className="card" style={{ marginTop: '60px', textAlign: 'left' }}>
        <h2>Features</h2>
        <ul style={{ marginTop: '20px', lineHeight: '2' }}>
          <li>🔐 Secure authentication and room creation</li>
          <li>💬 Real-time encrypted messaging</li>
          <li>🖥️ Personal Linux workspaces (Docker-based)</li>
          <li>📸 Workspace snapshot & restore</li>
          <li>👥 Collaborative workspace access</li>
          <li>🎥 Video streaming support</li>
          <li>🤖 Integrated AI coding agent</li>
          <li>🔒 Secure tunnel-based access</li>
        </ul>
      </div>
    </div>
  )
}
