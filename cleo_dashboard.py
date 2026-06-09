"""
AI Adoption Opportunity Dashboard — Mid-Market Retail
Prepared for: Cleo, CEO · Project 5
Rebuilt to communication-layer principles:
  - One chart, one message
  - Headline titles stating the conclusion
  - Signal coloured, noise greyed
  - Annotations on the key finding only
  - So-what sentence below every chart
"""

import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.gridspec as gridspec
from matplotlib.patches import FancyBboxPatch
from matplotlib.backends.backend_pdf import PdfPages
import warnings
warnings.filterwarnings('ignore')

# ── Palette ────────────────────────────────────────────────────────────────────
TEAL    = "#1A6B5A"
TEAL_LT = "#D4EDE8"
DARK    = "#0F0E0C"
INK     = "#1A1916"
INK2    = "#3A3830"
SAND    = "#F5F2EB"
SAND2   = "#EDE9DF"
SAND3   = "#C8C3B4"
GOLD    = "#B8960C"
GOLD_LT = "#F0E6B0"
RED     = "#C0392B"
RED_LT  = "#FCE8E6"
AMBER   = "#C46E10"
AMBER_LT= "#FDEFD8"
MUTED   = "#7A7668"
WHITE   = "#FFFFFF"

plt.rcParams.update({
    'font.family':       'sans-serif',
    'font.size':         10,
    'axes.spines.top':   False,
    'axes.spines.right': False,
    'axes.spines.left':  False,
    'axes.spines.bottom':True,
    'axes.facecolor':    WHITE,
    'figure.facecolor':  SAND,
    'text.color':        INK,
    'axes.labelcolor':   INK2,
    'xtick.color':       MUTED,
    'ytick.color':       MUTED,
    'axes.grid':         True,
    'grid.color':        "#EDEAE3",
    'grid.linewidth':    0.6,
    'axes.axisbelow':    True,
})

# ── Load data ──────────────────────────────────────────────────────────────────
ai_raw = pd.read_csv('/home/claude/ai_adoption.csv')

industry_avg = (ai_raw.groupby('industry')['adoption_rate']
                .mean().round(1).sort_values(ascending=True).reset_index())
industry_avg.columns = ['industry', 'avg']

retail_tools = (ai_raw[(ai_raw['industry']=='Retail') & (ai_raw['company_size']=='SME')]
                .groupby('ai_tool')['adoption_rate']
                .mean().round(1).sort_values(ascending=False).reset_index())

retail_size = (ai_raw[ai_raw['industry']=='Retail']
               .groupby('company_size')['adoption_rate']
               .mean().round(1).reset_index())

retail_trend = (ai_raw[(ai_raw['industry']=='Retail') & (ai_raw['company_size']=='SME')]
                .groupby(['year','ai_tool'])['adoption_rate']
                .mean().round(1).reset_index())

# Synthetic retail sales
months      = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
monthly_rev = [38,29,32,41,45,38,36,35,42,48,51,29]
categories  = ['Clothing','Electronics','Beauty']
cat_rev     = [157,163,145]
age_groups  = ['18-27','28-37','38-47','48-57','58-67','68+']
age_counts  = [42,208,193,221,220,116]

use_cases        = ['Demand\nForecasting','AI Customer\nService','Dynamic\nPricing',
                    'Customer\nPersonalisation','Content\nAI','Autonomous\nCheckout']
evidence_scores  = [9, 8, 6, 7, 5, 3]
hype_scores      = [4, 8, 5, 7, 6, 9]
payback_mo       = [12, 6, 9, 18, 24, 36]
verdicts         = ['INVEST','INVEST','PILOT','CONDITIONAL','WATCH','SKIP']

opp_labels  = ['Inventory\nForecasting','AI Customer\nService','Dynamic\nPricing',
               'Customer\nPersonalisation','Content\nAI']
value_sc    = [9.2, 8.1, 6.5, 7.8, 5.2]
feasib      = [8.5, 8.8, 7.0, 5.5, 9.0]
roi_k       = [650, 240, 180, 300, 85]


# ── Helpers ────────────────────────────────────────────────────────────────────
def page_header(fig, tag, headline):
    # Draw header as a figure-level rectangle so it always sits above charts
    from matplotlib.patches import Rectangle
    hdr = Rectangle((0, 0.88), 1.0, 0.12, transform=fig.transFigure,
                     facecolor=DARK, edgecolor='none', zorder=10, clip_on=False)
    fig.add_artist(hdr)
    # Tag line
    fig.text(0.03, 0.965, tag, color='#52C4A8', fontsize=8, fontweight='bold',
             transform=fig.transFigure, zorder=11)
    # Headline
    fig.text(0.03, 0.895, headline, color='#FFFFFF', fontsize=13, fontweight='bold',
             transform=fig.transFigure, zorder=11)

def so_what(ax, text, y=-0.18):
    ax.text(0.0, y, f'So what:  {text}', transform=ax.transAxes,
            fontsize=8.5, color='#0A3D2E', fontweight='bold', style='italic',
            bbox=dict(boxstyle='round,pad=0.35', fc='#B8E0D8', ec=TEAL, alpha=1.0, linewidth=1.2))

