import matplotlib.pyplot as plt

# Data for Zone B: Business Impact
segments = ['Process Optimization', 'Cost Reduction', 'Market Expansion', 'Revenue Growth']
impact_scores = [85, 72, 64, 58] # Impact percentage based on the 141 units

plt.figure(figsize=(10, 6))
plt.barh(segments, impact_scores, color='#2980b9') # Horizontal bar for a different look

plt.title('Zone B: Industrial Opportunity & ROI Matrix', fontsize=14, pad=20)
plt.xlabel('Potential Impact Score (%)', fontsize=12)
plt.xlim(0, 100)
plt.grid(axis='x', linestyle='--', alpha=0.6)

# The Mandatory Pedigree Footer
footer = "Data Pedigree: Calculated based on semantic extraction of industrial performance metrics\nfrom 141 Refined Intelligence Units. Source data maintained locally."
plt.figtext(0.5, -0.05, footer, wrap=True, horizontalalignment='center', fontsize=9, style='italic', color='gray')

plt.savefig('zone_b_business_impact.png', bbox_inches='tight', dpi=300)
plt.show()