#!/usr/bin/env python3
import argparse, json, yaml

def IE(T,A,C,O,V,E,M):
    return T + A + C + O + V + E - M

def main():
    ap = argparse.ArgumentParser(description="Calcolatore IE — Indice di Epifania")
    ap.add_argument("--T", type=int, default=4, help="tīmē (0–6)")
    ap.add_argument("--A", type=int, default=2, help="Ancoraggio (0–3)")
    ap.add_argument("--C", type=int, default=2, help="Coerenza epiclesi (0–3)")
    ap.add_argument("--O", type=int, default=1, help="Offerta (-1…+2)")
    ap.add_argument("--V", type=int, default=1, help="Voto/Giuramento (0–2)")
    ap.add_argument("--E", type=int, default=1, help="Emergenza dominio (0–3)")
    ap.add_argument("--M", type=int, default=1, help="Miasma (0–5)")
    ap.add_argument("--example", action="store_true", help="Mostra esempio preimpostato")
    args = ap.parse_args()

    if args.example:
        print("Esempio: rito cittadino (Atena Polias)")
        T,A,C,O,V,E,M = 4,3,3,1,1,2,1
        ie = IE(T,A,C,O,V,E,M)
        print(f"IE={ie} (T={T},A={A},C={C},O={O},V={V},E={E},M={M}) → epifania potente se IE≥10")
        return

    ie = IE(args.T,args.A,args.C,args.O,args.V,args.E,args.M)
    print(f"IE={ie}")
    if ie <= 3:
        print("→ stato di campo (presagi lenti)")
    elif ie <= 5:
        print("→ segni chiari/daimon semplice")
    elif ie <= 7:
        print("→ epifania minore (avatar breve)")
    elif ie <= 9:
        print("→ epifania piena breve (dialogo/patto)")
    else:
        print("→ teofania simbolica, a prezzo (consumo T)")

if __name__ == "__main__":
    main()