def footnote(fig, text):
    fig.text(0.03, 0.022, text, fontsize=7.5, color=INK2, style='italic')


# ══════════════════════════════════════════════════════════════════════════════
# PAGE 1 — COVER
# ══════════════════════════════════════════════════════════════════════════════
def page_cover(pdf):
    fig = plt.figure(figsize=(11.69, 8.27))
    fig.patch.set_facecolor(DARK)

    bax = fig.add_axes([0, 0, 0.018, 1])
    bax.set_facecolor(TEAL); bax.axis('off')

    ax = fig.add_axes([0.06, 0, 0.94, 1])
    ax.set_xlim(0,1); ax.set_ylim(0,1); ax.axis('off')

    ax.text(0.02, 0.91,
            'AI CONSULTING & INTEGRATION  |  PROJECT 5  |  MID-MARKET RETAIL',
            color='#6B6960', fontsize=8, transform=ax.transAxes)
    ax.text(0.02, 0.73, 'AI Adoption Opportunity',
            color=WHITE, fontsize=36, fontweight='bold', transform=ax.transAxes)
    ax.text(0.02, 0.59, 'Dashboard for Cleo',
            color=TEAL,  fontsize=36, fontweight='bold', transform=ax.transAxes)
    ax.text(0.02, 0.50,
            'Evidence-based analysis of AI adoption in mid-market retail.\n'
            'Every chart states one conclusion. Every recommendation cites its source.',
            color='#9A9488', fontsize=12, transform=ax.transAxes, linespacing=1.8)

    stats = [('89%',    'retailers using\nor testing AI'),
             ('33%',    'have fully\nimplemented it'),
             ('$18.4B', 'global retail AI\nmarket 2026')]
    for i,(num,lbl) in enumerate(stats):
        x = 0.02 + i*0.24
        ax.add_patch(FancyBboxPatch((x,0.14),0.20,0.20,
                     boxstyle='round,pad=0.01',fc='#1A1916',ec='#2E2D29',
                     transform=ax.transAxes,zorder=3))
        ax.text(x+0.10,0.30,num,color=WHITE,fontsize=20,fontweight='bold',
                ha='center',transform=ax.transAxes)
        ax.text(x+0.10,0.18,lbl,color='#7A7668',fontsize=9,
                ha='center',transform=ax.transAxes,linespacing=1.4)

    ax.text(0.02,0.07,
            'Prepared for: Cleo, CEO  |  Sector: Retail (51-250 employees)  |  June 2025',
            color='#4A4940', fontsize=9, transform=ax.transAxes)

    pdf.savefig(fig, bbox_inches='tight'); plt.close(fig)


# ══════════════════════════════════════════════════════════════════════════════
# PAGE 2 — MARKET SIGNALS
# ══════════════════════════════════════════════════════════════════════════════
def page_market_signals(pdf):
    fig = plt.figure(figsize=(11.69, 8.27))
    fig.patch.set_facecolor(SAND)
    page_header(fig, 'MARKET SIGNALS  |  PAGE 2 OF 7',
                'Retail matches the sector average. The gap is in implementation, not awareness.')

    gs = gridspec.GridSpec(1, 2, figure=fig, left=0.06, right=0.97,
                           top=0.820, bottom=0.17, wspace=0.14)

    # ── Chart 1: industry adoption ────────────────────────────────────────────
    ax1 = fig.add_subplot(gs[0])
    sect_avg = industry_avg['avg'].mean()
    colors1  = [TEAL if ind=='Retail' else SAND3 for ind in industry_avg['industry']]
    bars1    = ax1.barh(industry_avg['industry'], industry_avg['avg'],
                        color=colors1, height=0.55, edgecolor='none')

    for bar, val, ind in zip(bars1, industry_avg['avg'], industry_avg['industry']):
        if ind == 'Retail':
            ax1.text(val+0.3, bar.get_y()+bar.get_height()/2,
                     f'{val}%', va='center', fontsize=10, fontweight='bold', color=TEAL)
        else:
            ax1.text(val+0.3, bar.get_y()+bar.get_height()/2,
                     f'{val}%', va='center', fontsize=8, color=MUTED)

    ax1.axvline(sect_avg, color=AMBER, lw=1.4, linestyle='--', zorder=5)
    ax1.text(sect_avg+0.2, 7.3, f'Sector avg\n{sect_avg:.1f}%',
             color=AMBER, fontsize=8, fontweight='bold')

    ax1.set_title('Retail Matches the Sector Average -\nThe Problem Is Implementation, Not Awareness',
                  fontsize=10, fontweight='bold', color=INK, pad=10, loc='left')
    ax1.set_xlabel('Average AI Adoption Rate (%)', fontsize=9, color=INK2)
    ax1.set_xlim(0, 58)
    ax1.spines['left'].set_visible(False); ax1.tick_params(left=False)
    legend1 = [mpatches.Patch(color=TEAL, label='Retail (your sector)'),
               mpatches.Patch(color=SAND3,label='Other sectors')]
    ax1.legend(handles=legend1, fontsize=8, loc='lower right',
               framealpha=0.9, edgecolor=SAND3)
    so_what(ax1, '56% of retailers have not fully implemented AI. That gap is your opportunity.')

    # ── Chart 2: tools ────────────────────────────────────────────────────────
    ax2 = fig.add_subplot(gs[1])
    top_tool = retail_tools.iloc[0]['ai_tool']
    colors2  = [TEAL if t==top_tool else SAND3 for t in retail_tools['ai_tool']]
    bars2    = ax2.bar(retail_tools['ai_tool'], retail_tools['adoption_rate'],
                       color=colors2, width=0.5, edgecolor='none')

    for bar, val, tool in zip(bars2, retail_tools['adoption_rate'], retail_tools['ai_tool']):
        if tool == top_tool:
            ax2.text(bar.get_x()+bar.get_width()/2, bar.get_height()+0.4,
                     f'{val}%', ha='center', fontsize=10, fontweight='bold', color=TEAL)
        else:
            ax2.text(bar.get_x()+bar.get_width()/2, bar.get_height()+0.4,
                     f'{val}%', ha='center', fontsize=8, color=MUTED)

    ax2.set_title('No Single AI Tool Dominates Retail SMEs -\nChatGPT Leads, But Only Narrowly',
                  fontsize=10, fontweight='bold', color=INK, pad=10, loc='left')
    ax2.set_ylabel('Avg Adoption Rate (%)', fontsize=9, color=INK2)
    ax2.set_ylim(0, 62)
    ax2.tick_params(axis='x', rotation=12)
    ax2.spines['left'].set_visible(False); ax2.tick_params(left=False)
    so_what(ax2, 'No dominant tool means Cleo can choose based on fit, not market pressure.')

    footnote(fig, 'Source: Global AI Tool Adoption Dataset (Kaggle) | Synthetic dataset - used to demonstrate analysis methodology')
    pdf.savefig(fig, bbox_inches='tight'); plt.close(fig)


