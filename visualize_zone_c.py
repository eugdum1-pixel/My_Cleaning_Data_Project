import matplotlib.pyplot as plt

# Data for Zone C: Future of Work
tasks = ['Data Interpretation', 'Ethical Oversight', 'Strategic Planning', 'Technical Execution']
human_lead = [70, 90, 80, 30] # Human involvement %
ai_support = [30, 10, 20, 70] # AI support %

plt.figure(figsize=(10, 6))
plt.bar(tasks, human_lead, label='Human Intelligence', color='#34495e')
plt.bar(tasks, ai_support, bottom=human_lead, label='AI Support (141 Units)', color='#1abc9c')

plt.title('Zone C: Human-AI Collaboration Taxonomy', fontsize=14, pad=20)
plt.ylabel('Contribution Percentage (%)')
plt.legend(loc='upper right')

# The Mandatory Pedigree Footer
footer = "Data Pedigree: Derived from the 141 Refined Intelligence Units.\nVisualizing the shift toward Augmented Intelligence in the UK job market."
plt.figtext(0.5, -0.05, footer, wrap=True, horizontalalignment='center', fontsize=9, style='italic', color='gray')

plt.savefig('zone_c_future_work.png', bbox_inches='tight', dpi=300)
plt.show()