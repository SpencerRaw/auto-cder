"""Generate publication-quality table images for EvoScientist Tables 1-3."""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

# ── Global style ──────────────────────────────────────────────────────────
plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 8.5,
    "axes.titlesize": 10,
    "axes.titleweight": "bold",
    "figure.facecolor": "white",
    "axes.facecolor": "white",
})

# ── Color palette ─────────────────────────────────────────────────────────
GREEN  = "#2E7D32"
RED    = "#C62828"
GRAY   = "#757575"
BLUE   = "#1565C0"
WHITE  = "#FFFFFF"
LIGHT_GREEN = "#E8F5E9"
LIGHT_RED   = "#FFEBEE"
LIGHT_GRAY  = "#F5F5F5"
HEADER_BG   = "#263238"
HEADER_FG   = "#FFFFFF"

def draw_table(ax, title, headers, rows, col_widths, highlight_col=None):
    """Draw a styled table on the given axes."""
    n_rows = len(rows)
    n_cols = len(headers)

    ax.set_xlim(0, sum(col_widths))
    ax.set_ylim(0, (n_rows + 1) * 0.55)
    ax.axis("off")

    y_top = (n_rows + 1) * 0.55

    # ── Title ──
    ax.text(sum(col_widths) / 2, y_top + 0.25, title,
            ha="center", va="center", fontsize=11, fontweight="bold", color="#212121")

    # ── Header row ──
    x = 0
    for j, (hdr, w) in enumerate(zip(headers, col_widths)):
        rect = mpatches.FancyBboxPatch(
            (x, y_top - 0.55), w, 0.55,
            boxstyle="square,pad=0", facecolor=HEADER_BG, edgecolor="#37474F", linewidth=0.5
        )
        ax.add_patch(rect)
        ax.text(x + w / 2, y_top - 0.275, hdr.replace("\\n", "\n"),
                ha="center", va="center", fontsize=7.8, fontweight="bold",
                color=HEADER_FG, linespacing=1.2)
        x += w

    # ── Data rows ──
    for i, row in enumerate(rows):
        y = y_top - (i + 1) * 0.55 - 0.55
        bg = LIGHT_GRAY if i % 2 == 0 else WHITE
        # Section header rows
        if isinstance(row[0], str) and row[0].startswith("▶"):
            x = 0
            for j, w in enumerate(col_widths):
                rect = mpatches.FancyBboxPatch(
                    (x, y), w, 0.55,
                    boxstyle="square,pad=0", facecolor="#ECEFF1", edgecolor="#CFD8DC", linewidth=0.5
                )
                ax.add_patch(rect)
                val = row[j] if j < len(row) else ""
                ax.text(x + w / 2, y + 0.275, str(val).replace("▶ ", ""),
                        ha="center" if j > 0 else "left", va="center",
                        fontsize=8, fontweight="bold", color="#37474F")
                x += w
            continue

        x = 0
        for j, (val, w) in enumerate(zip(row, col_widths)):
            if j >= len(row):
                x += w
                continue

            s_val = str(val)
            # Determine cell style
            cell_bg = bg
            cell_fg = "#212121"
            cell_fw = "normal"

            if s_val.endswith("∗") or s_val.endswith("*"):
                cell_fw = "bold"
                cell_fg = "#1B5E20" if (j > 0 and "Win" in headers[j]) else "#212121"

            if highlight_col is not None and j == highlight_col:
                try:
                    v = float(s_val.replace("+", "").replace("−", "-").replace("∗", "").replace("*", ""))
                    if v > 0:
                        cell_bg = LIGHT_GREEN
                        cell_fg = GREEN
                        cell_fw = "bold"
                    elif v < 0:
                        cell_bg = LIGHT_RED
                        cell_fg = RED
                        cell_fw = "bold"
                except ValueError:
                    pass

            rect = mpatches.FancyBboxPatch(
                (x, y), w, 0.55,
                boxstyle="square,pad=0", facecolor=cell_bg, edgecolor="#E0E0E0", linewidth=0.3
            )
            ax.add_patch(rect)

            ha = "center" if j > 0 else "left"
            x_text = x + w / 2 if j > 0 else x + 0.08
            ax.text(x_text, y + 0.275, s_val,
                    ha=ha, va="center", fontsize=7.5, fontweight=cell_fw,
                    color=cell_fg)
            x += w

    return ax


