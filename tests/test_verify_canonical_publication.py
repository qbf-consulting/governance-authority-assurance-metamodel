import importlib.util
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "verify_canonical_publication.py"


def load_helpers():
    source = SCRIPT.read_text()
    prefix = source.split("parser = argparse.ArgumentParser", 1)[0]
    namespace = {}
    exec(compile(prefix, str(SCRIPT), "exec"), namespace)
    return namespace["publication_url_allowed"]


def test_approved_github_pages_url():
    allowed = load_helpers()
    url = "https://qbf-consulting.github.io/governance-authority-assurance-metamodel/v0.9.0/schemas/evidence.schema.json"
    assert allowed(url, url)


def test_approved_custom_domain_redirect():
    allowed = load_helpers()
    requested = "https://qbf-consulting.github.io/governance-authority-assurance-metamodel/v0.9.0/schemas/evidence.schema.json"
    resolved = "https://qbfconsulting.digital/governance-authority-assurance-metamodel/v0.9.0/schemas/evidence.schema.json"
    assert allowed(requested, resolved)


def test_http_downgrade_is_rejected():
    allowed = load_helpers()
    requested = "https://qbf-consulting.github.io/governance-authority-assurance-metamodel/v0.9.0/schemas/evidence.schema.json"
    resolved = "http://qbfconsulting.digital/governance-authority-assurance-metamodel/v0.9.0/schemas/evidence.schema.json"
    assert not allowed(requested, resolved)


def test_unapproved_host_is_rejected():
    allowed = load_helpers()
    requested = "https://qbf-consulting.github.io/governance-authority-assurance-metamodel/v0.9.0/schemas/evidence.schema.json"
    resolved = "https://example.invalid/governance-authority-assurance-metamodel/v0.9.0/schemas/evidence.schema.json"
    assert not allowed(requested, resolved)


def test_wrong_path_is_rejected():
    allowed = load_helpers()
    requested = "https://qbf-consulting.github.io/governance-authority-assurance-metamodel/v0.9.0/schemas/evidence.schema.json"
    resolved = "https://qbfconsulting.digital/governance-authority-assurance-metamodel/v0.9.0/schemas/remedy.schema.json"
    assert not allowed(requested, resolved)