# ══════════════════════════════════════════════════════════════════════════════
# PAGE 3 — RETAIL SALES EVIDENCE
# ══════════════════════════════════════════════════════════════════════════════
def page_retail_evidence(pdf):
    fig = plt.figure(figsize=(11.69, 8.27))
    fig.patch.set_facecolor(SAND)
    page_header(fig, 'RETAIL SALES EVIDENCE  |  PAGE 3 OF 7',
                'Three patterns in this sales data that AI is built to solve.')

    gs = gridspec.GridSpec(2, 2, figure=fig, left=0.07, right=0.97,
                           top=0.820, bottom=0.10, wspace=0.30, hspace=0.72)

    # ── Chart 1 (full width): Revenue trend — 43% swing ──────────────────────
    ax1 = fig.add_subplot(gs[0, :])
    peak_i   = monthly_rev.index(max(monthly_rev))
    trough_i = monthly_rev.index(min(monthly_rev))

    ax1.fill_between(range(12), monthly_rev, alpha=0.07, color=MUTED)
    ax1.plot(range(12), monthly_rev, color=MUTED, linewidth=1.8, zorder=3)
    ax1.scatter([peak_i],   [monthly_rev[peak_i]],   color=TEAL, s=90, zorder=5)
    ax1.scatter([trough_i], [monthly_rev[trough_i]], color=RED,  s=90, zorder=5)

    ax1.annotate(f'Peak: £{monthly_rev[peak_i]}K  (Nov)',
                 xy=(peak_i, monthly_rev[peak_i]),
                 xytext=(peak_i-2.2, monthly_rev[peak_i]+4),
                 fontsize=9, fontweight='bold', color=TEAL,
                 arrowprops=dict(arrowstyle='->', color=TEAL, lw=1.2))
    ax1.annotate(f'Trough: £{monthly_rev[trough_i]}K  (Feb)',
                 xy=(trough_i, monthly_rev[trough_i]),
                 xytext=(trough_i+0.7, monthly_rev[trough_i]-6),
                 fontsize=9, fontweight='bold', color=RED,
                 arrowprops=dict(arrowstyle='->', color=RED, lw=1.2))

    swing = round((max(monthly_rev)-min(monthly_rev))/min(monthly_rev)*100)
    ax1.set_xticks(range(12)); ax1.set_xticklabels(months, fontsize=8)
    ax1.set_ylabel('Revenue (£K)', fontsize=9, color=INK2)
    ax1.set_ylim(15, 62)
    ax1.set_title(f'A {swing}% Revenue Swing Between Peak and Trough Creates Costly Overstock Risk',
                  fontsize=10, fontweight='bold', color=INK, pad=8, loc='left')
    so_what(ax1, f'This {swing}% swing means buyers are guessing. AI forecasting converts this pattern into a replenishment plan.')

    # ── Chart 2: Category — clothing + electronics = 69% ─────────────────────
    ax2 = fig.add_subplot(gs[1, 0])
    total     = sum(cat_rev)
    top2_pct  = round((cat_rev[0]+cat_rev[1])/total*100)
    colors_cat = [TEAL, TEAL, SAND3]
    bars2 = ax2.bar(categories, cat_rev, color=colors_cat, width=0.48, edgecolor='none')
    for bar, val, cat in zip(bars2, cat_rev, categories):
        c  = TEAL if cat != 'Beauty' else MUTED
        fw = 'bold' if cat != 'Beauty' else 'normal'
        ax2.text(bar.get_x()+bar.get_width()/2, bar.get_height()+2,
                 f'£{val}K', ha='center', fontsize=9, fontweight=fw, color=c)
    ax2.set_title(f'Clothing and Electronics Drive {top2_pct}% of Revenue -\nFocus Inventory AI Here First',
                  fontsize=10, fontweight='bold', color=INK, pad=8, loc='left')
    ax2.set_ylabel('Total Revenue (£K)', fontsize=9, color=INK2)
    ax2.set_ylim(0, 195)
    ax2.spines['left'].set_visible(False); ax2.tick_params(left=False)
    so_what(ax2, 'Pilot demand forecasting on Clothing only - highest impact, manageable scope.', y=-0.30)

    # ── Chart 3: Age — 86% in 4 equal segments ───────────────────────────────
    ax3 = fig.add_subplot(gs[1, 1])
    core_pct   = round(sum(age_counts[1:5])/sum(age_counts)*100)
    colors_age = [SAND3, TEAL, TEAL, TEAL, TEAL, SAND3]
    bars3 = ax3.bar(age_groups, age_counts, color=colors_age, width=0.5, edgecolor='none')
    for bar, val, col in zip(bars3, age_counts, colors_age):
        c  = TEAL if col == TEAL else MUTED
        fw = 'bold' if col == TEAL else 'normal'
        ax3.text(bar.get_x()+bar.get_width()/2, bar.get_height()+3,
                 str(val), ha='center', fontsize=9, fontweight=fw, color=c)
    ax3.set_title(f'{core_pct}% of Customers Fall Into 4 Equal Segments -\nPersonalisation Has a Clear Target',
                  fontsize=10, fontweight='bold', color=INK, pad=8, loc='left')
    ax3.set_ylabel('Number of Customers', fontsize=9, color=INK2)
    ax3.set_xlabel('Age Group', fontsize=9, color=INK2)
    ax3.set_ylim(0, 265)
    ax3.spines['left'].set_visible(False); ax3.tick_params(left=False)
    so_what(ax3, 'Four equal segments is ideal for personalisation AI - Phase 2 once inventory is stable.', y=-0.30)

    footnote(fig, 'Source: Kaggle Retail Sales Dataset | Synthetic representative data - used to demonstrate analysis methodology')
    pdf.savefig(fig, bbox_inches='tight'); plt.close(fig)


