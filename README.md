# ChartingLib 📈

**ChartingLib** is a modern TUI (Textual User Interface) Python library built with [Textual](https://github.com/Textualize/textual) and [Plotly](https://plotly.com/python/), designed for interactive data visualization directly in your terminal.

It provides a rich, responsive interface to display a variety of charts such as Line, Bar, Scatter, Candlestick, GDP trends, and more.

---

## ✨ Features

- 📊 Interactive Plotly charts inside your terminal
- 🧠 Automatic data generation or loading using `DataProcessing`
- 🧩 Modular chart widget (`ChartWidget`) for easy embedding
- 🎨 Sidebar for selecting different chart types
- 💻 Clean TUI with keyboard navigation (powered by Textual)

---

## 📦 Installation

```bash
pip install chartinglib
```

---

## 🚀 Usage

Here’s a simple example using `ChartWidget` in a Textual app:

```python
from textual.app import App, ComposeResult
from textual.containers import Container
from chartinglib import ChartWidget, DataProcessing

class DemoChartApp(App):
    def compose(self) -> ComposeResult:
        raw_data = DataProcessing("line").process()
        chart = ChartWidget(chart_type="line", data=raw_data)
        yield Container(chart)

if __name__ == "__main__":
    app = DemoChartApp()
    app.run()
```

---

## 📈 Supported Chart Types

- `line`
- `bar`
- `scatter`
- `candlestick`
- `gdp`
- `revenue`
- `multiple_lines`
- `mixed_bar_line`

---

## 🛠 Development

```bash
git clone https://github.com/yourusername/chartinglib
cd chartinglib
pip install -e .[dev]
```

To run the example app:

```bash
python -m chartinglib.app
```

---

## 📄 License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

---

## 👤 Author

**Your Name**  
[GitHub](https://github.com/yourusername)

---

## 🙏 Acknowledgments

- [Textual by Textualize](https://github.com/Textualize/textual)
- [Plotly for Python](https://plotly.com/python/)
