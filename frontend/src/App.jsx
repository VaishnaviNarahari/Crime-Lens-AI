import { useEffect, useMemo, useState } from 'react';

const sampleRecords = [
  {
    id: 1,
    date: '2024-01-10T09:30:00',
    primary_type: 'Theft',
    latitude: 41.88,
    longitude: -87.63,
    district: 'Central',
  },
  {
    id: 2,
    date: '2024-01-11T10:00:00',
    primary_type: 'Battery',
    latitude: 41.87,
    longitude: -87.62,
    district: 'North',
  },
  {
    id: 3,
    date: '2024-02-10T12:00:00',
    primary_type: 'Assault',
    latitude: 41.89,
    longitude: -87.64,
    district: 'Central',
  },
];

const fallbackDashboard = {
  kpis: {
    total_incidents: 3,
    high_risk_zones: 2,
    active_categories: 3,
    confidence: 0.81,
  },
  trends: [
    { label: 'Theft concentration', value: 2 },
    { label: 'Assault clusters', value: 1 },
  ],
  recommendations: [
    { title: 'Deploy patrols around Central', confidence: 0.84 },
    { title: 'Increase visibility near North', confidence: 0.78 },
  ],
  hotspots: [
    { category: 'Theft', latitude: 41.88, longitude: -87.63 },
  ],
};

const fallbackPrediction = {
  forecast: [
    { district: 'Central', confidence: 0.78 },
    { district: 'North', confidence: 0.72 },
  ],
};

const navItems = [
  { id: 'dashboard', label: 'Dashboard' },
  { id: 'map', label: 'Crime Map' },
  { id: 'cases', label: 'Case Explorer' },
  { id: 'predictive', label: 'Predictive AI' },
  { id: 'network', label: 'Network' },
  { id: 'reports', label: 'Reports' },
];

