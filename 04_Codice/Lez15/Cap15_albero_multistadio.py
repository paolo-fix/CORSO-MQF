"""Figura 15.3: albero illustrativo a quattro stadi decisionali.

T_1={0}: x; T_2={1}: u_1; T_3={2,3}: (u_2,u_3); T_4={4}: g_4.
A,B etichettano le realizzazioni di Z_1; C_1,C_2 le storie del blocco
(Z_2,Z_3) considerate al termine dello stadio 3; D_1,D_2 quelle di Z_4.
Il nodo a t=2 e' intermedio e non introduce una decisione autonoma.
"""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

# Nel repository salva in <radice>/graphics; altrove accanto allo script.
script_dir = Path(__file__).resolve().parent
candidate_root = Path(__file__).resolve().parents[2]
project_root = candidate_root if (candidate_root / "00_MasterPlan").is_dir() else script_dir
out_dir = project_root / "graphics" if project_root != script_dir else script_dir
out_dir.mkdir(parents=True, exist_ok=True)
png_path = out_dir / "Cap15_albero_multistadio.png"
svg_path = out_dir / "Cap15_albero_multistadio.svg"

FONT_FAMILY = "DejaVu Sans"
FONT_SCALE = 1.0
LINE_SPACING_SCALE = 1.0
FONT_SIZES = {
    "title": 18.0, "stage_title": 16.0, "stage_set": 14.0,
    "stage_description": 12.0, "node_label": 13.0,
    "scenario_label": 12.0, "intermediate_label": 12.0,
    "root_label": 16.0, "root_description": 12.0,
    "time_label": 13.0, "legend": 11.5,
}
LINE_SPACINGS = {key: 1.0 for key in FONT_SIZES}
LINE_SPACINGS["stage_description"] = 1.25
plt.rcParams["font.family"] = FONT_FAMILY

def fs(key):
    return FONT_SIZES[key] * FONT_SCALE

def ls(key):
    return LINE_SPACINGS[key] * LINE_SPACING_SCALE

BLU, ROSSO, GRIGIO = "#2b4c7e", "#c0502e", "#8a8a8a"
X = lambda t: 2.0 * t
X_STADIO_4 = 7.0
FINE_STADIO_4 = 9.5
ymin, ymax = -5.6, 6.6
fig, ax = plt.subplots(figsize=(12.5, 7.6))

bande = [
    (1, -1.0, 0.45, r"$\mathcal{T}_1=\{0\}$", "decide $x$", "#eef2f8"),
    (2, 0.45, 2.45, r"$\mathcal{T}_2=\{1\}$", "osserva $Z_1$\ndecide $u_1$", "#f7f3ee"),
    (3, 2.45, 6.45, r"$\mathcal{T}_3=\{2,3\}$", "osserva $(Z_2,Z_3)$\ndecide $(u_2,u_3)$", "#eef2f8"),
    (4, 6.45, FINE_STADIO_4, r"$\mathcal{T}_4=\{4\}$", "osserva $Z_4$\ndecide $g_4$", "#f7f3ee"),
]
for k, x0, x1, times, description, bg in bande:
    ax.add_patch(Rectangle((x0, ymin), x1-x0, ymax-ymin, color=bg, lw=0, zorder=0))
    xm=(x0+x1)/2
    ax.text(xm,ymax-.3,f"Stadio {k}",ha="center",va="top",fontsize=fs("stage_title"),color=BLU,weight="bold")
    ax.text(xm,ymax-.95,times,ha="center",va="top",fontsize=fs("stage_set"),color=BLU)
    ax.text(xm,ymax-1.55,description,ha="center",va="top",fontsize=fs("stage_description"),color="#555555",linespacing=ls("stage_description"))
for xb in (0.45,2.45,6.45):
    ax.plot([xb,xb],[ymin,ymax],color=BLU,lw=1,ls=":",zorder=.5)

def arco(p,q,evidenziato=False):
    ax.plot([p[0],q[0]],[p[1],q[1]],color=ROSSO if evidenziato else GRIGIO,
            lw=2.4 if evidenziato else 1.3,zorder=1)

