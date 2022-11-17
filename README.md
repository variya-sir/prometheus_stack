# Prometheus stack
Introduction to Monitoring system with Prometheus stacks
## Components
- **Exporters**: scrape and expose metrics (time series data) from services
- **Prometheus server**: store metrics
- **Alertmanager**: handle alerts based on defined rules that sends from Prometheus, and route them to recievers (i.e. email)
- **Grafana**: for data visualization

## Development
- Run `make install` to generate .env file and replace your prefer variables here
- Run `make run` to start all prometheys stacks

Note: Some exporters are PoCs and not included for starting it via `make run`
## References
- https://prometheus.io/docs/introduction/overview/
- https://github.com/kaihendry/pingprom