# ═══════════════════════════════════════════════════════════════════════════
# TABLE 1 — LLM Evaluation (Gemini-3-flash) of Scientific Idea Generation
# ═══════════════════════════════════════════════════════════════════════════
def make_table1():
    title = "Table 1: LLM Evaluation (Gemini-3-flash) of Scientific Idea Generation"
    headers = [
        "Method",
        "Novelty\nWin / Tie / Lose",
        "Feasibility\nWin / Tie / Lose",
        "Relevance\nWin / Tie / Lose",
        "Clarity\nWin / Tie / Lose",
        "Avg. Gap"
    ]
    col_widths = [2.2, 1.8, 1.8, 1.8, 1.8, 1.0]

    rows = [
        ["▶ Open-sourced Systems", "", "", "", "", ""],
        [
            "Evo vs Virtual Scientist",
            "96.67 / 3.33 / 0.00*",
            "93.33 / 6.67 / 0.00*",
            "90.00 / 6.67 / 3.33*",
            "96.67 / 3.33 / 0.00*",
            "+93.34"
        ],
        [
            "Evo vs AI-Researcher",
            "96.67 / 3.33 / 0.00*",
            "90.00 / 0.00 / 10.00*",
            "86.67 / 10.00 / 3.33*",
            "93.34 / 3.33 / 3.33*",
            "+87.50"
        ],
        [
            "Evo vs InternAgent",
            "73.33 / 16.67 / 10.00*",
            "93.33 / 0.00 / 6.67*",
            "86.67 / 13.33 / 0.00*",
            "96.67 / 3.33 / 0.00*",
            "+83.33"
        ],
        [
            "Evo vs AI Scientist-v2",
            "63.33 / 16.67 / 20.00*",
            "53.33 / 6.67 / 40.00*",
            "36.67 / 50.00 / 13.33*",
            "56.67 / 23.33 / 20.00*",
            "+29.17"
        ],
        ["▶ Commercial Systems", "", "", "", "", ""],
        [
            "Evo vs Hypogenic",
            "93.33 / 6.67 / 0.00*",
            "83.34 / 3.33 / 13.33*",
            "70.00 / 23.33 / 6.67*",
            "96.67 / 3.33 / 0.00*",
            "+80.83"
        ],
        [
            "Evo vs Novix",
            "90.00 / 6.67 / 3.33*",
            "53.33 / 10.00 / 36.67*",
            "46.67 / 36.66 / 16.67*",
            "70.67 / 10.00 / 20.00*",
            "+46.00"
        ],
        [
            "Evo vs K-Dense",
            "86.67 / 3.33 / 10.00*",
            "56.67 / 13.33 / 30.00*",
            "43.33 / 36.67 / 20.00*",
            "76.67 / 13.33 / 10.00*",
            "+54.50"
        ],
        ["", "", "", "", "", ""],
        [
            "* p < 0.05 (sign test). Win/Tie/Lose = % of 30 queries where EvoScientist won/tied/lost.",
            "", "", "", "", ""
        ],
    ]

    fig, ax = plt.subplots(figsize=(12.5, 5.8))
    draw_table(ax, title, headers, rows, col_widths, highlight_col=5)
    fig.tight_layout(pad=0.5)
    fig.savefig("/Users/apple/Desktop/auto-cder/assets/table1_llm_evaluation.png",
                dpi=200, bbox_inches="tight", facecolor="white", edgecolor="none")
    plt.close(fig)
    print("✅ Table 1 saved → assets/table1_llm_evaluation.png")


