import matplotlib.pyplot as plt

def draw_er_diagram(entities, relationships):
    fig, ax = plt.subplots()

    for entity, pos in entities.items():
        ax.annotate(entity, pos, fontsize=12, ha='center', va='center', bbox=dict(boxstyle='round,pad=0.2', edgecolor='k'))

    for relationship, positions in relationships:
        for start, end in positions:
            ax.annotate(relationship, (sum(start) / len(start), sum(end) / len(end)), fontsize=12, ha='center', va='center')
            ax.plot(start, end, 'k-', linewidth=2)

    ax.axis('off')
    plt.show()

# Beispielentitäten und Beziehungen
entities = {
    "Student": (1, 1),
    "Kurs": (4, 1),
    "Professor": (1, 4)
}

relationships = [
    ("besucht", [((1, 1), (4, 1)), ((1, 1), (1, 4))]),
    ("unterrichtet", [((1, 4), (4, 1))])
]

# Aufruf der Funktion, um das ER-Diagramm zu zeichnen
draw_er_diagram(entities, relationships)
