from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


required = [
    "README.md",
    "main.tex",
    "solution_packet.pdf",
    "source_paper.pdf",
    "supporting_somaglia_1803.11107.pdf",
    "figures/open_problem_crop.png",
]

missing = [name for name in required if not (ROOT / name).exists()]
if missing:
    raise SystemExit(f"missing required packet files: {missing}")

tex = (ROOT / "main.tex").read_text()
phrases = [
    "Problem 5.9",
    "height \\(\\omega_2\\)",
    "clopen replacement",
    "Cantor--Bendixson",
    "minimal Cantor--Bendixson rank",
    "Russo--Somaglia",
    "Human review",
]

missing_phrases = [phrase for phrase in phrases if phrase not in tex]
if missing_phrases:
    raise SystemExit(f"main.tex missing expected phrases: {missing_phrases}")

print("full packet asset checks passed")
