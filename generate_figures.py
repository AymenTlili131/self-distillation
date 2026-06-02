"""
Generate figures for the Self-Distillation timeline visualization.
Run this script to create standalone PNG figures.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np

# Set style
plt.style.use('default')
plt.rcParams['figure.dpi'] = 150
plt.rcParams['savefig.dpi'] = 150
plt.rcParams['figure.facecolor'] = 'white'

def create_timeline():
    """Create the main timeline figure."""
    fig, ax = plt.subplots(figsize=(16, 10))
    
    # Paper data: (year, title, authors, key_contribution, y_position, color)
    papers = [
        (2019, "Be Your Own Teacher", "Zhang et al.", "First systematic self-distillation\nfor CNNs - deeper layers teach\nshallow classifiers", 0.85, '#FF6B6B'),
        (2021, "Self-Distillation:\nTowards Efficient and\nCompact Neural Networks", "Zhang et al. (IEEE)", "Multi-classifier architecture\nwith attention modules\nfor model compression", 0.65, '#4ECDC4'),
        (2022, "Revisiting Self-Distillation", "Pham et al.", "Theoretical analysis:\nself-distillation leads to\nflatter loss minima", 0.45, '#45B7D1'),
        (2024, "Self-Distillation Enables\nContinual Learning", "Shenfeld et al.", "On-policy learning from\ndemonstrations without\ncatastrophic forgetting", 0.25, '#96CEB4'),
        (2024, "Embarrassingly Simple\nSelf-Distillation", "Apple Research", "LLM code generation\nimproved by own outputs\nno verifier needed", 0.05, '#FFEAA7'),
        (2024, "Self-Distillation Bridges\nDistribution Gap\nin LM Fine-Tuning", "Yang et al. (ACL)", "SDFT: Mitigates forgetting\nin LLM fine-tuning\nbridges task/prior gap", 0.45, '#DDA0DD')
    ]
    
    # Draw timeline axis
    ax.axhline(y=0.5, xmin=0.05, xmax=0.95, color='#333333', linewidth=3, alpha=0.7)
    
    # Add year markers
    for year in [2019, 2020, 2021, 2022, 2023, 2024, 2025]:
        x_pos = 0.05 + (year - 2019) / 6 * 0.9
        ax.plot([x_pos, x_pos], [0.48, 0.52], 'k-', linewidth=2)
        ax.text(x_pos, 0.42, str(year), ha='center', va='top', fontsize=11, fontweight='bold')
    
    # Draw paper boxes
    for year, title, authors, contribution, y_pos, color in papers:
        x_pos = 0.05 + (year - 2019) / 6 * 0.9
        
        # Draw connection line
        ax.plot([x_pos, x_pos], [0.5, y_pos], color=color, linewidth=2, alpha=0.6, linestyle='--')
        
        # Draw paper box
        box = FancyBboxPatch((x_pos - 0.08, y_pos - 0.08), 0.16, 0.16,
                             boxstyle="round,pad=0.01",
                             facecolor=color, edgecolor='black', linewidth=1.5, alpha=0.9)
        ax.add_patch(box)
        
        # Add text
        ax.text(x_pos, y_pos + 0.05, title, ha='center', va='center', fontsize=9, fontweight='bold', wrap=True)
        ax.text(x_pos, y_pos - 0.05, authors, ha='center', va='center', fontsize=7, style='italic')
        
        # Add contribution text below
        ax.text(x_pos, y_pos - 0.12, contribution, ha='center', va='top', fontsize=7, alpha=0.8)
    
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')
    ax.set_title('Evolution of Self-Distillation Research (2019-2024)', fontsize=16, fontweight='bold', pad=20)
    
    plt.tight_layout()
    plt.savefig('timeline.png', dpi=150, bbox_inches='tight', facecolor='white')
    print("✓ Saved: timeline.png")
    plt.close()

def create_evolution_stages():
    """Create the evolution stages comparison figure."""
    fig, axes = plt.subplots(2, 3, figsize=(16, 10))
    axes = axes.flatten()
    
    stages = [
        ("2015: Traditional KD", "Teacher (Large) → Student (Small)\nDifferent architectures\nExternal teacher required", '#FFB6C1'),
        ("2019: Be Your Own Teacher", "Deep Classifier → Shallow Classifiers\nSame network, different depths\nMulti-classifier architecture", '#FF6B6B'),
        ("2021: Efficient & Compact", "Multi-classifier + Attention\nShallow classifiers with\nattention modules", '#4ECDC4'),
        ("2022: Theoretical Analysis", "Same weights, same architecture\nLoss landscape flattening\nBetter generalization", '#45B7D1'),
        ("2024: Continual Learning", "Demonstration-conditioned\nteaches base model\nOn-policy from demonstrations", '#96CEB4'),
        ("2024: Code Generation", "High-temp sampling\nteaches base model\nNo verifier needed", '#FFEAA7')
    ]
    
    for idx, (title, desc, color) in enumerate(stages):
        ax = axes[idx]
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)
        ax.axis('off')
        
        # Draw background
        rect = FancyBboxPatch((0.5, 0.5), 9, 9, boxstyle="round,pad=0.1",
                             facecolor=color, edgecolor='black', linewidth=2, alpha=0.3)
        ax.add_patch(rect)
        
        # Add title
        ax.text(5, 8.5, title, ha='center', va='center', fontsize=12, fontweight='bold')
        
        # Add description
        ax.text(5, 5, desc, ha='center', va='center', fontsize=10, 
                bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
        
        # Draw simple network diagram based on stage
        if idx == 0:
            # Traditional KD: Two separate networks
            ax.add_patch(plt.Rectangle((2, 2), 2, 3, facecolor='lightblue', edgecolor='black'))
            ax.text(3, 3.5, 'Teacher', ha='center', fontsize=8)
            ax.add_patch(plt.Rectangle((6, 2), 2, 2, facecolor='lightcoral', edgecolor='black'))
            ax.text(7, 3, 'Student', ha='center', fontsize=8)
            ax.annotate('', xy=(6, 3), xytext=(4, 3), arrowprops=dict(arrowstyle='->', lw=2))
        elif idx in [1, 2]:
            # Multi-classifier
            for i, y in enumerate([1.5, 2.5, 3.5]):
                width = 3 - i * 0.3
                ax.add_patch(plt.Rectangle((5-width/2, y), width, 0.8, 
                                          facecolor=plt.cm.Blues(0.3 + i*0.2), edgecolor='black'))
            ax.text(5, 1, 'Shallow→Deep', ha='center', fontsize=8)
        else:
            # Self-loop
            ax.add_patch(plt.Circle((5, 3), 1.5, facecolor='lightyellow', edgecolor='black'))
            ax.text(5, 3, 'Self', ha='center', fontsize=9)
            ax.annotate('', xy=(6.2, 4), xytext=(6.5, 3.5), 
                       arrowprops=dict(arrowstyle='->', lw=2, connectionstyle='arc3,rad=0.3'))
    
    plt.suptitle('Evolution of Self-Distillation Paradigms', fontsize=16, fontweight='bold', y=0.98)
    plt.tight_layout()
    plt.savefig('evolution_stages.png', dpi=150, bbox_inches='tight', facecolor='white')
    print("✓ Saved: evolution_stages.png")
    plt.close()

def create_architecture_diagram():
    """Create a detailed architecture diagram for Be Your Own Teacher."""
    fig, ax = plt.subplots(figsize=(12, 10))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')
    
    # Title
    ax.text(5, 9.5, 'Be Your Own Teacher: Multi-Classifier Architecture', 
            ha='center', fontsize=14, fontweight='bold')
    
    # Input
    ax.add_patch(plt.Rectangle((4, 0.5), 2, 0.8, facecolor='lightgreen', edgecolor='black'))
    ax.text(5, 0.9, 'Input Image', ha='center', va='center', fontsize=9)
    
    # Feature extraction layers
    y_pos = 1.8
    layer_colors = ['#E3F2FD', '#BBDEFB', '#90CAF9', '#64B5F6', '#42A5F5']
    
    for i, color in enumerate(layer_colors):
        width = 3 - i * 0.2
        ax.add_patch(plt.Rectangle((5 - width/2, y_pos + i*0.8), width, 0.6, 
                                   facecolor=color, edgecolor='black'))
        ax.text(5, y_pos + i*0.8 + 0.3, f'Conv Block {i+1}', ha='center', va='center', fontsize=7)
    
    # Shallow classifiers
    classifier_positions = [(2, 3.5), (2, 4.3), (2, 5.1)]
    for i, (x, y) in enumerate(classifier_positions):
        ax.add_patch(plt.Rectangle((x-0.6, y-0.3), 1.2, 0.6, facecolor='#FFCCBC', edgecolor='black'))
        ax.text(x, y, f'Auxiliary\nClassifier {i+1}', ha='center', va='center', fontsize=7)
        # Connection line
        ax.plot([x+0.6, 5-(3-i*0.2)/2], [y, y], 'k--', alpha=0.5, linewidth=1)
    
    # Main classifier
    ax.add_patch(plt.Rectangle((4, 6), 2, 1, facecolor='#FF7043', edgecolor='black', linewidth=2))
    ax.text(5, 6.5, 'Main Classifier\n(Teacher)', ha='center', va='center', fontsize=9, fontweight='bold')
    
    # Distillation arrows
    for i, (x, y) in enumerate(classifier_positions):
        ax.annotate('', xy=(x, y+0.3), xytext=(5, 6),
                   arrowprops=dict(arrowstyle='->', lw=1.5, color='blue', alpha=0.6))
    
    # Loss labels
    ax.text(1, 3.5, 'L_hint + L_distill', ha='center', fontsize=8, color='blue', rotation=90)
    ax.text(5, 7.5, 'L_label + L_distill', ha='center', fontsize=9, color='red', fontweight='bold')
    
    plt.tight_layout()
    plt.savefig('architecture_be_your_own_teacher.png', dpi=150, bbox_inches='tight', facecolor='white')
    print("✓ Saved: architecture_be_your_own_teacher.png")
    plt.close()

def create_loss_landscape():
    """Create a conceptual loss landscape visualization."""
    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    # Create synthetic loss landscape
    x = np.linspace(-2, 2, 50)
    y = np.linspace(-2, 2, 50)
    X, Y = np.meshgrid(x, y)
    
    # Loss function with multiple minima
    Z = np.log(1 + (X**2 + Y**2 - 1)**2 + 0.5*X**2)
    
    # Plot surface
    surf = ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.6, edgecolor='none')
    
    # Mark teacher minimum (sharp)
    ax.scatter([0.5], [0.5], [0.2], color='red', s=100, marker='o', label='Teacher (Sharp Minimum)')
    
    # Mark student minimum (flat)
    ax.scatter([0], [0], [0], color='blue', s=100, marker='^', label='Student (Flat Minimum)')
    
    # Draw trajectory
    t = np.linspace(0, 1, 20)
    traj_x = 0.5 - 0.5*t
    traj_y = 0.5 - 0.5*t
    traj_z = 0.2 - 0.15*t
    ax.plot(traj_x, traj_y, traj_z, 'w-', linewidth=3, label='Self-Distillation Path')
    
    ax.set_xlabel('Parameter 1')
    ax.set_ylabel('Parameter 2')
    ax.set_zlabel('Loss')
    ax.set_title('Loss Landscape: Self-Distillation Finds Flatter Minima', fontsize=12, fontweight='bold')
    ax.legend()
    
    plt.tight_layout()
    plt.savefig('loss_landscape.png', dpi=150, bbox_inches='tight', facecolor='white')
    print("✓ Saved: loss_landscape.png")
    plt.close()

if __name__ == "__main__":
    print("Generating Self-Distillation visualizations...")
    print()
    
    create_timeline()
    create_evolution_stages()
    create_architecture_diagram()
    create_loss_landscape()
    
    print()
    print("All figures generated successfully!")
    print("Files created:")
    print("  - timeline.png")
    print("  - evolution_stages.png")
    print("  - architecture_be_your_own_teacher.png")
    print("  - loss_landscape.png")
