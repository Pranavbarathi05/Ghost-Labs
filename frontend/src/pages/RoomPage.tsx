import { useParams } from 'react-router-dom'
import { useState } from 'react'

export default function RoomPage() {
  const { roomId } = useParams()
  const [message, setMessage] = useState('')
  const [messages, setMessages] = useState([
    { id: 1, user: 'Alice', content: 'Hey everyone!', timestamp: new Date() },
    { id: 2, user: 'Bob', content: 'Hi Alice!', timestamp: new Date() },
  ])

  const handleSendMessage = (e: React.FormEvent) => {
    e.preventDefault()
    if (!message.trim()) return
    
    // TODO: Send message via WebSocket
    const newMessage = {
      id: messages.length + 1,
      user: 'You',
      content: message,
      timestamp: new Date()
    }
    setMessages([...messages, newMessage])
    setMessage('')
  }

  return (
    <div className="page">
      <h1>Room {roomId}</h1>
      
      <div style={{ display: 'grid', gridTemplateColumns: '1fr 350px', gap: '20px', marginTop: '40px' }}>
        {/* Workspace area */}
        <div>
          <div className="workspace-tabs">
            <button className="workspace-tab active">My Workspace</button>
            <button className="workspace-tab">Alice's Workspace</button>
          </div>
          
          <div className="card">
            <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '16px' }}>
              <h3>Terminal</h3>
              <div style={{ display: 'flex', gap: '8px' }}>
                <button className="btn btn-secondary">Start</button>
                <button className="btn btn-secondary">Snapshot</button>
                <button className="btn btn-secondary">AI Assist</button>
              </div>
            </div>
            <div className="terminal-container">
              <p style={{ color: '#4ade80', padding: '16px' }}>
                $ Terminal will be rendered here using xterm.js
              </p>
            </div>
          </div>
        </div>
        
        {/* Chat area */}
        <div>
          <div className="card">
            <h3>Chat</h3>
            <div className="chat-container" style={{ marginTop: '16px' }}>
              <div className="chat-messages">
                {messages.map(msg => (
                  <div key={msg.id} style={{ marginBottom: '12px', padding: '8px', background: 'rgba(255,255,255,0.05)', borderRadius: '6px' }}>
                    <strong>{msg.user}:</strong> {msg.content}
                  </div>
                ))}
              </div>
              <form onSubmit={handleSendMessage} className="chat-input">
                <input
                  type="text"
                  value={message}
                  onChange={(e) => setMessage(e.target.value)}
                  placeholder="Type a message..."
                />
                <button type="submit" className="btn btn-primary">Send</button>
              </form>
            </div>
          </div>
          
          <div className="card" style={{ marginTop: '16px' }}>
            <h3>Room Members</h3>
            <ul style={{ marginTop: '12px', listStyle: 'none' }}>
              <li style={{ padding: '8px' }}>👤 You (Host)</li>
              <li style={{ padding: '8px' }}>👤 Alice</li>
              <li style={{ padding: '8px' }}>👤 Bob</li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  )
}
