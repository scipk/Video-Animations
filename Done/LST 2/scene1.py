"""
Block Diagram Scene — SciPK
============================

Animates the script:
  - Basic block diagram: u -> [System] -> y
  - Memoryless system (ruler example)
  - System with memory / state (car example: position, velocity)
  - General "System" block, labeled P

Setup
-----
    pip install manim manim-voiceover
    pip install "manim-voiceover[gtts]"     # free, offline-ish TTS for drafting
    # For your real voice track, swap GTTSService() below for:
    #   from manim_voiceover.services.recorder import RecorderService
    #   self.set_speech_service(RecorderService())
    # which will record from your mic and let you re-take lines.

Render
------
    manim -pql block_diagram_scene.py BlockDiagramIntro     # quick draft (480p)
    manim -pqh block_diagram_scene.py BlockDiagramIntro     # final (1080p)
"""

from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService


class BlockDiagramIntro(VoiceoverScene):
    def construct(self):
        self.set_speech_service(GTTSService())

        # =================================================================
        # 1. Basic block diagram:  u -> [ System ] -> y
        # =================================================================
        box = Rectangle(width=2.5, height=1.5, color=BLUE)
        box_label = Text("System", font_size=32)
        box_label.move_to(box)

        in_arrow = Arrow(LEFT * 4, box.get_left(), buff=0.15)
        out_arrow = Arrow(box.get_right(), RIGHT * 4, buff=0.15)

        u_label = MathTex("u").next_to(in_arrow, UP)
        y_label = MathTex("y").next_to(out_arrow, UP)

        diagram = VGroup(box, box_label, in_arrow, out_arrow, u_label, y_label)

        with self.voiceover(text="A block diagram for a linear system is easy.") as tracker:
            self.play(Create(box), run_time=3.25)

        with self.voiceover(
            text="Remember from the last video that u is our input vector, "
            "and y is our output vector."
        ) as tracker:
            self.play(
                GrowArrow(in_arrow),
                Write(u_label),
                GrowArrow(out_arrow),
                Write(y_label),
                Write(box_label),
                run_time=6.7,
            )

        self.wait(0.3)

        # =================================================================
        # 2. Memoryless system
        # =================================================================
        memoryless_label = Text("Memoryless System", font_size=28, color=YELLOW)
        memoryless_label.next_to(diagram, DOWN, buff=0.6)

        with self.voiceover(
            text="Well, this on its own is called a memoryless system."
        ) as tracker:
            self.play(FadeIn(memoryless_label, shift=UP), run_time=3.4)

        self.play(FadeOut(memoryless_label))

        # shrink the diagram up top to make room for the ruler example
        self.play(diagram.animate.scale(0.6).to_edge(UP))

        # --- ruler visual (simple rectangle + tick marks) ---
        def make_ruler():
            body = Rectangle(width=4, height=0.5, color=GREY_B, fill_opacity=0.15)
            ticks = VGroup(
                *[
                    Line(
                        body.get_bottom() + RIGHT * (i * 0.4 - 1.8),
                        body.get_bottom() + RIGHT * (i * 0.4 - 1.8) + UP * 0.15,
                        color=GREY_B,
                    )
                    for i in range(10)
                ]
            )
            return VGroup(body, ticks)

        ruler = make_ruler().shift(DOWN * 1.0)

        with self.voiceover(
            text="For example, when you use a ruler to measure the height of something,"
        ) as tracker:
            self.play(Create(ruler), run_time=4.4)

        measurement = Text("5 inches", font_size=32, color=GREEN)
        measurement.next_to(ruler, DOWN, buff=0.4)

        with self.voiceover(text="and find it to be 5 inches,") as tracker:
            self.play(Write(measurement), run_time=2.25)

        yesterday = Text("Yesterday: 10 inches", font_size=24, color=GREY_A)
        yesterday.next_to(measurement, DOWN, buff=0.4)
        cross = Cross(yesterday, stroke_color=RED)

        with self.voiceover(
            text="the ruler doesn't remember that yesterday you measured "
            "something else that was 10 inches."
        ) as tracker:
            half = 5.0 / 2
            self.play(FadeIn(yesterday), run_time=half)
            self.play(Create(cross), run_time=half)

        self.wait(0.4)
        self.play(
            FadeOut(ruler),
            FadeOut(measurement),
            FadeOut(yesterday),
            FadeOut(cross),
        )

        # =================================================================
        # 3. System with memory / state — car example
        # =================================================================
        state_label = Text("State: position (x), velocity (v)", font_size=28, color=ORANGE)
        state_label.move_to(ORIGIN)

        with self.voiceover(
            text="But let's say our system had a state that had memory, "
            "like position or velocity."
        ) as tracker:
            self.play(Write(state_label), run_time=6.0)

        self.play(state_label.animate.to_edge(UP, buff=1.5))

        # --- car visual (rounded rectangle body + two wheels) ---
        def make_car():
            body = RoundedRectangle(
                width=2.4, height=0.8, corner_radius=0.15, color=BLUE_D, fill_opacity=0.6
            )
            wheel_l = Circle(radius=0.25, color=BLACK, fill_opacity=1)
            wheel_l.move_to(body.get_corner(DL) + RIGHT * 0.35 + UP * 0.05)
            wheel_r = Circle(radius=0.25, color=BLACK, fill_opacity=1)
            wheel_r.move_to(body.get_corner(DR) + LEFT * 0.35 + UP * 0.05)
            return VGroup(body, wheel_l, wheel_r)

        car = make_car().shift(LEFT * 4 + DOWN * 0.5)
        parking_spot = DashedVMobject(
            Rectangle(width=2.8, height=1.2, color=GREY_B), num_dashes=24
        )
        parking_spot.shift(RIGHT * 2 + DOWN * 0.5)

        with self.voiceover(
            text="Like a car, because it remembered that you parked it, and "
            "that it was going 10 miles per hour before you found the parking spot."
        ) as tracker:
            self.play(Create(parking_spot), run_time=8.0 * 0.25)
            self.play(
                car.animate.move_to(parking_spot.get_center()),
                run_time=8.0 * 0.75,
            )

        speed_label = Text("v: 10 mph  ->  0 mph (parked)", font_size=24, color=YELLOW)
        speed_label.next_to(car, DOWN, buff=0.5)
        self.play(Write(speed_label))
        self.wait(0.6)
        self.play(
            FadeOut(car),
            FadeOut(parking_spot),
            FadeOut(speed_label),
            FadeOut(state_label),
        )

        # =================================================================
        # 4. General System block, labeled P
        # =================================================================
        self.play(diagram.animate.scale(1 / 0.6).move_to(ORIGIN))

        state_box = Rectangle(width=1.2, height=0.8, color=ORANGE)
        state_box.next_to(box, DOWN, buff=0.7)
        state_box_label = MathTex("x").move_to(state_box)
        connecting_line = DashedLine(box.get_bottom(), state_box.get_top())

        with self.voiceover(
            text="That would fit in between the input and output — the same "
            "black box we mentioned in the other video."
        ) as tracker:
            self.play(
                Create(state_box),
                Write(state_box_label),
                Create(connecting_line),
                run_time=7.25,
            )

        new_label = MathTex("P", font_size=44)
        new_label.move_to(box)

        with self.voiceover(
            text="This block is called our System — we usually use capital P "
            "to represent it."
        ) as tracker:
            self.play(Transform(box_label, new_label), run_time=5.5)

        self.wait(1)