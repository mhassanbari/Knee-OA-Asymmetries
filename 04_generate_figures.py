import matplotlib.pyplot as plt
import numpy as np

# Apply clean figure formatting styling
plt.rcParams.update({'font.sans-serif': 'DejaVu Sans', 'font.size': 11})

def plot_figure1_asymmetry_comparison():
    fig, ax = plt.subplots(figsize=(6, 4), dpi=300)
    
    conditions = ['Non-Fatigued', 'Fatigued']
    means = [25.5, 34.2]
    sds = [14.1, 15.8]
    colors = ['#808080', '#1f3a60']
    
    bars = ax.bar(conditions, means, yerr=sds, capsize=6, color=colors, width=0.5, edgecolor='black', linewidth=0.5)
    
    ax.set_ylabel('Asymmetry Index (%)')
    ax.set_title('Inter-Limb Load Asymmetry by Condition', pad=12)
    ax.set_ylim(0, 55)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    
    ax.text(0.5, 48, r'$p < 0.001$', ha='center', va='center', fontsize=11, fontstyle='italic')
    
    # Annotate bar tops
    for bar, mean in zip(bars, means):
        ax.text(bar.get_x() + bar.get_width()/2.0, mean + 2.0, f'{mean:.1f}%', ha='center', va='bottom', fontweight='bold')
        
    plt.tight_layout()
    plt.savefig('results/figures/figure1_asymmetry_comparison.png')
    plt.close()

if __name__ == "__main__":
    plot_figure1_asymmetry_comparison()
    print("Figure generated successfully.")