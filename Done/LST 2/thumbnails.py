"""
==============================================================================
SciPK Thumbnail Generator
"How to Represent a State-Space Linear System using Block Diagrams" (Simulink)
==============================================================================

Three thumbnail concepts, one Manim Scene each, rendered as a single
1280x720 still frame (standard YouTube thumbnail size):

    1. BlackBoxThumbnail      -- the video's own hook: "what's inside the box?"
    2. MemoryThumbnail        -- the car/integrator "systems remember" analogy
    3. BlockDiagramThumbnail  -- the payoff: any system = 3 simple blocks

No LaTeX is required. Every math symbol (u, y, an integral sign, sigma) is
drawn with plain Text() using unicode glyphs, so the only dependency is
Manim itself -- no TeX distribution needed.

INSTALL:
    pip install manim

RENDER (the -s flag saves only the final frame as a PNG and skips video
encoding entirely -- exactly what you want for a thumbnail):
    manim -s -qh scipk_thumbnails.py BlackBoxThumbnail
    manim -s -qh scipk_thumbnails.py MemoryThumbnail
    manim -s -qh scipk_thumbnails.py BlockDiagramThumbnail

Output PNGs land in:
    media/images/scipk_thumbnails/<SceneName>_<version>.png

Treat the exact numbers below (positions, scales, font sizes) as a strong
first pass, not gospel -- nudge them after your first render. Manim will
immediately show you if two elements collide.
"""

from manim import *

# ---------------------------------------------------------------------------
# Shared palette: dark aerospace-console navy + rocket-orange / tech-cyan
# accents, so all three thumbnails read as one consistent series/thumbnail
# family for the channel.
# ---------------------------------------------------------------------------
BG = "#0A0E27"       # deep console navy -- background
ORANGE = "#FF6B35"   # rocket orange -- inputs / warm accent
CYAN = "#00D9FF"     # tech cyan -- systems / cool accent
YELLOW = "#FFD23F"   # highlight yellow -- gain / summing blocks
INK = "#F5F5F5"      # near-white -- headline text
FAINT = "#4A5578"    # muted slate -- background hints (matrix labels)
DARKBAR = "#000000"  # banner backing behind headline text

config.pixel_width = 1280
config.pixel_height = 720


# ---------------------------------------------------------------------------
# Shared helpers, reused across all three scenes
# ---------------------------------------------------------------------------

def glow_box(width, height, color, layers=5, corner_radius=0.18):
    """A rounded rectangle with a soft outer glow -- built from stacked,
    increasingly faint copies rather than a real blur (Manim has no cheap
    Gaussian blur). Reads well at thumbnail scale and thumbnail-compression."""
    group = VGroup()
    for i in range(layers, 0, -1):
        group.add(RoundedRectangle(
            width=width + i * 0.05, height=height + i * 0.05,
            corner_radius=corner_radius, stroke_width=0,
            fill_color=color, fill_opacity=0.04,
        ))
    group.add(RoundedRectangle(
        width=width, height=height, corner_radius=corner_radius,
        stroke_color=color, stroke_width=6, fill_color=BG, fill_opacity=1,
    ))
    return group


def banner_headline(text, font_size=54, bar_width=13.0, bar_height=1.5):
    """Bold white headline on a translucent black bar so it stays readable
    no matter what's rendered behind it -- standard thumbnail-legibility
    trick, since thumbnails get shrunk to ~120px tall in the feed."""
    bar = Rectangle(width=bar_width, height=bar_height, fill_color=DARKBAR,
                     fill_opacity=0.55, stroke_width=0)
    label = Text(text, color=INK, weight=BOLD, font_size=font_size,
                 line_spacing=0.9)
    label.move_to(bar.get_center())
    return VGroup(bar, label)


def gain_triangle(color, size=1.0):
    """Standard control-diagram gain symbol: a sideways (right-pointing)
    triangle -- matches how gain blocks are actually drawn in Simulink."""
    tri = Triangle(color=color, fill_color=color, fill_opacity=1, stroke_width=0)
    tri.rotate(-PI / 2)  # default points up -> rotate to point right
    tri.scale(size)
    return tri


