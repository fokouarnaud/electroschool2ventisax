from courses.rendering import render_markdown


def test_markdown_emphasis_becomes_html():
    assert render_markdown("**EPI**") == "<p><strong>EPI</strong></p>"


def test_script_tags_are_neutralised():
    html = render_markdown("<script>alert(1)</script>")
    assert "<script>" not in html


def test_javascript_links_are_dropped():
    assert "javascript:" not in render_markdown("[x](javascript:alert(1))")


def test_tables_and_images_are_kept():
    html = render_markdown("| a |\n|---|\n| 1 |\n\n![EPI](/media/epi.webp)")
    assert "<table>" in html
    assert '<img alt="EPI" src="/media/epi.webp">' in html


def test_calculator_marker_becomes_an_inert_widget_slot():
    html = render_markdown("Essayez :\n\n[[calc:ohm]]")

    assert '<div class="calc" data-calc="ohm"></div>' in html
    assert "[[calc" not in html


def test_every_documented_calculator_is_accepted():
    for kind in ("ohm", "divider", "resistor", "bias"):
        assert f'data-calc="{kind}"' in render_markdown(f"[[calc:{kind}]]")


def test_part_two_calculators_are_accepted():
    """US-42 : réactance, fréquence de coupure et résonance (Partie 2)."""
    for kind in ("reactance", "cutoff", "resonance"):
        assert f'<div class="calc" data-calc="{kind}"></div>' in render_markdown(f"[[calc:{kind}]]")


def test_part_three_calculators_are_accepted():
    """US-50 : gain, transformateur et ondulation (Partie 3)."""
    for kind in ("gain", "transformer", "ripple"):
        assert f'<div class="calc" data-calc="{kind}"></div>' in render_markdown(f"[[calc:{kind}]]")


def test_unknown_calculator_stays_plain_text():
    html = render_markdown("[[calc:rm-rf]]")

    assert "data-calc" not in html
    assert "[[calc:rm-rf]]" in html


def test_calculator_marker_inside_a_sentence_is_not_expanded():
    assert "data-calc" not in render_markdown("Le marqueur [[calc:ohm]] doit être seul sur sa ligne.")


def test_markup_cannot_forge_a_calculator_slot():
    html = render_markdown('<div class="calc" data-calc="ohm" onclick="alert(1)"></div>')

    assert "data-calc" not in html and "onclick" not in html


def test_diagrams_link_to_their_full_size_file():
    html = render_markdown("![Loi d'Ohm](/static/content/electro/m1/ohm-circuit.svg)")

    assert '<a class="figure-zoom" href="/static/content/electro/m1/ohm-circuit.svg">' in html
    assert '<img alt="Loi d\'Ohm" src="/static/content/electro/m1/ohm-circuit.svg"></a>' in html


def test_other_images_are_not_wrapped():
    assert "figure-zoom" not in render_markdown("![Photo](/media/epi.webp)")


def test_external_svg_is_never_linked():
    assert "figure-zoom" not in render_markdown("![x](https://evil.example/x.svg)")


def test_moteurs_calculators_are_accepted():
    """US-68 (formation `moteurs`, M8) : courant d'un moteur, vitesse, couple, étoile-triangle."""
    for kind in ("motor_current", "speed", "torque", "stardelta"):
        assert f'<div class="calc" data-calc="{kind}"></div>' in render_markdown(f"[[calc:{kind}]]")


# --- US-108 (formation `esp32`, C6) : blocs de code délimités dans les sections --------------------------------------

BLINK = "```cpp\nconst uint8_t LED_PIN = 2;\nvoid loop() {\n  if (a < b && c > d) digitalWrite(LED_PIN, HIGH);\n}\n```"


def test_a_fenced_code_block_becomes_a_pre_code_block():
    html = render_markdown("Le programme :\n\n" + BLINK)

    assert "<pre><code>const uint8_t LED_PIN = 2;\nvoid loop() {" in html
    assert "```" not in html


def test_a_fenced_code_block_is_escaped_and_keeps_no_attribute():
    html = render_markdown(BLINK)

    assert "if (a &lt; b &amp;&amp; c &gt; d)" in html
    assert "class=" not in html


def test_a_fenced_block_without_language_is_rendered_too():
    assert "<pre><code>Serial.begin(115200);\n</code></pre>" in render_markdown("```\nSerial.begin(115200);\n```")


def test_markers_inside_a_code_block_are_never_expanded():
    html = render_markdown("```\n[[calc:ohm]]\n\n[[fig:rc_lowpass]]\n```")

    assert "data-calc" not in html
    assert "data-fig" not in html
    assert "[[calc:ohm]]" in html
