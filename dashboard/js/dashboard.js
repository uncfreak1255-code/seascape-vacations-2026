/**
 * Seascape Analytics Dashboard - Core JavaScript
 * Handles data display, charts, and local storage persistence
 */

// ==================== Configuration ====================
const CONFIG = {
  storageKey: 'seascape_dashboard_data',
  refreshInterval: 300000, // 5 minutes
  chartColors: {
    primary: '#3B82F6',
    primaryLight: '#60A5FA',
    secondary: '#F97316',
    success: '#22C55E',
    warning: '#EAB308',
    danger: '#EF4444',
    grid: '#334155',
    text: '#94A3B8'
  }
};

// ==================== Sample Data (Replace with API data) ====================
const SAMPLE_DATA = {
  ga: {
    visitors: 1247,
    visitorsChange: '+12.4%',
    pageViews: 4892,
    pageViewsChange: '+8.2%',
    avgSession: '2:45',
    avgSessionChange: '+0:15',
    bounceRate: 42.3,
    bounceRateChange: '-3.1%',
    trafficTrend: [820, 932, 901, 1090, 1230, 1150, 1247]
  },
  meta: {
    events: 156,
    eventsChange: '+24%',
    pageViews: 3421,
    pageViewsChange: '+15%',
    leads: 18,
    leadsChange: '+6',
    matchQuality: '7.2',
    matchQualityChange: '+0.8',
    eventsTrend: [95, 102, 118, 130, 142, 148, 156]
  },
  revenue: {
    total: 28500,
    totalChange: '+18.5%',
    inquiries: 42,
    inquiriesChange: '+8',
    conversionRate: 3.4,
    conversionChange: '+0.6%'
  },
  funnel: {
    visitors: 1247,
    propertyViews: 748,
    inquiries: 42,
    bookings: 12
  },
  properties: [
    { name: 'Sunset Villa', views: 234, inquiries: 8, bookings: 3, badge: 'Top' },
    { name: 'Ocean Breeze Condo', views: 189, inquiries: 5, bookings: 2, badge: null },
    { name: 'Palm Beach House', views: 156, inquiries: 4, bookings: 1, badge: null },
    { name: 'Gulf View Retreat', views: 142, inquiries: 3, bookings: 1, badge: null },
    { name: 'Coastal Paradise', views: 127, inquiries: 3, bookings: 0, badge: 'New' }
  ],
  sources: [
    { name: 'Google Search', value: 512, percent: 41, color: '#4285F4' },
    { name: 'Direct', value: 287, percent: 23, color: '#34A853' },
    { name: 'Facebook', value: 199, percent: 16, color: '#1877F2' },
    { name: 'Instagram', value: 137, percent: 11, color: '#E4405F' },
    { name: 'Referral', value: 112, percent: 9, color: '#F97316' }
  ],
  dateLabels: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
};

// ==================== Data Management ====================
class DashboardData {
  constructor() {
    this.data = this.load() || SAMPLE_DATA;
  }

  load() {
    try {
      const stored = localStorage.getItem(CONFIG.storageKey);
      return stored ? JSON.parse(stored) : null;
    } catch (e) {
      console.warn('Failed to load data from storage:', e);
      return null;
    }
  }

  save(newData) {
    try {
      this.data = { ...this.data, ...newData };
      this.data.lastUpdated = new Date().toISOString();
      localStorage.setItem(CONFIG.storageKey, JSON.stringify(this.data));
      return true;
    } catch (e) {
      console.error('Failed to save data:', e);
      return false;
    }
  }

  get() {
    return this.data;
  }

  getLastUpdated() {
    if (this.data.lastUpdated) {
      return new Date(this.data.lastUpdated).toLocaleString();
    }
    return 'Never (using sample data)';
  }
}

// ==================== Chart Manager ====================
class ChartManager {
  constructor() {
    this.charts = {};
  }

  createAreaChart(canvasId, labels, data, label, color) {
    const ctx = document.getElementById(canvasId);
    if (!ctx) return null;

    // Destroy existing chart if it exists
    if (this.charts[canvasId]) {
      this.charts[canvasId].destroy();
    }

    this.charts[canvasId] = new Chart(ctx, {
      type: 'line',
      data: {
        labels: labels,
        datasets: [{
          label: label,
          data: data,
          borderColor: color,
          backgroundColor: `${color}20`,
          fill: true,
          tension: 0.4,
          pointRadius: 0,
          pointHoverRadius: 6,
          pointHoverBackgroundColor: color,
          pointHoverBorderColor: '#fff',
          pointHoverBorderWidth: 2
        }]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
          legend: { display: false },
          tooltip: {
            backgroundColor: '#1E293B',
            titleColor: '#F8FAFC',
            bodyColor: '#94A3B8',
            borderColor: '#334155',
            borderWidth: 1,
            cornerRadius: 8,
            padding: 12
          }
        },
        scales: {
          x: {
            grid: { color: CONFIG.chartColors.grid, drawBorder: false },
            ticks: { color: CONFIG.chartColors.text, font: { family: 'Fira Code' } }
          },
          y: {
            grid: { color: CONFIG.chartColors.grid, drawBorder: false },
            ticks: { color: CONFIG.chartColors.text, font: { family: 'Fira Code' } },
            beginAtZero: true
          }
        },
        interaction: {
          intersect: false,
          mode: 'index'
        }
      }
    });