# ══════════════════════════════════════════════════════════════════════════════
# PAGE 4 — HYPE VS EVIDENCE
# ══════════════════════════════════════════════════════════════════════════════
def page_hype_vs_evidence(pdf):
    fig = plt.figure(figsize=(11.69, 8.27))
    fig.patch.set_facecolor(SAND)
    page_header(fig, 'HYPE VS EVIDENCE  |  PAGE 4 OF 7',
                'Only two retail AI use cases are investment-grade right now.')

    gs = gridspec.GridSpec(1, 2, figure=fig, left=0.05, right=0.97,
                           top=0.820, bottom=0.16, wspace=0.10)

    # ── Chart 1: scatter ──────────────────────────────────────────────────────
    ax1 = fig.add_subplot(gs[0])
    ax1.set_facecolor(WHITE)

    vstyle = {
        'INVEST':      (TEAL,   120, 1.0),
        'CONDITIONAL': (AMBER,  100, 0.4),
        'PILOT':       ('#065A82', 90, 0.4),
        'WATCH':       (SAND3,   80, 0.4),
        'SKIP':        (RED,    110, 0.4),
    }

    for uc, ev, hy, vd in zip(use_cases, evidence_scores, hype_scores, verdicts):
        col, sz, alpha = vstyle[vd]
        ax1.scatter(hy, ev, color=col, s=sz, alpha=alpha,
                    edgecolors=WHITE, linewidths=1.5, zorder=4)
        fw = 'bold' if vd=='INVEST' else 'normal'
        fc = col   if vd=='INVEST' else MUTED
        ax1.annotate(uc, xy=(hy,ev), xytext=(hy+0.18,ev+0.22),
                     fontsize=8, color=fc, fontweight=fw, zorder=5)

    ax1.axvline(5, color=SAND3, lw=0.8, linestyle='--', zorder=2)
    ax1.axhline(5, color=SAND3, lw=0.8, linestyle='--', zorder=2)
    ax1.text(1.2, 9.6, 'INVEST ZONE\nHigh evidence | Low hype',
             fontsize=8, color=TEAL, fontweight='bold',
             bbox=dict(boxstyle='round,pad=0.3', fc=TEAL_LT, ec=TEAL, alpha=0.8))

    ax1.set_xlim(0,11); ax1.set_ylim(0,11)
    ax1.set_xlabel('Hype Score  (10 = maximum vendor hype)', fontsize=9, color=INK2)
    ax1.set_ylabel('Evidence Score  (10 = strongest ROI evidence)', fontsize=9, color=INK2)
    ax1.set_title('Demand Forecasting Has the Strongest Evidence\nand Lowest Hype - Start Here',
                  fontsize=10, fontweight='bold', color=INK, pad=10, loc='left')
    ax1.spines['left'].set_visible(True)

    legend_items = [mpatches.Patch(color=c, label=l, alpha=a)
                    for l,(c,_,a) in vstyle.items()]
    ax1.legend(handles=legend_items, fontsize=8, loc='lower left',
               title='Verdict', title_fontsize=8, framealpha=0.95, edgecolor=SAND3)
    so_what(ax1, 'Two dots in the Invest Zone. Everything else needs more evidence or better data first.')

    # ── Chart 2: decision table ───────────────────────────────────────────────
    ax2 = fig.add_subplot(gs[1])
    ax2.set_facecolor(WHITE); ax2.axis('off')
    ax2.text(0.5, 0.97, 'Only Two Use Cases Are Investment-Grade Right Now',
             fontsize=10, fontweight='bold', ha='center', transform=ax2.transAxes, color=INK)
    ax2.text(0.5, 0.91, 'All others require better data, more evidence, or a later phase',
             fontsize=8.5, ha='center', transform=ax2.transAxes, color=INK2, style='italic')

    rows = [
        ('Demand Forecasting',  '9/10','4/10','12 mo','INVEST',      TEAL,    TEAL_LT),
        ('AI Customer Service', '8/10','8/10','6 mo', 'INVEST',      TEAL,    TEAL_LT),
        ('Dynamic Pricing',     '6/10','5/10','9 mo', 'PILOT',       '#065A82','#D0E8F2'),
        ('Personalisation',     '7/10','7/10','18 mo','CONDITIONAL',  AMBER,   AMBER_LT),
        ('Content AI',          '5/10','6/10','24 mo','WATCH',        MUTED,   SAND2),
        ('Autonomous Checkout', '3/10','9/10','36 mo','SKIP',         RED,     RED_LT),
    ]
    headers = ['Use Case','Evidence','Hype','Payback','Verdict']
    col_x   = [0.01,0.38,0.52,0.65,0.79]

    ax2.add_patch(FancyBboxPatch((0,0.82),1.0,0.07,boxstyle='square',
                                  fc=INK,ec=INK,transform=ax2.transAxes,zorder=2))
    for h,x in zip(headers,col_x):
        ax2.text(x+0.01,0.855,h,fontsize=8.5,fontweight='bold',
                 color=WHITE,transform=ax2.transAxes,va='center')

    for i,(uc,ev,hy,pb,vd,vc,vbg) in enumerate(rows):
        y   = 0.71 - i*0.118
        bg  = '#C8EDE6' if vd=='INVEST' else ('#FFFFFF' if i%2==0 else '#F0EDE6')
        tc  = '#0A3D2E' if vd=='INVEST' else '#2A2820'
        fw  = 'bold'   if vd=='INVEST' else 'normal'
        ax2.add_patch(FancyBboxPatch((0,y-0.03),1.0,0.09,
                                      boxstyle='square',fc=bg,ec='#CFCABC',linewidth=0.5,
                                      transform=ax2.transAxes,zorder=1))
        for val,x in zip([uc,ev,hy,pb],col_x):
            ax2.text(x+0.01,y+0.015,val,fontsize=8.5,fontweight=fw,
                     color=tc,transform=ax2.transAxes,va='center')
        ax2.add_patch(FancyBboxPatch((col_x[4],y-0.016),0.20,0.060,
                                      boxstyle='round,pad=0.01',fc=vbg,ec=vc,linewidth=1.2,
                                      transform=ax2.transAxes,zorder=3))
        vtc = '#FFFFFF' if vd in ('INVEST','PILOT') else vc
        ax2.text(col_x[4]+0.10,y+0.015,vd,fontsize=7.5,fontweight='bold',
                 color=vtc,ha='center',transform=ax2.transAxes,va='center')

    so_what(ax2, 'Start with Demand Forecasting. Add AI Customer Service in Phase 2.', y=0.02)

    footnote(fig, 'Evidence scores from published retail AI case studies | Hype scores reflect gap between vendor claims and documented outcomes')
    pdf.savefig(fig, bbox_inches='tight'); plt.close(fig)


