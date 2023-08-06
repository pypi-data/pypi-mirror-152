# pandaslearn

`pandaslearn` is a small wrapper on top of `scikit-learn` to automate common modeling tasks.

* Create `Trainer` instance with `Dataset` and `Model` instances, `__init__()` in `Trainer` instance should populate `Dataset` and `Model` instance's `logger` attributes. Methods on `Dataset` and `Model` should be called after that, so that everything gets logged appropriately.
# TODO

* TODO: visualization: add barcharts (plotnine)
* TODO: visualization: add histograms (plotnine)
* TODO: visualization: add scatterplots (plotnine)
* TODO: visualization: add lineplots (plotnine)
* TODO: visualization: add boxplots (plotnine)
* TODO: visualization: add violin plots (plotnine)
* TODO: visualization: add function to change theme (xkcd, ?)
* TODO: add a `geo` namespace (+ feature engineering, plots)
* TODO: add tests against a few standard fixtures (precompute values and test against them)
* TODO: integrate missingno package: functions to only compute/sort nullity
* TODO: integrate missingno package: plotnine functions matching missingno plot(including geo)
* TODO: integrate missingno package: timeseries nullity plots (just plot all timelines with gaps)
* TODO: pandas-profiling has a lot of useful analysis useful for ml. Integrate those (provide textual outcomes like dicts or dfs instead of plot)
* TODO: future integration targets: https://compose.alteryx.com/en/stable/
* TODO: future integration targets: https://featuretools.alteryx.com/en/stable/
* TODO: future integration targets: https://evalml.alteryx.com/en/stable/