function App() {
  const [dashboard, setDashboard] = useState(fallbackDashboard);
  const [prediction, setPrediction] = useState(fallbackPrediction);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const [activeView, setActiveView] = useState('dashboard');

  const runAnalysis = async () => {
    setLoading(true);
    setError('');

    try {
      const [dashboardResponse, predictionResponse] = await Promise.all([
        fetch('http://127.0.0.1:8002/dashboard/overview', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ records: sampleRecords }),
        }),
        fetch('http://127.0.0.1:8002/predictive/intelligence', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ records: sampleRecords }),
        }),
      ]);

      if (!dashboardResponse.ok || !predictionResponse.ok) {
        throw new Error('The intelligence API is temporarily unavailable.');
      }

      const dashboardData = await dashboardResponse.json();
      const predictionData = await predictionResponse.json();
      setDashboard(dashboardData || fallbackDashboard);
      setPrediction(predictionData || fallbackPrediction);
    } catch (err) {
      setDashboard(fallbackDashboard);
      setPrediction(fallbackPrediction);
      setError(err.message || 'Unable to reach the backend.');
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    runAnalysis();
  }, []);

  const overview = useMemo(() => {
    const kpis = dashboard?.kpis || fallbackDashboard.kpis;
    return [
      { label: 'Total incidents', value: kpis.total_incidents },
      { label: 'High-risk zones', value: kpis.high_risk_zones },
      { label: 'Active categories', value: kpis.active_categories },
      { label: 'Confidence', value: `${Math.round(kpis.confidence * 100)}%` },
    ];
  }, [dashboard]);

  return (
    <div className="app-shell">
      <aside className="sidebar">
        <div className="brand-block">
          <div className="brand-mark">CL</div>
          <div>
            <h2>CrimeLens AI</h2>
            <p>Intelligence Center</p>
          </div>
        </div>

        <nav className="nav-links">
          {navItems.map((item) => (
            <button
              key={item.id}
              className={`nav-button ${activeView === item.id ? 'active' : ''}`}
              onClick={() => setActiveView(item.id)}
            >
              {item.label}
            </button>
          ))}
        </nav>
      </aside>

      <main className="main-panel">
        <header className="hero">
          <div>
            <p className="eyebrow">Karnataka Crime Intelligence Operating System</p>
            <h1>CrimeLens AI Command Center</h1>
            <p className="hero-copy">
              Explainable intelligence for hotspots, trends, patrol recommendations, and investigative decision support.
            </p>
          </div>
          <button onClick={runAnalysis} disabled={loading}>
            {loading ? 'Refreshing intelligence…' : 'Refresh intelligence'}
          </button>
        </header>

        {error ? <div className="status-banner">{error}</div> : null}

        {activeView === 'dashboard' ? (
          <>
            <section className="grid">
              {overview.map((item) => (
                <article key={item.label} className="card metric-card">
                  <h2>{item.label}</h2>
                  <p>{item.value}</p>
                </article>
              ))}
            </section>

            <section className="content-grid">
              <article className="card wide-card">
                <h2>Operational trends</h2>
                <div className="list-stack">
                  {dashboard?.trends?.map((item) => (
                    <div key={item.label} className="list-row">
                      <span>{item.label}</span>
                      <strong>{item.value} incidents</strong>
                    </div>
                  ))}
                </div>
              </article>

              <article className="card wide-card">
                <h2>AI recommendations</h2>
                <div className="list-stack">
                  {dashboard?.recommendations?.map((item) => (
                    <div key={item.title} className="list-row">
                      <span>{item.title}</span>
                      <strong>{Math.round(item.confidence * 100)}%</strong>
                    </div>
                  ))}
                </div>
              </article>
            </section>

            <section className="content-grid">
              <article className="card">
                <h2>Hotspot intelligence</h2>
                <div className="list-stack">
                  {dashboard?.hotspots?.map((item) => (
                    <div key={`${item.latitude}-${item.longitude}`} className="list-row">
                      <span>{item.category}</span>
                      <strong>{item.latitude.toFixed(2)}, {item.longitude.toFixed(2)}</strong>
                    </div>
                  ))}
                </div>
              </article>

              <article className="card">
                <h2>Predictive outlook</h2>
                <div className="list-stack">
                  {prediction?.forecast?.map((item) => (
                    <div key={item.district} className="list-row">
                      <span>{item.district}</span>
                      <strong>{item.confidence * 100}% confidence</strong>
                    </div>
                  ))}
                </div>
              </article>
            </section>
          </>
        ) : null}

        {activeView === 'map' ? (
          <section className="view-grid">
            <article className="card wide-card">
              <h2>Live incident map</h2>
              <div className="map-surface">
                <div className="map-grid" />
                <div className="map-glow" />
                {sampleRecords.map((record, idx) => {
                  const typeColor = {
                    'Theft': '#3b82f6',
                    'Battery': '#ef4444',
                    'Assault': '#f97316',
                  }[record.primary_type] || '#64748b';
                  
                  const normalizedLat = ((record.latitude - 41.87) / (41.89 - 41.87)) * 100;
                  const normalizedLng = ((record.longitude - (-87.64)) / ((-87.62) - (-87.64))) * 100;
                  
                  return (
                    <div
                      key={idx}
                      className="map-marker"
                      style={{
                        left: `${normalizedLng}%`,
                        top: `${normalizedLat}%`,
                        '--marker-color': typeColor,
                      }}
                      title={`${record.primary_type} - ${record.district}`}
                    >
                      <div className="marker-ping" />
                      <div className="marker-dot" />
                    </div>
                  );
                })}
                <div className="map-overlay">
                  <p>Active monitoring zone · {sampleRecords.length} incidents</p>
                  <div className="pill-row">
                    <span className="pill pill-theft">● Theft</span>
                    <span className="pill pill-battery">● Battery</span>
                    <span className="pill pill-assault">● Assault</span>
                  </div>
                </div>
              </div>
            </article>

            <article className="card">
              <h2>Incidents on map</h2>
              <div className="list-stack">
                {sampleRecords.map((record) => (
                  <div key={record.id} className="list-row incident-row">
                    <div className="incident-info">
                      <strong>{record.primary_type}</strong>
                      <span className="incident-district">{record.district}</span>
                    </div>
                    <span className="incident-time">{record.date.split('T')[1].slice(0, 5)}</span>
                  </div>
                ))}
              </div>
            </article>
          </section>
        ) : null}

        {activeView === 'cases' ? (
          <section className="view-grid">
            <article className="card wide-card">
              <h2>Open case queue</h2>
              <div className="table-stack">
                {sampleRecords.map((record) => (
                  <div key={record.id} className="table-row">
                    <span>{record.primary_type}</span>
                    <span>{record.district}</span>
                    <span>{record.date.split('T')[0]}</span>
                  </div>
                ))}
              </div>
            </article>

            <article className="card">
              <h2>Case triage</h2>
              <div className="list-stack">
                <div className="list-row"><span>Priority queue</span><strong>High</strong></div>
                <div className="list-row"><span>Evidence review</span><strong>2 pending</strong></div>
                <div className="list-row"><span>Officer assignment</span><strong>3 active</strong></div>
              </div>
            </article>
          </section>
        ) : null}

        {activeView === 'predictive' ? (
          <section className="view-grid">
            <article className="card wide-card">
              <h2>Threat forecast</h2>
              <div className="list-stack">
                {prediction?.forecast?.map((item) => (
                  <div key={item.district} className="list-row">
                    <span>{item.district}</span>
                    <strong>{Math.round(item.confidence * 100)}% confidence</strong>
                  </div>
                ))}
              </div>
            </article>

            <article className="card">
              <h2>Recommended actions</h2>
              <div className="list-stack">
                {dashboard?.recommendations?.map((item) => (
                  <div key={item.title} className="list-row">
                    <span>{item.title}</span>
                    <strong>{Math.round(item.confidence * 100)}%</strong>
                  </div>
                ))}
              </div>
            </article>
          </section>
        ) : null}

        {activeView === 'network' ? (
          <section className="view-grid">
            <article className="card wide-card">
              <h2>Association network</h2>
              <div className="map-surface compact-map">
                <div className="map-glow" />
                <div className="map-overlay">
                  <p>Linked entities and repeat contacts</p>
                  <div className="pill-row">
                    <span className="pill">Person A</span>
                    <span className="pill">Location B</span>
                    <span className="pill">Vehicle C</span>
                  </div>
                </div>
              </div>
            </article>

            <article className="card">
              <h2>Network notes</h2>
              <div className="list-stack">
                <div className="list-row"><span>Known links</span><strong>7 active</strong></div>
                <div className="list-row"><span>Cross-reference score</span><strong>0.82</strong></div>
                <div className="list-row"><span>Investigation flags</span><strong>3 new</strong></div>
              </div>
            </article>
          </section>
        ) : null}

        {activeView === 'reports' ? (
          <section className="view-grid">
            <article className="card wide-card">
              <h2>Operational report</h2>
              <div className="list-stack">
                <div className="list-row"><span>Summary</span><strong>Pattern review complete</strong></div>
                <div className="list-row"><span>Coverage</span><strong>Central and North zones</strong></div>
                <div className="list-row"><span>Next export</span><strong>Auto-generated at 18:00</strong></div>
              </div>
            </article>

            <article className="card">
              <h2>Export options</h2>
              <div className="list-stack">
                <div className="list-row"><span>PDF brief</span><strong>Ready</strong></div>
                <div className="list-row"><span>CSV feed</span><strong>Ready</strong></div>
                <div className="list-row"><span>Share link</span><strong>Active</strong></div>
              </div>
            </article>
          </section>
        ) : null}
      </main>
    </div>
  );
}

export default App;