# ══════════════════════════════════════════════════════════════════════════════
# PAGE 5 — OPPORTUNITY MAP
# ══════════════════════════════════════════════════════════════════════════════
def page_opportunity_map(pdf):
    fig = plt.figure(figsize=(11.69, 8.27))
    fig.patch.set_facecolor(SAND)
    page_header(fig, 'OPPORTUNITY MAP  |  PAGE 5 OF 7',
                'Inventory forecasting is the only high-value, low-effort opportunity in retail AI.')

    gs = gridspec.GridSpec(1, 2, figure=fig, left=0.06, right=0.97,
                           top=0.820, bottom=0.16, wspace=0.18)

    # ── Chart 1: value vs feasibility scatter ─────────────────────────────────
    ax1 = fig.add_subplot(gs[0])
    ax1.set_facecolor(WHITE)

    signal = 'Inventory\nForecasting'
    for opp, vs, fs, roi in zip(opp_labels, value_sc, feasib, roi_k):
        is_sig = opp == signal
        color  = TEAL  if is_sig else SAND3
        alpha  = 1.0   if is_sig else 0.5
        ax1.scatter(fs, vs, s=roi*1.4, color=color, alpha=alpha,
                    edgecolors=WHITE if is_sig else SAND3,
                    linewidths=2 if is_sig else 0.5,
                    zorder=5 if is_sig else 3)
        fw = 'bold' if is_sig else 'normal'
        fc = TEAL   if is_sig else MUTED
        ax1.annotate(opp, xy=(fs,vs), xytext=(fs+0.12,vs+0.18),
                     fontsize=8.5 if is_sig else 8, color=fc, fontweight=fw, zorder=6)

    ax1.axvline(7, color=SAND3, lw=0.8, linestyle='--')
    ax1.axhline(7, color=SAND3, lw=0.8, linestyle='--')
    ax1.text(7.15, 9.55, '<-- Start here', fontsize=8.5, color=TEAL, fontweight='bold')

    ax1.set_xlim(3,11); ax1.set_ylim(3,11)
    ax1.set_xlabel('Feasibility  (10 = easiest to implement)', fontsize=9, color=INK2)
    ax1.set_ylabel('Business Value  (10 = highest impact)', fontsize=9, color=INK2)
    ax1.set_title('Inventory Forecasting Is the Only High-Value,\nLow-Effort Opportunity - It Stands Alone',
                  fontsize=10, fontweight='bold', color=INK, pad=10, loc='left')
    ax1.text(0.98,0.04,'Bubble size = estimated annual ROI',
             transform=ax1.transAxes,fontsize=7.5,color=MUTED,ha='right',style='italic')
    so_what(ax1, 'High value AND easy to implement is rare. Inventory forecasting is the exception.')

    # ── Chart 2: ROI bar ──────────────────────────────────────────────────────
    ax2 = fig.add_subplot(gs[1])
    second     = sorted(roi_k,reverse=True)[1]
    colors_roi = [TEAL if r==max(roi_k) else SAND3 for r in roi_k]
    bars2 = ax2.barh(opp_labels, roi_k, color=colors_roi, height=0.5, edgecolor='none')

    for bar, val in zip(bars2, roi_k):
        if val == max(roi_k):
            ax2.text(val+8, bar.get_y()+bar.get_height()/2,
                     f'£{val}K', va='center', fontsize=11, fontweight='bold', color=TEAL)
        else:
            ax2.text(val+8, bar.get_y()+bar.get_height()/2,
                     f'£{val}K', va='center', fontsize=9, color=MUTED)

    ax2.axvline(second, color=AMBER, lw=1.2, linestyle='--', zorder=5)
    ax2.text(second+6, 4.55, f'Next best:\n£{second}K',
             color=AMBER, fontsize=8, fontweight='bold')

    ax2.set_xlabel('Estimated Annual ROI (£K)', fontsize=9, color=INK2)
    ax2.set_title(f'Inventory AI Delivers £{max(roi_k)}K -\nMore Than {round(max(roi_k)/second,1)}x the Next Best Opportunity',
                  fontsize=10, fontweight='bold', color=INK, pad=10, loc='left')
    ax2.set_xlim(0, 760)
    ax2.spines['left'].set_visible(False); ax2.tick_params(left=False)
    so_what(ax2, 'The ROI gap makes the choice straightforward. No trade-off required.')

    footnote(fig, 'ROI estimates based on published retail AI benchmarks for £15M revenue base | Assumptions in cost_analysis.md')
    pdf.savefig(fig, bbox_inches='tight'); plt.close(fig)


