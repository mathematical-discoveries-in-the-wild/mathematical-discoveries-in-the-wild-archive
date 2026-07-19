from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def pdf_text(path: Path) -> str:
    import fitz

    doc = fitz.open(path)
    return "\n".join(page.get_text() for page in doc)


def main() -> None:
    source = pdf_text(ROOT / "source_paper.pdf")
    support = pdf_text(ROOT / "supporting_paper_2207.03614.pdf")
    support_compact = "".join(support.split())

    required_source = [
        "We conjecture that the bound",
        "is optimal.",
        "The same estimate also follows from Theorem 1.1",
    ]
    required_support = [
        "Corollary5.Let2\u2264p\u2264\u221eandk\u2208N.",
        "min{p,log(2m",
        "assuming we are given z as a convex combination",
    ]

    missing = [item for item in required_source if item not in source]
    missing += [
        item
        for item in required_support
        if item not in support and item not in support_compact
    ]
    if missing:
        raise SystemExit("Missing expected text snippets: " + repr(missing))

    print("Verified source conjecture and supporting approximate-Caratheodory snippets.")
    print(
        "Implication: Corollary 5 of Reis--Rothvoss with p=infinity and m=n "
        "gives ac_k(B_infty^n,B_infty^n) <= C sqrt(log(2n/k)/k). "
        "The Helly paper's dual reduction transfers this to ell_1^n up to a "
        "universal factor."
    )


if __name__ == "__main__":
    main()