def pieno(p):
    ax.scatter(*p,s=210,color=BLU,edgecolor="white",lw=1.5,zorder=3)

def vuoto(p):
    ax.scatter(*p,s=120,facecolor="white",edgecolor=BLU,lw=1.6,zorder=3)

root=(X(0),0)
pieno(root)
ax.text(root[0],root[1]+.48,"$x$",ha="center",fontsize=fs("root_label"),color=BLU)
ax.text(root[0],root[1]-.65,"radice",ha="center",fontsize=fs("root_description"),color="#555555")

yZ1={"A":2.0,"B":-2.0}
yC={("A",1):3.0,("A",2):1.0,("B",1):-1.0,("B",2):-3.0}
percorso_evidenziato=("A",2)
i=0
for z in ("A","B"):
    p1=(X(1),yZ1[z])
    p2=(X(2),yZ1[z])  # nodo informativo a t=2: nessuna nuova decisione
    arco(root,p1,evidenziato=(z=="A"))
    arco(p1,p2,evidenziato=(z=="A"))
    pieno(p1)
    vuoto(p2)
    ax.text(p1[0],p1[1]+(.48 if z=="A" else -.75),
            f"$Z_1={z},\\ u_1({z})$",ha="center",fontsize=fs("node_label"),color=BLU)
    for c in (1,2):
        yc=yC[(z,c)]
        p3=(X(3),yc)
        evidenziato=(z,c)==percorso_evidenziato
        arco(p2,p3,evidenziato=evidenziato)
        pieno(p3)
        # C_c indica la storia congiunta (Z_2,Z_3) nota al tempo t=3.
        ax.text(p3[0]-.05,p3[1]+.46,rf"$(Z_2,Z_3)=C_{c}$",ha="center",va="bottom",
                fontsize=fs("intermediate_label"),color="#555555")
        if evidenziato:
            ax.text(p3[0]-.38,p3[1]-.60,r"decisione $(u_2,u_3)$",ha="center",va="top",
                    fontsize=fs("scenario_label"),color=BLU)
        for d,dy in ((1,.5),(2,-.5)):
            i+=1
            p4=(X_STADIO_4,yc+dy)
            arco(p3,p4)
            pieno(p4)
            # Etichette D_1,D_2 al nodo terminale (tempo t=4).
            ax.text(p4[0]+.24,p4[1]+.22,rf"$Z_4=D_{d}$",ha="left",va="bottom",
                    fontsize=fs("intermediate_label"),color="#555555")
            ax.text(p4[0]+.30,p4[1],f"$s_{i}=({z},C_{c},D_{d})$",va="center",
                    fontsize=fs("scenario_label"),color=BLU)

for t in range(5):
    x_t=X_STADIO_4 if t==4 else X(t)
    ax.text(x_t,ymin+.3,f"$t={t}$",ha="center",color="#555555",fontsize=fs("time_label"))

ax.scatter([],[],s=150,color=BLU,label=r"nodo di stadio (decisione), a $t_{k,n_k}$")
ax.scatter([],[],s=100,facecolor="white",edgecolor=BLU,lw=1.6,
           label="nodo informativo intermedio (nessuna decisione)")
legend=ax.legend(loc="lower center",bbox_to_anchor=(.5,-.09),ncol=2,
                 frameon=False,fontsize=fs("legend"))
for t in legend.get_texts():
    t.set_linespacing(ls("legend"))
ax.set_title("Albero degli scenari a 4 stadi: tempi e decisioni",
             fontsize=fs("title"),color=BLU,pad=10)
ax.set_xlim(-1.0,FINE_STADIO_4)
ax.set_ylim(ymin,ymax)
ax.axis("off")
fig.tight_layout()
fig.savefig(png_path,dpi=300,bbox_inches="tight")
fig.savefig(svg_path,bbox_inches="tight")
plt.close(fig)
print(f"PNG: {png_path}\nSVG: {svg_path}")
