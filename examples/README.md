# Examples

Run these from the repository root with Roc:

```sh
roc examples/01-text-and-tables.roc
roc examples/02-slider.roc
roc examples/03-chart.roc
```

1. **Text and tables:** create a Markdown greeting and a small table.
2. **Slider:** read a control's default value and use it in a calculation.
3. **Chart:** construct a Plotly figure without an additional package dependency.

These ordinary Roc apps pin the published release recorded in `package-url.txt`.
Roc downloads and caches that release on first use. They print readable summaries;
ordinary Roc does not open a chart or interactive slider. To see the graphical
notebook experience, try [Roclet's demos](https://ageron.github.io/roclet/).

`python3 tools/test-package.py` also runs every example against the extracted
release archive, checking the package users will actually download.
