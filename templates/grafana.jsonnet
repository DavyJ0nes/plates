local grafana = import '../lib/grafonnet/grafana.libsonnet';

local dashboard = grafana.dashboard;
local prometheus = grafana.prometheus;
local row = grafana.row;
local template = grafana.template;

// ***** Variables ***** //

local vars = {
  Datasource: grafana.template.datasource(
    'PROMETHEUS_DS',
    'prometheus',
    'prometheus',
    hide='all',
  ),

  Interval: grafana.template.interval(
    'interval',
    '1m,5m,10m,30m,1h',
    '1m',
  ),
};

// ***** Metrics ***** //

local cpuMetrics = {};

// ***** Rows ***** //

local topRow = row.new(
  title='Info',
  height='60px'
)
               .addPanels([]);

// ***** Dashboard ***** //

dashboard.new(
  'Sample Dashboard',
  refresh='30s',
  time_from='now-30m',
  tags=['prometheus', 'sample']
)
.addTemplate(vars.Datasource)
.addTemplate(vars.Interval)
.addRows(
  [
    topRow,
  ]
)