# ---------------------------------------------------------------------------
# THUMBNAIL 1 -- "What's really inside the box?"
# ---------------------------------------------------------------------------
class BlackBoxThumbnail(Scene):
    """
    CONCEPT: the video's own hook. The system is a glowing "black box" sitting
    between u(t) and y(t), with the matrices that secretly define it (A, B, C,
    D) just barely visible inside, like a circuit board under frosted glass.
    Curiosity-driven -- "what's actually happening in there?" -- which is
    exactly what the video goes on to answer. Honest to the content: this
    black-box framing is literally how the script introduces the System block.
    """

    def construct(self):
        self.camera.background_color = BG

        box = glow_box(3.6, 2.8, CYAN)
        box.move_to(UP * 0.4)

        hint = Text("A   B\nC   D", color=FAINT, font_size=30, line_spacing=1.2)
        hint.move_to(box.get_center() + DOWN * 0.5)

        mark = Text("?", color=CYAN, weight=BOLD, font_size=100)
        mark.move_to(box.get_center() + UP * 0.6)

        in_arrow = Arrow(LEFT * 6.0 + UP * 0.4, box.get_left(), color=ORANGE,
                          stroke_width=10, buff=0.1)
        out_arrow = Arrow(box.get_right(), RIGHT * 6.0 + UP * 0.4, color=ORANGE,
                           stroke_width=10, buff=0.1)

        u_label = Text("u(t)", color=INK, weight=BOLD, font_size=40)
        u_label.next_to(in_arrow, UP, buff=0.15)
        y_label = Text("y(t)", color=INK, weight=BOLD, font_size=40)
        y_label.next_to(out_arrow, UP, buff=0.15)

        headline = banner_headline("WHAT'S REALLY\nINSIDE THE BOX?", font_size=50)
        headline.to_edge(DOWN, buff=0.3)

        subhead = Text("State-space systems -> block diagrams", color=CYAN,
                        weight=BOLD, font_size=24)
        subhead.next_to(headline, UP, buff=0.15)

        self.add(box, hint, mark, in_arrow, out_arrow, u_label, y_label,
                  headline, subhead)


# ---------------------------------------------------------------------------
# THUMBNAIL 2 -- "Systems that remember"
# ---------------------------------------------------------------------------
class MemoryThumbnail(Scene):
    """
    CONCEPT: the video's own analogy. A parked car "remembers" it was doing
    10 mph before it stopped -- which is exactly what an integrator does
    mathematically. A simple car icon feeds into a glowing integral-sign
    block, which outputs a "remembers 10 mph" badge -- translating an
    abstract idea (memory / state in a dynamical system) into something
    anyone scrolling past instantly gets, without misrepresenting the
    actual content (this analogy is drawn directly from the script's Intro).
    """

    def construct(self):
        self.camera.background_color = BG

        # --- car, built from primitive shapes (no external image assets) ---
        body = RoundedRectangle(width=2.5, height=0.85, corner_radius=0.22,
                                 fill_color=ORANGE, fill_opacity=1, stroke_width=0)
        roof = RoundedRectangle(width=1.3, height=0.65, corner_radius=0.18,
                                 fill_color=ORANGE, fill_opacity=1, stroke_width=0)
        roof.move_to(body.get_center() + UP * 0.62 + LEFT * 0.15)
        wheel_l = Circle(radius=0.26, fill_color="#12162E", fill_opacity=1, stroke_width=0)
        wheel_r = wheel_l.copy()
        wheel_l.move_to(body.get_bottom() + LEFT * 0.75 + UP * 0.02)
        wheel_r.move_to(body.get_bottom() + RIGHT * 0.75 + UP * 0.02)
        car = VGroup(body, roof, wheel_l, wheel_r)
        car.move_to(LEFT * 4.7 + DOWN * 0.1)

        # --- motion streaks trailing behind it, suggesting "was moving" ---
        streaks = VGroup(*[
            Line(LEFT * 0.55, RIGHT * 0.55, color=CYAN, stroke_width=7 - i * 1.5)
            .set_opacity(0.55 - i * 0.15)
            .move_to(car.get_left() + LEFT * (0.9 + i * 0.55) + DOWN * (0.05 * i))
            for i in range(3)
        ])

        # --- integrator block ---
        integrator = glow_box(1.9, 1.9, CYAN)
        integrator.move_to(RIGHT * 0.4 + DOWN * 0.1)
        integral_sign = Text("\u222B", color=CYAN, weight=BOLD, font_size=110)
        integral_sign.move_to(integrator.get_center() + UP * 0.05)

        arrow_in = Arrow(car.get_right() + RIGHT * 0.25, integrator.get_left(),
                          color=INK, stroke_width=9, buff=0.1)
        arrow_out = Arrow(integrator.get_right(), RIGHT * 4.3 + DOWN * 0.1,
                           color=INK, stroke_width=9, buff=0.1)

        badge_bg = RoundedRectangle(width=2.6, height=0.95, corner_radius=0.15,
                                     fill_color=YELLOW, fill_opacity=1, stroke_width=0)
        badge_txt = Text("REMEMBERS\n10 MPH", color=BG, weight=BOLD,
                          font_size=22, line_spacing=0.9)
        badge_txt.move_to(badge_bg.get_center())
        badge = VGroup(badge_bg, badge_txt)
        badge.move_to(RIGHT * 5.6 + DOWN * 0.1)

        headline = banner_headline("SYSTEMS THAT\nREMEMBER", font_size=52)
        headline.to_edge(DOWN, buff=0.3)

        subhead = Text("Why integrators give math a memory", color=CYAN,
                        weight=BOLD, font_size=24)
        subhead.next_to(headline, UP, buff=0.15)

        self.add(streaks, car, arrow_in, integrator, integral_sign, arrow_out,
                  badge, headline, subhead)


