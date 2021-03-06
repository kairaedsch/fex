import logging
from core import prepare
from ..parsec.plot import process_type

BENCH_NAME = 'phoenix'
EXP_NAME = BENCH_NAME
BENCHMARK_ORDER = (
    "linear_regression",
    "string_match",
    "matrix_multiply",
    "histogram",
    "kmeans",
    "pca",
    "word_count",
)

OVERFLOWS = {
    "perf": (
        (-0.45, 3, "5.3",),
        (0.55, 3, "7.9",),
        (1.55, 3, "5.9",),
        (2.55, 3.3, "4.0",),
        (3.55, 3.3, "9.5",),
        (6.61, 3.3, "4.5",),
    ),
}


def main(t="perf"):
    logging.info("Processing data")

    # common processing
    df = prepare.process_results(t)
    plot_args = {
        "ylim": (0.85, 3.5),
        "vline_position": 6.6,
        "title": "Phoenix",
        "figsize" : (12, 2.5),
        "text_points": OVERFLOWS.get(t, ()),
    }
    plot, columns = process_type(t, df, plot_args, BENCHMARK_ORDER)

    if t == "multi":
        plot_args.update({
            "ylim": (0.51, 4.5),
        })

    plot.get_data(df, columns)
    plot.build_plot(**plot_args)
    plot.save_plot("%s_%s.pdf" % (BENCH_NAME, t))
