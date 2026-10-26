import ssl
import zipfile

import certifi
from fastapi.testclient import TestClient
from filelock import FileLock, Timeout
import pytest
from setuptools import build_meta

from app.main import app


def test_ca_bundle_loads_for_https_clients():
    context = ssl.create_default_context(cafile=certifi.where())
    assert context.cert_store_stats()["x509_ca"] > 0


def test_filelock_excludes_a_second_owner(tmp_path):
    path = tmp_path / "dependency.lock"
    with FileLock(path):
        with pytest.raises(Timeout):
            FileLock(path).acquire(timeout=0)
    with FileLock(path, timeout=0):
        pass


def test_setuptools_builds_a_wheel(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    (tmp_path / "setup.py").write_text(
        "from setuptools import setup\n"
        "setup(name='dependency-check', version='0.0.0', py_modules=['sample'])\n"
    )
    (tmp_path / "sample.py").write_text("VALUE = 1\n")
    output = tmp_path / "dist"
    wheel = build_meta.build_wheel(str(output))
    with zipfile.ZipFile(output / wheel) as archive:
        assert "sample.py" in archive.namelist()


def test_application_openapi_loads():
    with TestClient(app) as client:
        response = client.get("/openapi.json")
    assert response.status_code == 200
    assert response.json()["openapi"].startswith("3.")