    return this.charts[canvasId];
  }

  createDoughnutChart(canvasId, labels, data, colors) {
    const ctx = document.getElementById(canvasId);
    if (!ctx) return null;

    if (this.charts[canvasId]) {
      this.charts[canvasId].destroy();
    }

    this.charts[canvasId] = new Chart(ctx, {
      type: 'doughnut',
      data: {
        labels: labels,
        datasets: [{
          data: data,
          backgroundColor: colors,
          borderColor: '#1E293B',
          borderWidth: 3,
          hoverBorderColor: '#334155'
        }]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        cutout: '65%',
        plugins: {
          legend: { display: false },
          tooltip: {
            backgroundColor: '#1E293B',
            titleColor: '#F8FAFC',
            bodyColor: '#94A3B8',
            borderColor: '#334155',
            borderWidth: 1,
            cornerRadius: 8,
            padding: 12
          }
        }
      }
    });

    return this.charts[canvasId];
  }
}

// ==================== UI Manager ====================
class UIManager {
  constructor(dashboardData, chartManager) {
    this.data = dashboardData;
    this.charts = chartManager;
  }

  updateMetric(elementId, value, changeId = null, changeValue = null) {
    const el = document.getElementById(elementId);
    if (el) {
      el.textContent = value;
      el.classList.remove('loading');
    }
    
    if (changeId && changeValue) {
      const changeEl = document.getElementById(changeId);
      if (changeEl) {
        changeEl.textContent = changeValue;
      }
    }
  }

  updateAllMetrics() {
    const d = this.data.get();
    
    // Google Analytics
    this.updateMetric('gaVisitors', d.ga.visitors.toLocaleString(), 'gaVisitorsChange', d.ga.visitorsChange);
    this.updateMetric('gaPageViews', d.ga.pageViews.toLocaleString(), 'gaPageViewsChange', d.ga.pageViewsChange);
    this.updateMetric('gaAvgSession', d.ga.avgSession, 'gaAvgSessionChange', d.ga.avgSessionChange);
    this.updateMetric('gaBounceRate', d.ga.bounceRate + '%', 'gaBounceRateChange', d.ga.bounceRateChange);
    
    // Meta Pixel
    this.updateMetric('metaEvents', d.meta.events.toLocaleString(), 'metaEventsChange', d.meta.eventsChange);
    this.updateMetric('metaPageViews', d.meta.pageViews.toLocaleString(), 'metaPageViewsChange', d.meta.pageViewsChange);
    this.updateMetric('metaLeads', d.meta.leads, 'metaLeadsChange', d.meta.leadsChange);
    this.updateMetric('metaMatchQuality', d.meta.matchQuality, 'metaMatchQualityChange', d.meta.matchQualityChange);
    
    // Revenue
    this.updateMetric('totalRevenue', '$' + d.revenue.total.toLocaleString(), 'revenueChange', d.revenue.totalChange);
    this.updateMetric('bookingInquiries', d.revenue.inquiries, 'inquiriesChange', d.revenue.inquiriesChange);
    this.updateMetric('conversionRate', d.revenue.conversionRate + '%', 'conversionChange', d.revenue.conversionChange);
    
    // Funnel
    this.updateMetric('funnelVisitors', d.funnel.visitors.toLocaleString());
    this.updateMetric('funnelPropertyViews', d.funnel.propertyViews.toLocaleString());
    this.updateMetric('funnelInquiries', d.funnel.inquiries);
    this.updateMetric('funnelBookings', d.funnel.bookings);
    
    // Last updated
    document.getElementById('lastUpdated').textContent = 'Last updated: ' + this.data.getLastUpdated();
  }

  renderPropertyCards() {
    const grid = document.getElementById('propertyGrid');
    if (!grid) return;

    const properties = this.data.get().properties;
    
    grid.innerHTML = properties.map(prop => `
      <div class="property-card">
        <div class="property-header">
          <span class="property-name">${prop.name}</span>
          ${prop.badge ? `<span class="property-badge">${prop.badge}</span>` : ''}
        </div>
        <div class="property-stats">
          <div class="property-stat">
            <span class="property-stat-value">${prop.views}</span>
            <span class="property-stat-label">Views</span>
          </div>
          <div class="property-stat">
            <span class="property-stat-value">${prop.inquiries}</span>
            <span class="property-stat-label">Inquiries</span>
          </div>
          <div class="property-stat">
            <span class="property-stat-value">${prop.bookings}</span>
            <span class="property-stat-label">Bookings</span>
          </div>
        </div>
      </div>
    `).join('');
  }

