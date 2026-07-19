from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def pdf_text(path: Path) -> str:
    import fitz

    doc = fitz.open(path)
    return "\n".join(page.get_text() for page in doc)


def main() -> None:
    source = pdf_text(ROOT / "source_paper.pdf")
    support = pdf_text(ROOT / "supporting_paper_2604.01875.pdf")

    required_source = [
        "Question 6.3. Let 0 < p \u22641.",
        "for each K \u2208[1, \u221e)",
        "uniformly separated bounded metric space",
    ]
    required_support = [
        "Theorem 1.1. Let M be a uniformly discrete metric space. Then F(M) is 3-Schur.",
        "If X is c-Schur, it has also the c-strong Schur property.",
        "Lipschitz-free spaces are over the reals",
    ]

    missing = [item for item in required_source if item not in source]
    missing += [item for item in required_support if item not in support]
    if missing:
        raise SystemExit("Missing expected text snippets: " + repr(missing))

    print("Verified source question text and supporting theorem snippets.")
    print(
        "Implication: for p=1 and real Lipschitz-free spaces, uniformly separated "
        "metric spaces are uniformly discrete, so Theorem 1.1 gives 3-Schur; "
        "Proposition 2.2 then gives 3-strong Schur. Thus the uniformly separated "
        "bounded p=1 route cannot produce spaces failing K-strong Schur for every K."
    )


if __name__ == "__main__":
    main()
