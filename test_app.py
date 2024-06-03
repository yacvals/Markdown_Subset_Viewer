import pytest
from app import parse_markdown

def test_bold():
    md_text = "This is **bold** text."
    expected_html = "<p>This is <b>bold</b> text.</p>"
    assert parse_markdown(md_text) == expected_html

def test_italic():
    md_text = "This is _italic_ text."
    expected_html = "<p>This is <i>italic</i> text.</p>"
    assert parse_markdown(md_text) == expected_html


if __name__ == "__main__":
    pytest.main()
