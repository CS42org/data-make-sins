"""Shared plotting style for the Data Make Sins notebooks."""
from pathlib import Path
import matplotlib as mpl

BLUE = "#0071e3"
RED = "#ff3b30"
AMBER = "#ff9f0a"
GREY = "#c7c7cc"
INK = "#1d1d1f"
INK2 = "#6e6e73"
LIGHT = "#f5f5f7"


def find_root():
    here = Path.cwd()
    for candidate in [here, *here.parents]:
        if (candidate / "src").exists() and (candidate / "notebooks").exists():
            return candidate
    return here


ROOT = find_root()
FIG = ROOT / "figures"
DATA = ROOT / "data"


def style():
    mpl.rcParams.update({
        "figure.figsize": (8, 4.5),
        "figure.dpi": 100,
        "savefig.dpi": 160,
        "font.family": "sans-serif",
        "font.sans-serif": ["SF Pro Text", "Helvetica Neue", "Helvetica", "Arial", "DejaVu Sans"],
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.edgecolor": GREY,
        "axes.labelcolor": INK2,
        "axes.titlesize": 14,
        "axes.titleweight": "bold",
        "axes.titlelocation": "left",
        "xtick.color": INK2,
        "ytick.color": INK2,
        "text.color": INK,
        "legend.frameon": False,
    })


def save(fig, name):
    FIG.mkdir(exist_ok=True)
    path = FIG / name
    fig.savefig(path, bbox_inches="tight", facecolor="white")
    return path