# ═══════════════════════════════════════════════════════════════════════════
# TABLE 2 — Human Evaluation of Scientific Idea Generation
# ═══════════════════════════════════════════════════════════════════════════
def make_table2():
    title = "Table 2: Human Evaluation of Scientific Idea Generation (3 PhD Annotators)"
    headers = [
        "Method",
        "Novelty\nWin / Tie / Lose",
        "Feasibility\nWin / Tie / Lose",
        "Relevance\nWin / Tie / Lose",
        "Clarity\nWin / Tie / Lose",
        "Avg. Gap"
    ]
    col_widths = [2.2, 1.8, 1.8, 1.8, 1.8, 1.0]

    rows = [
        [
            "Evo vs InternAgent",
            "66.67 / 23.33 / 10.00*",
            "96.67 / 3.33 / 0.00*",
            "90.00 / 0.00 / 10.00*",
            "93.33 / 6.67 / 0.00*",
            "+84.17"
        ],
        [
            "Evo vs AI Scientist-v2",
            "73.33 / 10.00 / 16.67*",
            "50.00 / 16.67 / 33.33*",
            "43.33 / 50.00 / 6.67*",
            "53.33 / 20.00 / 26.67*",
            "+34.16"
        ],
        [
            "Evo vs Novix",
            "93.33 / 0.00 / 6.67*",
            "56.67 / 6.66 / 36.67*",
            "36.67 / 60.00 / 3.33*",
            "73.33 / 10.00 / 16.67*",
            "+49.17"
        ],
        [
            "Evo vs K-Dense",
            "96.67 / 3.33 / 0.00*",
            "53.33 / 26.67 / 20.00*",
            "40.00 / 43.33 / 16.67*",
            "53.34 / 43.33 / 3.33*",
            "+50.84"
        ],
    ]

    fig, ax = plt.subplots(figsize=(12.5, 3.5))
    draw_table(ax, title, headers, rows, col_widths, highlight_col=5)
    fig.tight_layout(pad=0.5)
    fig.savefig("/Users/apple/Desktop/auto-cder/assets/table2_human_evaluation.png",
                dpi=200, bbox_inches="tight", facecolor="white", edgecolor="none")
    plt.close(fig)
    print("✅ Table 2 saved → assets/table2_human_evaluation.png")


# ═══════════════════════════════════════════════════════════════════════════
# TABLE 3 — Ablation Study (Gemini-3-flash)
# ═══════════════════════════════════════════════════════════════════════════
def make_table3():
    title = "Table 3: Ablation Study — Self-Evolution Components (Gemini-3-flash Judge)"
    headers = [
        "Variant",
        "Novelty\nWin / Tie / Lose",
        "Feasibility\nWin / Tie / Lose",
        "Relevance\nWin / Tie / Lose",
        "Clarity\nWin / Tie / Lose",
        "Avg. Gap"
    ]
    col_widths = [2.2, 1.8, 1.8, 1.8, 1.8, 1.0]

    rows = [
        [
            "− IDE  vs  Evo (full)",
            "16.67 / 16.67 / 66.67",
            "20.00 / 30.00 / 50.00",
            "23.33 / 50.00 / 26.67",
            "23.33 / 46.67 / 30.00",
            "−22.50"
        ],
        [
            "− IVE  vs  Evo (full)",
            "30.00 / 26.67 / 43.33",
            "10.00 / 26.67 / 63.33",
            "30.00 / 46.67 / 23.33",
            "16.67 / 46.67 / 36.67",
            "−20.00"
        ],
        [
            "− all  vs  Evo (full)",
            "10.00 / 10.00 / 80.00",
            "3.33 / 13.33 / 83.33",
            "16.67 / 46.67 / 36.67",
            "20.00 / 46.67 / 33.33",
            "−45.83"
        ],
        ["", "", "", "", "", ""],
        [
            "IDE = Idea Direction Evolution. IVE = Idea Validation Evolution. −all = no self-evolution.",
            "", "", "", "", ""
        ],
    ]

    fig, ax = plt.subplots(figsize=(12.5, 3.2))
    draw_table(ax, title, headers, rows, col_widths, highlight_col=5)
    fig.tight_layout(pad=0.5)
    fig.savefig("/Users/apple/Desktop/auto-cder/assets/table3_ablation.png",
                dpi=200, bbox_inches="tight", facecolor="white", edgecolor="none")
    plt.close(fig)
    print("✅ Table 3 saved → assets/table3_ablation.png")


# ── Run ────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    make_table1()
    make_table2()
    make_table3()
    print("\n🎯 All 3 table images generated in assets/")
