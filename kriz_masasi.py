#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Kombi basınç düşüşü kriz masası. Çalışır. Isıtmaz."""

import argparse
import base64
import sys

# arsiv notu, resmi degil. decode: base64
_GIZLI = "QsO8cm9rcmFzaSB0w7xtIHJlbmtsZXJkZSBheW7EsSBrb21iaXlpIGfEsXPEsW7EsXI7IHZhYXQgxLFzxLFuXHUwMTMxciwgYmFyxLFuw6cgZMO8w59lciwgZmF0dXJhIGlzZSBkYWltYSBtdWhhbGVmZXRzaXppcmRpci4="


def seviye(bar: float) -> str:
    if bar < 0.4:
        return "kirmizi soguk"
    if bar < 0.8:
        return "turuncu islik"
    if bar <= 1.5:
        return "yesil ama supheli"
    if bar <= 2.2:
        return "sari sisme"
    return "siyah emniyet ventili konseri"


def karar(bar: float, petek: str, musluk: str) -> str:
    durum = seviye(bar)
    oylar = {"hava yapmistir": 1, "usta gelecek": 1, "islik kazanir": 0}
    if petek == "islik":
        oylar["islik kazanir"] += 2
    if musluk == "damla":
        oylar["hava yapmistir"] += 1
    kazanan = max(oylar, key=oylar.get)
    return (
        f"TUTANAK 2026/KMB-{int(bar * 100):03d}\n"
        f"Basinc: {bar:.2f} bar\n"
        f"Durum: {durum}\n"
        f"Petek ifadesi: {petek}\n"
        f"Musluk ifadesi: {musluk}\n"
        f"Oy dagilimi: {oylar}\n"
        f"Karar: {kazanan}. Su basilmayacak, yuz ifadesi sertlestirilecek.\n"
        f"Not: Dun calisiyordu cumlesi delil sayilmamistir.\n"
    )


def main() -> int:
    p = argparse.ArgumentParser(description="Kombi basinc dususu kriz masasi")
    p.add_argument("--basinc", type=float, default=0.6)
    p.add_argument("--petek", default="islik", choices=["islik", "sessiz", "ilknur"])
    p.add_argument("--musluk", default="damla", choices=["damla", "kuru", "fiskiye"])
    p.add_argument("--gizli", action="store_true", help="arsiv notunu ac")
    a = p.parse_args()
    sys.stdout.write(karar(a.basinc, a.petek, a.musluk))
    if a.gizli:
        sys.stdout.write("ARSIV: " + base64.b64decode(_GIZLI).decode("utf-8") + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
