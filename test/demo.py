# app.py
from textual.app import App, ComposeResult
from textual.containers import Container
from textual.widgets import Header, Footer

from chartinglib import ChartWidget

class DemoChartApp(App):
    CSS_PATH = "app.tcss"  # Optional: Add a CSS file for layout/styling

    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        yield Footer()

        # Sample data (e.g., line chart)
        raw_data = {
            "x": [1, 2, 3, 4, 5],
            "y": [10, 20, 30, 25, 15]
        }

        # Process it (optional depending on your chartinglib design)
        #processor = DataProcessing(chart_type="line")
        #processed_data = processor.process(raw_data)

        # ChartWidget expects processed data and chart type
        chart = ChartWidget(raw_data=raw_data, chart_type="line", widget_id="linechart", title="Demo Chart",)

        yield Container(chart)

if __name__ == "__main__":
    app = DemoChartApp()
    app.run()
