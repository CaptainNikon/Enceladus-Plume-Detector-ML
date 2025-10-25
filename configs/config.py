# ===================================================
# Configuration and utility settings adapted for this notebook
# Original source: Shahab Fatemi, Associate Professor of Computational Space Physics
#                  Department of Physics, Umeå University, Sweden
# 
# Description:
# This configuration file and structure are adapted from work by Shahab Fatemi
# for educational and research use in computational space physics.
# Updated and customized by Jeremias Siehr, 25.10.2025.
# ===================================================

import matplotlib
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from cycler import cycler

# ===================================================
# Display Settings
# ===================================================
matplotlib.rcParams.update({
    'figure.dpi': 200,                        # Modern high-DPI rendering
    'figure.figsize': (6, 4),                 # Default figure size
    'figure.autolayout': True,                # Auto layout management
    'figure.constrained_layout.use': False,   # Avoid engine conflict by default
    'axes.formatter.use_mathtext': True,      # Modern scientific formatting
})

# ===================================================
# Font & Aesthetic Styling
# ===================================================
matplotlib.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['DejaVu Serif', 'Times New Roman', 'Cambria'],
    'axes.titlesize': 16,
    'axes.labelsize': 14,
    'axes.linewidth': 1.2,
    'axes.labelpad': 6,
    'grid.alpha': 0.4,
    'xtick.labelsize': 12,
    'ytick.labelsize': 12,
    'text.kerning_factor': 6,
})

# ===================================================
# Grid Settings
# ===================================================
matplotlib.rcParams.update({
    'axes.grid': True,
    'grid.color': 'gray',
    'grid.linestyle': '--',
    'grid.linewidth': 0.6,
})

# ===================================================
# Line & Marker Properties
# ===================================================
matplotlib.rcParams.update({
    'lines.linewidth': 2.0,
    'lines.markersize': 7,
    'markers.fillstyle': 'full',
})

# ===================================================
# Legend Configuration
# ===================================================
matplotlib.rcParams.update({
    'legend.fontsize': 12,
    'legend.frameon': True,
    'legend.loc': 'best',
    'legend.framealpha': 0.8,
    'legend.handletextpad': 0.5,
})

# ===================================================
# Color Cycle (uses 'tab10' colormap)
# ===================================================
cmap = cm.get_cmap('tab10', 10)
colors = [cmap(i) for i in range(cmap.N)]
matplotlib.rcParams['axes.prop_cycle'] = cycler(color=colors)

# ===================================================
# Save Figure Defaults
# ===================================================
matplotlib.rcParams.update({
    'savefig.dpi': 300,
    'savefig.format': 'pdf',
    'savefig.bbox': 'tight',     # Prevent cropped labels
    'savefig.transparent': False,
    'savefig.pad_inches': 0.1,
})

# ===================================================
# Recommended Usage
# ===================================================
# Use constrained_layout when creating subplots:
#     fig, axes = plt.subplots(nrows=2, ncols=2, constrained_layout=True)
#
# Or manually call:
#     plt.tight_layout()
# ===================================================
