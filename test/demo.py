# app.py
from textual.app import App, ComposeResult
from textual.containers import Container
from textual.widgets import Header, Footer

from chartinglib import ChartWidget

class DemoChartApp(App):
    CSS_PATH = "app.tcss"  # Optional: Add a CSS file for layout/styling

    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        yield ChartWidget(chart_type="bar", title="GDP Growth", widget_id="gdp_growth")
        yield Footer()



    async def on_mount(self):
        chart_widget = self.query_one("#gdp_growth", ChartWidget)
        # Sample data (e.g., line chart)
        chart_data = {
            "labels": [1, 2, 3, 4, 5],
            "values": [10, 20, 30, 25, 15]
        }

        chart_widget.update_chart(new_data=chart_data, new_title=f"GDP_Growth")

if __name__ == "__main__":
    app = DemoChartApp()
    app.run()