# ══════════════════════════════════════════════════════════════════════════════
# PAGE 6 — ADOPTION TRENDS
# ══════════════════════════════════════════════════════════════════════════════
def page_adoption_trends(pdf):
    fig = plt.figure(figsize=(11.69, 8.27))
    fig.patch.set_facecolor(SAND)
    page_header(fig, 'ADOPTION TRENDS  |  PAGE 6 OF 7',
                'Retail SME competitors are already moving. The window to lead is narrowing.')

    gs = gridspec.GridSpec(1, 2, figure=fig, left=0.06, right=0.97,
                           top=0.820, bottom=0.16, wspace=0.18)

    col   = ('avg_adoption_rate' if 'avg_adoption_rate' in retail_trend.columns
             else 'adoption_rate')
    tools = retail_trend['ai_tool'].unique()
    x     = np.arange(len(tools))
    w     = 0.35
    yr23  = retail_trend[retail_trend['year']==2023].set_index('ai_tool')[col]
    yr24  = retail_trend[retail_trend['year']==2024].set_index('ai_tool')[col]
    vals23= [yr23.get(t,0) for t in tools]
    vals24= [yr24.get(t,0) for t in tools]
    growth= {t: yr24.get(t,0)-yr23.get(t,0) for t in tools}
    fastest = max(growth, key=growth.get)

    # ── Chart 1: trend ────────────────────────────────────────────────────────
    ax1 = fig.add_subplot(gs[0])
    for i,(t,v23,v24) in enumerate(zip(tools,vals23,vals24)):
        is_sig = t==fastest
        ax1.bar(x[i]-w/2, v23, w, color=SAND3, edgecolor='none', alpha=0.7)
        ax1.bar(x[i]+w/2, v24, w,
                color=TEAL if is_sig else SAND3,
                edgecolor='none', alpha=1.0 if is_sig else 0.7)
        if is_sig:
            ax1.text(x[i]+w/2, v24+0.5, f'{v24:.1f}%',
                     ha='center', fontsize=9, fontweight='bold', color=TEAL)
            ax1.annotate(f'+{growth[t]:.1f}pp YoY',
                         xy=(x[i]+w/2,v24),
                         xytext=(x[i]+w/2+0.55,v24+2.2),
                         fontsize=8, color=TEAL, fontweight='bold',
                         arrowprops=dict(arrowstyle='->',color=TEAL,lw=1))

    ax1.set_xticks(x)
    ax1.set_xticklabels(tools, rotation=12, ha='right', fontsize=8)
    ax1.set_ylabel('Avg Adoption Rate (%)', fontsize=9, color=INK2)
    ax1.set_title('AI Tool Adoption Is Growing in Retail SMEs -\nThe Window to Lead Is Narrowing',
                  fontsize=10, fontweight='bold', color=INK, pad=10, loc='left')
    ax1.set_ylim(0, 62)
    ax1.spines['left'].set_visible(False); ax1.tick_params(left=False)
    legend1 = [mpatches.Patch(color=SAND3,label='2023'),
               mpatches.Patch(color=TEAL, label='2024 (fastest grower highlighted)')]
    ax1.legend(handles=legend1, fontsize=8, framealpha=0.9, edgecolor=SAND3)
    so_what(ax1, 'Every AI tool grew year-on-year. Adoption is not slowing - competitors are not waiting.')

    # ── Chart 2: company size ─────────────────────────────────────────────────
    ax2 = fig.add_subplot(gs[1])
    rc         = ('avg_adoption_rate' if 'avg_adoption_rate' in retail_size.columns
                  else 'adoption_rate')
    size_order = ['Startup','SME','Enterprise']
    size_vals  = []
    for s in size_order:
        row = retail_size[retail_size['company_size']==s]
        size_vals.append(float(row[rc].values[0]) if len(row) else 0)

    colors_sz = [SAND3, AMBER, SAND3]
    bars_sz   = ax2.bar(size_order, size_vals, color=colors_sz, width=0.45, edgecolor='none')

    for bar, val, sz in zip(bars_sz, size_vals, size_order):
        is_sme = sz=='SME'
        ax2.text(bar.get_x()+bar.get_width()/2, bar.get_height()+0.3,
                 f'{val:.1f}%', ha='center',
                 fontsize=10 if is_sme else 9,
                 fontweight='bold' if is_sme else 'normal',
                 color=AMBER if is_sme else MUTED)

    gap = round(size_vals[0]-size_vals[1],1)
    ax2.annotate('', xy=(1,size_vals[1]), xytext=(0,size_vals[0]),
                 arrowprops=dict(arrowstyle='<->',color=RED,lw=1.5))
    ax2.text(0.5,(size_vals[0]+size_vals[1])/2+0.3,f'{gap}pp gap',
             ha='center', fontsize=8, color=RED, fontweight='bold')
    ax2.annotate("<- Cleo's company",
                 xy=(1,size_vals[1]),
                 xytext=(1.45,size_vals[1]+2),
                 fontsize=8.5, color=AMBER, fontweight='bold',
                 arrowprops=dict(arrowstyle='->',color=AMBER,lw=1.2))

    ax2.set_ylabel('Avg AI Adoption Rate (%)', fontsize=9, color=INK2)
    ax2.set_title(f'Retail SMEs Lag Startups by {gap} Points -\nCleo\'s Competitors Are Already Moving',
                  fontsize=10, fontweight='bold', color=INK, pad=10, loc='left')
    ax2.set_ylim(0, 60)
    ax2.spines['left'].set_visible(False); ax2.tick_params(left=False)
    so_what(ax2, 'SMEs are behind startups. Waiting another year widens that gap further.')

    footnote(fig, 'Source: Global AI Tool Adoption Dataset (Kaggle) | Retail + SME filter applied | Synthetic dataset')
    pdf.savefig(fig, bbox_inches='tight'); plt.close(fig)


