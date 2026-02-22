import { Link } from 'react-router-dom'

export default function DashboardPage() {
  // TODO: Fetch actual data from API
  const rooms = [
    { id: 1, name: 'Project Alpha', members: 5 },
    { id: 2, name: 'Study Session', members: 3 },
  ]

  const workspaces = [
    { id: 1, name: 'Dev Environment', status: 'stopped' },
    { id: 2, name: 'Test Lab', status: 'running' },
  ]

  return (
    <div className="page">
      <h1>Dashboard</h1>
      
      <div style={{ marginTop: '40px' }}>
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
          <h2>My Rooms</h2>
          <button className="btn btn-primary">Create Room</button>
        </div>
        
        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(300px, 1fr))', gap: '16px', marginTop: '20px' }}>
          {rooms.map(room => (
            <Link key={room.id} to={`/room/${room.id}`} style={{ textDecoration: 'none' }}>
              <div className="card" style={{ cursor: 'pointer' }}>
                <h3>{room.name}</h3>
                <p>👥 {room.members} members</p>
              </div>
            </Link>
          ))}
        </div>
      </div>
      
      <div style={{ marginTop: '60px' }}>
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
          <h2>My Workspaces</h2>
          <button className="btn btn-primary">Create Workspace</button>
        </div>
        
        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(300px, 1fr))', gap: '16px', marginTop: '20px' }}>
          {workspaces.map(workspace => (
            <Link key={workspace.id} to={`/workspace/${workspace.id}`} style={{ textDecoration: 'none' }}>
              <div className="card" style={{ cursor: 'pointer' }}>
                <h3>{workspace.name}</h3>
                <p>
                  Status: <span style={{ color: workspace.status === 'running' ? '#4ade80' : '#94a3b8' }}>
                    {workspace.status}
                  </span>
                </p>
              </div>
            </Link>
          ))}
        </div>
      </div>
    </div>
  )
}