  renderSourcesList() {
    const list = document.getElementById('sourcesList');
    if (!list) return;

    const sources = this.data.get().sources;
    
    list.innerHTML = sources.map(src => `
      <div class="source-item">
        <span class="source-color" style="background: ${src.color}"></span>
        <span class="source-name">${src.name}</span>
        <span class="source-value">${src.value.toLocaleString()}</span>
        <span class="source-percent">${src.percent}%</span>
      </div>
    `).join('');
  }

  renderCharts() {
    const d = this.data.get();
    
    // GA Traffic Chart
    this.charts.createAreaChart(
      'gaTrafficChart',
      d.dateLabels,
      d.ga.trafficTrend,
      'Visitors',
      CONFIG.chartColors.primary
    );
    
    // Meta Events Chart
    this.charts.createAreaChart(
      'metaEventsChart',
      d.dateLabels,
      d.meta.eventsTrend,
      'Events',
      '#1877F2'
    );
    
    // Sources Chart
    const sources = d.sources;
    this.charts.createDoughnutChart(
      'sourcesChart',
      sources.map(s => s.name),
      sources.map(s => s.value),
      sources.map(s => s.color)
    );
  }

  renderAll() {
    this.updateAllMetrics();
    this.renderPropertyCards();
    this.renderSourcesList();
    this.renderCharts();
  }
}

// ==================== Modal Manager ====================
class ModalManager {
  constructor(dashboardData, uiManager) {
    this.data = dashboardData;
    this.ui = uiManager;
    this.modal = document.getElementById('configModal');
    this.form = document.getElementById('dataForm');
    
    this.bindEvents();
  }

  bindEvents() {
    // Open modal on refresh button (for manual data entry)
    document.getElementById('refreshBtn').addEventListener('click', () => {
      this.open();
    });
    
    // Close modal
    document.getElementById('closeModal').addEventListener('click', () => {
      this.close();
    });
    
    // Close on backdrop click
    this.modal.addEventListener('click', (e) => {
      if (e.target === this.modal) {
        this.close();
      }
    });
    
    // Form submit
    this.form.addEventListener('submit', (e) => {
      e.preventDefault();
      this.saveData();
    });
  }

  open() {
    this.modal.classList.add('active');
    this.populateForm();
  }

  close() {
    this.modal.classList.remove('active');
  }

  populateForm() {
    const d = this.data.get();
    
    document.getElementById('inputGaVisitors').value = d.ga.visitors || '';
    document.getElementById('inputGaPageViews').value = d.ga.pageViews || '';
    document.getElementById('inputGaAvgSession').value = d.ga.avgSession || '';
    document.getElementById('inputGaBounceRate').value = d.ga.bounceRate || '';
    document.getElementById('inputMetaEvents').value = d.meta.events || '';
    document.getElementById('inputMetaLeads').value = d.meta.leads || '';
    document.getElementById('inputRevenue').value = d.revenue.total || '';
    document.getElementById('inputInquiries').value = d.revenue.inquiries || '';
  }

  saveData() {
    const newData = {
      ga: {
        ...this.data.get().ga,
        visitors: parseInt(document.getElementById('inputGaVisitors').value) || 0,
        pageViews: parseInt(document.getElementById('inputGaPageViews').value) || 0,
        avgSession: document.getElementById('inputGaAvgSession').value || '0:00',
        bounceRate: parseFloat(document.getElementById('inputGaBounceRate').value) || 0
      },
      meta: {
        ...this.data.get().meta,
        events: parseInt(document.getElementById('inputMetaEvents').value) || 0,
        leads: parseInt(document.getElementById('inputMetaLeads').value) || 0
      },
      revenue: {
        ...this.data.get().revenue,
        total: parseInt(document.getElementById('inputRevenue').value) || 0,
        inquiries: parseInt(document.getElementById('inputInquiries').value) || 0
      }
    };
    
    this.data.save(newData);
    this.ui.renderAll();
    this.close();
  }
}

// ==================== Date Range Handler ====================
class DateRangeHandler {
  constructor() {
    this.buttons = document.querySelectorAll('.date-btn');
    this.currentRange = 7;
    this.bindEvents();
  }

  bindEvents() {
    this.buttons.forEach(btn => {
      btn.addEventListener('click', () => {
        this.buttons.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        this.currentRange = parseInt(btn.dataset.range);
        // In a real implementation, this would re-fetch data for the new range
        console.log(`Date range changed to: ${this.currentRange} days`);
      });
    });
  }
}

// ==================== Initialize Dashboard ====================
document.addEventListener('DOMContentLoaded', () => {
  // Initialize managers
  const dashboardData = new DashboardData();
  const chartManager = new ChartManager();
  const uiManager = new UIManager(dashboardData, chartManager);
  const modalManager = new ModalManager(dashboardData, uiManager);
  const dateRangeHandler = new DateRangeHandler();
  
  // Initial render
  uiManager.renderAll();
  
  // Log initialization
  console.log('🌊 Seascape Analytics Dashboard initialized');
  console.log('💡 Click the refresh button to manually update data');
});