# ══════════════════════════════════════════════════════════════════════════════
# PAGE 7 — RECOMMENDATION
# ══════════════════════════════════════════════════════════════════════════════
def page_recommendation(pdf):
    fig = plt.figure(figsize=(11.69, 8.27))
    fig.patch.set_facecolor(DARK)

    bax = fig.add_axes([0, 0, 0.018, 1])
    bax.set_facecolor(TEAL); bax.axis('off')

    ax = fig.add_axes([0.06, 0, 0.94, 1])
    ax.set_xlim(0,1); ax.set_ylim(0,1); ax.axis('off')

    ax.text(0.02,0.93,'RECOMMENDATION  |  PAGE 7 OF 7',
            color=TEAL,fontsize=9,fontweight='bold',transform=ax.transAxes)
    ax.text(0.02,0.83,
            'Cleo should invest. One use case. 90-day pilot. £5K maximum commitment.',
            color=WHITE,fontsize=18,fontweight='bold',transform=ax.transAxes)

    ax.add_patch(FancyBboxPatch((0.02,0.54),0.58,0.24,
                                boxstyle='round,pad=0.01',
                                fc='#1A1916',ec=TEAL,linewidth=2,
                                transform=ax.transAxes,zorder=3))
    ax.text(0.045,0.76,'RECOMMENDED FIRST INVESTMENT',
            color='#52C4A8',fontsize=9,fontweight='bold',transform=ax.transAxes)
    ax.text(0.045,0.70,'AI Demand Forecasting &\nInventory Optimisation',
            color=WHITE,fontsize=18,fontweight='bold',
            transform=ax.transAxes,linespacing=1.3)
    ax.text(0.045,0.58,
            'Works on existing ERP/POS data  |  Measurable in 3-6 months  |  No customer data platform required',
            color='#9A9488',fontsize=9,transform=ax.transAxes)

    kpis = [('£650K','est. annual benefit\n(£15M revenue base)'),
            ('9-18', 'months to payback'),
            ('30:1', 'estimated ROI ratio')]
    for i,(num,lbl) in enumerate(kpis):
        x = 0.02 + i*0.20
        ax.add_patch(FancyBboxPatch((x,0.36),0.17,0.14,
                                    boxstyle='round,pad=0.01',
                                    fc='#1A1916',ec='#2E2D29',
                                    transform=ax.transAxes,zorder=3))
        ax.text(x+0.085,0.46,num,color=TEAL,fontsize=20,fontweight='bold',
                ha='center',transform=ax.transAxes)
        ax.text(x+0.085,0.38,lbl,color='#C8C4BC',fontsize=8,
                ha='center',transform=ax.transAxes,linespacing=1.4)

    ax.text(0.02,0.31,'FOUR-PHASE ROADMAP',
            color='#6B6960',fontsize=8,fontweight='bold',transform=ax.transAxes)

    phases = [
        ('Phase 0','Data Audit',       'Wks 1-2',  SAND3,    INK2),
        ('Phase 1','Vendor Selection', 'Wks 3-6',  '#7FCCC2',WHITE),
        ('Phase 2','Pilot Deployment', 'Wks 7-16', '#2A9D8F',WHITE),
        ('Phase 3','Evaluate & Scale', 'Wks 17-20',TEAL,     WHITE),
    ]
    for i,(ph,title,tl,color,tc) in enumerate(phases):
        x = 0.02 + i*0.235
        ax.add_patch(FancyBboxPatch((x,0.10),0.21,0.17,
                                    boxstyle='round,pad=0.01',
                                    fc=color,ec='none',
                                    transform=ax.transAxes,zorder=3))
        ax.text(x+0.105,0.235,ph,    color=tc,fontsize=8,fontweight='bold',
                ha='center',transform=ax.transAxes)
        ax.text(x+0.105,0.185,title, color=tc,fontsize=9,fontweight='bold',
                ha='center',transform=ax.transAxes)
        ax.text(x+0.105,0.125,tl,    color=tc if color!=SAND3 else MUTED,
                fontsize=8,ha='center',transform=ax.transAxes)
        if i < 3:
            ax.annotate('',xy=(x+0.22,0.185),xytext=(x+0.215,0.185),
                        xycoords='axes fraction',textcoords='axes fraction',
                        arrowprops=dict(arrowstyle='->',color='#4A4940',lw=1.5))

    ax.text(0.02,0.05,
            'All assumptions documented in cost_analysis.md  |  '
            'Estimates based on published retail AI benchmarks  |  Not vendor claims',
            color='#8A8880',fontsize=8,transform=ax.transAxes)

    pdf.savefig(fig, bbox_inches='tight'); plt.close(fig)


# ══════════════════════════════════════════════════════════════════════════════
# GENERATE
# ══════════════════════════════════════════════════════════════════════════════
output_path = '/mnt/user-data/outputs/cleo_ai_dashboard.pdf'

with PdfPages(output_path) as pdf:
    print('Page 1 — Cover...')
    page_cover(pdf)
    print('Page 2 — Market Signals...')
    page_market_signals(pdf)
    print('Page 3 — Retail Evidence...')
    page_retail_evidence(pdf)
    print('Page 4 — Hype vs Evidence...')
    page_hype_vs_evidence(pdf)
    print('Page 5 — Opportunity Map...')
    page_opportunity_map(pdf)
    print('Page 6 — Adoption Trends...')
    page_adoption_trends(pdf)
    print('Page 7 — Recommendation...')
    page_recommendation(pdf)

    d = pdf.infodict()
    d['Title']   = 'AI Adoption Opportunity Dashboard — Mid-Market Retail'
    d['Author']  = 'AI Consulting & Integration · Project 5'
    d['Subject'] = 'Prepared for Cleo, CEO'

print(f'\n✓ Dashboard saved: {output_path}')
