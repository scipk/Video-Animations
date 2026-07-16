from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService

class Animation_2(VoiceoverScene):
    def construct(self):
        # Initialize Google TTS voiceover service
        self.set_speech_service(GTTSService(lang="en", tld="com"))

        # =========================================================================
        # PART 1: Opening the Box to Reveal "State" (0.0s to 4.5s)
        # =========================================================================
        box = Square(side_length=2.5, color=BLUE)
        box_text = Text("Black Box", font_size=28, color=WHITE).move_to(box.get_center())

        dashed_box = DashedVMobject(box, num_dashes=30).set_color(BLUE_E)
        # State vector representation
        state_vector = MathTex(
            r"\mathbf{x} = \begin{bmatrix} x_1 \\ x_2 \end{bmatrix}", 
            font_size=42
        ).move_to(box.get_center())
        state_label = Text("State", font_size=24, color=YELLOW).next_to(dashed_box, UP, buff=0.3)

        with self.voiceover(
            text="Let's open the box and describe what's inside, calling it the state."
        ) as tracker:
            # Draw the original system box
            self.play(Create(box), Write(box_text), run_time=1.0)
            
            # "Open" the box by turning its borders dashed and revealing the state vector inside
            self.play(
                ReplacementTransform(box, dashed_box),
                ReplacementTransform(box_text, state_vector),
                FadeIn(state_label, shift=UP),
                dashed_box.animate.scale(1.2),
                run_time=1.5
            )
            self.wait(2.0)

        # Clear Part 1 elements
        self.play(
            FadeOut(dashed_box),
            FadeOut(state_vector),
            FadeOut(state_label),
            run_time=0.5
        )

        # =========================================================================
        # PART 2: The Moving Car Example (4.5s to 10.0s)
        # =========================================================================
        # Ground line
        ground = Line(start=LEFT * 5 + DOWN * 1.5, end=RIGHT * 5 + DOWN * 1.5, color=GRAY)
        
        # Simple procedural car
        car_body = Rectangle(width=2, height=0.7, fill_color=BLUE_D, fill_opacity=0.8, stroke_color=WHITE)
        car_body.shift(UP * 0.35)
        wheel_l = Circle(radius=0.22, fill_color=BLACK, fill_opacity=1, stroke_color=WHITE).move_to(LEFT * 0.6 + DOWN * 0.1)
        wheel_r = Circle(radius=0.22, fill_color=BLACK, fill_opacity=1, stroke_color=WHITE).move_to(RIGHT * 0.6 + DOWN * 0.1)
        
        # Velocity arrow attached to the front of the car
        vel_arrow = Arrow(start=ORIGIN, end=RIGHT * 1.2, color=YELLOW, buff=0).next_to(car_body, RIGHT, buff=0)
        
        # FIXED: Changed from Text with font_style to MathTex for automatic mathematical italics
        vel_tag = MathTex("v", font_size=24, color=YELLOW).next_to(vel_arrow, UP, buff=0.1)
        
        # Grouping car elements together
        car_system = VGroup(car_body, wheel_l, wheel_r, vel_arrow, vel_tag).shift(LEFT * 3.5 + DOWN * 1.3)

        # Dynamic state labels
        states_header = Text("States of the Car:", font_size=24).to_edge(UP)
        pos_text = Text("Position (x)", font_size=20, color=GREEN).next_to(states_header, DOWN, buff=0.2)
        vel_text = Text("Velocity (v)", font_size=20, color=YELLOW).next_to(pos_text, DOWN, buff=0.2)
        labels_group = VGroup(states_header, pos_text, vel_text)

        with self.voiceover(
            text="For example, in a moving car, the states could be its position and its velocity."
        ) as tracker:
            # Introduce the car on the ground along with the state labels
            self.play(
                Create(ground),
                FadeIn(car_system, shift=RIGHT),
                Write(labels_group),
                run_time=1.0
            )
            
            # Highlight labels and move the car forward to visualize position changes and speed
            self.play(
                car_system.animate.shift(RIGHT * 4.5),
                pos_text.animate.scale(1.15).set_color(GREEN_A),
                vel_text.animate.scale(1.15).set_color(YELLOW_A),
                run_time=3.0
            )
            self.wait(1.0)

        # Clear Part 2 elements
        self.play(
            FadeOut(ground),
            FadeOut(car_system),
            FadeOut(labels_group),
            run_time=0.5
        )

        # =========================================================================
        # PART 3: Time Domain vs Frequency Domain (10.0s to 17.0s)
        # =========================================================================
        # Left side: Time Domain (Linear Algebra)
        time_title = Text("Time Domain", font_size=28, color=GREEN).shift(LEFT * 3.2 + UP * 1.8)
        time_eq = MathTex(
            r"\dot{\mathbf{x}}(t) = \mathbf{A}\mathbf{x}(t) + \mathbf{B}\mathbf{u}(t)", 
            font_size=32
        ).next_to(time_title, DOWN, buff=0.8)
        time_desc = Text("Linear Algebra Basis", font_size=18, color=GRAY).next_to(time_eq, DOWN, buff=0.5)
        time_group = VGroup(time_title, time_eq, time_desc)

        # Right side: Frequency Domain (Classical Laplace)
        freq_title = Text("Frequency Domain", font_size=28, color=RED).shift(RIGHT * 3.2 + UP * 1.8)
        freq_eq = MathTex(
            r"H(s) = \frac{Y(s)}{U(s)}", 
            font_size=34
        ).next_to(freq_title, DOWN, buff=0.8)
        freq_desc = Text("Classical Transfer Functions", font_size=18, color=GRAY).next_to(freq_eq, DOWN, buff=0.5)
        freq_group = VGroup(freq_title, freq_eq, freq_desc)

        # Large Red "X" to place over the Frequency Domain
        cross_line1 = Line(start=RIGHT * 1.2 + UP * 2.2, end=RIGHT * 5.2 + DOWN * 1.8, color=RED, stroke_width=6)
        cross_line2 = Line(start=RIGHT * 1.2 + DOWN * 1.8, end=RIGHT * 5.2 + UP * 2.2, color=RED, stroke_width=6)
        cross_mark = VGroup(cross_line1, cross_line2)

        with self.voiceover(
            text="Thanks to him, now we can use Linear Algebra in the Time Domain, so there's no need to transfer into the Frequency Domain anymore."
        ) as tracker:
            # Reveal both systems side by side
            self.play(
                FadeIn(time_group, shift=UP),
                FadeIn(freq_group, shift=UP),
                run_time=2.0
            )
            
            # Boldly cross out the frequency domain side
            self.play(Create(cross_mark), run_time=1.5)
            
            # Dim the frequency domain to emphasize the shift to Time Domain
            self.play(
                freq_group.animate.set_opacity(0.2),
                cross_mark.animate.set_opacity(0.4),
                time_group.animate.scale(1.1),
                run_time=1.5
            )
            self.wait(1.5)