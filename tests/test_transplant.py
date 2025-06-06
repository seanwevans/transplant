import runpy
from pathlib import Path
import textwrap
import pytest
from types import SimpleNamespace

# Load the transplant script using runpy so we can access its functions
mod_globals = runpy.run_path(Path(__file__).resolve().parents[1] / "transplant")
transplant = SimpleNamespace(**mod_globals)


def test_parse_args_valid(tmp_path):
    listing = tmp_path / "listing.txt"
    listing.write_text("dummy")
    dest = tmp_path / "dest"
    args = transplant.parse_args([str(listing), str(dest)])
    assert args.listing == listing
    assert args.destination == dest
    assert not args.dry_run
    assert not args.verbose


def test_parse_args_dry_run(tmp_path):
    listing = tmp_path / "listing.txt"
    listing.write_text("dummy")
    args = transplant.parse_args([str(listing), "--dry-run"])
    assert args.listing == listing
    assert args.destination is None
    assert args.dry_run


def test_parse_args_requires_dest(tmp_path):
    listing = tmp_path / "listing.txt"
    listing.write_text("dummy")
    with pytest.raises(SystemExit):
        transplant.parse_args([str(listing)])


def test_is_probably_file():
    assert transplant.is_probably_file("file.txt")
    assert transplant.is_probably_file("archive.tar.gz")
    assert not transplant.is_probably_file("directory")


def test_rebuild_tree(tmp_path):
    listing_content = textwrap.dedent(
        """
        .
        ├── dir1
        │   └── file1.txt
        └── file_root.txt

        2 directories, 2 files
        """
    )
    listing_file = tmp_path / "listing.txt"
    listing_file.write_text(listing_content, encoding="utf-8")
    dest = tmp_path / "dest"
    transplant.rebuild_tree(listing_file, dest)

    assert (dest / "dir1").is_dir()
    assert (dest / "dir1" / "file1.txt").is_file()
    assert (dest / "file_root.txt").is_file()


def test_rebuild_tree_dry_run(tmp_path):
    listing_content = textwrap.dedent(
        """
        .
        └── file.txt

        1 directory, 1 file
        """
    )
    listing_file = tmp_path / "listing.txt"
    listing_file.write_text(listing_content, encoding="utf-8")
    dest = tmp_path / "dest"
    transplant.rebuild_tree(listing_file, dest, dry_run=True)
    assert not dest.exists()