# ---------------------------------------------------------------------------
# THUMBNAIL 3 -- "3 blocks build any system"
# ---------------------------------------------------------------------------
class BlockDiagramThumbnail(Scene):
    """
    CONCEPT: the payoff of the whole video. Any linear system, no matter how
    complex, decomposes into just three block types -- an integrator, a gain,
    and a summing junction. Shown as a tight loop (visual shorthand for
    feedback), it reads like a clean, satisfying control-systems diagram at a
    glance. Honest to content: decomposing a system into exactly these three
    block types is literally what Section 2 of the script does in Simulink.
    """

    def construct(self):
        self.camera.background_color = BG

        # --- three hero blocks, arranged in a triangular loop ---
        integrator = glow_box(2.0, 1.5, CYAN)
        integrator.move_to(UP * 1.6)
        integrator_sym = Text("\u222B", color=CYAN, weight=BOLD, font_size=80)
        integrator_sym.move_to(integrator.get_center())
        integrator_lbl = Text("INTEGRATOR", color=CYAN, weight=BOLD, font_size=20)
        integrator_lbl.next_to(integrator, UP, buff=0.15)

        gain = gain_triangle(ORANGE, size=1.5)
        gain.move_to(DOWN * 1.1 + LEFT * 3.6)
        gain_lbl = Text("GAIN", color=ORANGE, weight=BOLD, font_size=20)
        gain_lbl.next_to(gain, DOWN, buff=0.3)

        summer = Circle(radius=1.0, color=YELLOW, fill_color=BG, fill_opacity=1,
                         stroke_width=6)
        summer.move_to(DOWN * 1.1 + RIGHT * 3.6)
        summer_sym = Text("\u03A3", color=YELLOW, weight=BOLD, font_size=70)
        summer_sym.move_to(summer.get_center())
        summer_lbl = Text("SUMMER", color=YELLOW, weight=BOLD, font_size=20)
        summer_lbl.next_to(summer, DOWN, buff=0.3)

        loop = VGroup(
            CurvedArrow(gain.get_top(), integrator.get_left(), color=INK,
                        stroke_width=6, angle=-TAU / 8),
            CurvedArrow(integrator.get_right(), summer.get_top(), color=INK,
                        stroke_width=6, angle=-TAU / 8),
            CurvedArrow(summer.get_left(), gain.get_right(), color=INK,
                        stroke_width=6, angle=-TAU / 8),
        )

        u_arrow = Arrow(LEFT * 6.0 + DOWN * 1.1, gain.get_left(), color=INK,
                         stroke_width=8, buff=0.15)
        u_lbl = Text("u", color=INK, weight=BOLD, font_size=32).next_to(u_arrow, UP, buff=0.1)
        y_arrow = Arrow(summer.get_right(), RIGHT * 6.0 + DOWN * 1.1, color=INK,
                         stroke_width=8, buff=0.15)
        y_lbl = Text("y", color=INK, weight=BOLD, font_size=32).next_to(y_arrow, UP, buff=0.1)

        headline = banner_headline("3 BLOCKS BUILD\nANY SYSTEM", font_size=48)
        headline.to_edge(DOWN, buff=0.25)

        self.add(loop, integrator, integrator_sym, integrator_lbl,
                  gain, gain_lbl, summer, summer_sym, summer_lbl,
                  u_arrow, u_lbl, y_arrow, y_lbl, headline)


if __name__ == "__main__":
    print(__doc__)