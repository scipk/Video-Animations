from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService

class Animation_3(VoiceoverScene):
    def construct(self):
        self.set_speech_service(GTTSService(lang="en", tld="com"))

        # Part 1
        # Script: "When we're building a state-space linear system, we have the input function $u(t)$, which exists as a vector of Real Numbers of size $k$ ($\mathbb{R}^k$), a state function $x(t)$, which exists as a vector of Real Numbers of size $n$ ($\mathbb{R}^n$), and an output function $y(t)$, which exists as a vector of Real Numbers of size $m$ ($\mathbb{R}^m$). Notice how all three of those depend on time."
        header = Text("State-Space Linear System", font_size=36, color=WHITE).to_edge(UP)

        box = Rectangle(width=3.5, height=2.2, color=BLUE, fill_color=BLACK, fill_opacity=1)

        arrow_in = Arrow(start=LEFT * 4.5, end=LEFT * 1.8, color=WHITE)
        label_in = MathTex(r"u", r"(t)", r" \in \mathbb{R}^k", font_size=36).next_to(arrow_in, UP, buff=0.1)

        box_text = MathTex(r"x", r"(t)", r" \in \mathbb{R}^n", font_size=40).move_to(box.get_center())

        arrow_out = Arrow(start=RIGHT * 1.8, end=RIGHT * 4.5, color=WHITE)
        label_out = MathTex(r"y", r"(t)", r" \in \mathbb{R}^m", font_size=36).next_to(arrow_out, UP, buff=0.1)
        
        with self.voiceover(text="When we're building a state-space linear system, ") as tracker:
            self.play(
                Create(header),
                run_time=3.0
            )

        with self.voiceover(text="we have the input function u, which exists as a vector of Real Numbers of size k,") as tracker:
            self.play(
                Create(arrow_in),
                run_time=2.0
            )
            self.play(
                Write(label_in),
                run_time=4.0
            )

        with self.voiceover(text="a state function x, which exists as a vector of Real Numbers of size n, ") as tracker:
            self.play(
                Create(box),
                run_time=2.0
            )
            self.play(
                Write(box_text),
                run_time=3.0
            )

        with self.voiceover(text="and an output function y, which exists as a vector of Real Numbers of size m.") as tracker:
            self.play(
                Create(arrow_out),
                run_time=2.0
            )
            self.play(
                Write(label_out),
                run_time=3.0
            )
        
        self.wait(1.0)

        with self.voiceover(text="Notice how all three of those depend on time.") as tracker:
            self.play(
                label_in[1].animate.set_color(YELLOW),
                box_text[1].animate.set_color(YELLOW),
                label_out[1].animate.set_color(YELLOW),
                run_time=3.0
            )
        
        self.play(FadeOut(header, arrow_in, label_in, box, box_text, arrow_out, label_out), run_time=1.0)


        # Part 2
        # Script: Let me teach you the term "Continuous-Time". That means that time is an element of all the numbers from 0 to infinity with no breaks. ($t \in [0,\infty)$) Every infinitely small number right after another.

        header = Text("Continuous-Time", font_size=36, color=WHITE).to_edge(UP)
        t_equation = MathTex(r"t \in [0,\infty)", font_size=36).next_to(header, DOWN, buff=0.5)

        number_line = NumberLine(x_range=[0, 10, 1], length=10, color=WHITE)
        label_zero = MathTex(r"0", font_size=36, color=YELLOW).next_to(number_line, LEFT, buff=0.5)
        label_infinity = MathTex(r"\infty", font_size=36, color=YELLOW).next_to(number_line, RIGHT, buff=0.5)


        with self.voiceover(text="Let me teach you the term Continuous-Time. ") as tracker:
            self.play(
                Write(header),
                run_time=1.0
            )
        
        with self.voiceover(text="That means that time is an element of all the numbers from 0 to infinity with no breaks.") as tracker:
            self.play(
                Write(t_equation),
                Create(number_line),
                Write(label_zero),
                Write(label_infinity),
                run_time=1.0
            )

        # 1. Highlight the interval [1, 2] on the original number line
        zoom_box = SurroundingRectangle(
            Line(number_line.n2p(1), number_line.n2p(2)),
            color=YELLOW,
            buff=0.15
        )
        self.play(Create(zoom_box), run_time=1.0)
        
        # 2. Setup the zoomed-in number line representing [1, 2]
        zoom_line = NumberLine(
            x_range=[1, 2, 0.1], 
            length=10, 
            color=WHITE, 
            include_numbers=True,
            font_size=24
        ).shift(DOWN * 0.5)
        
        # Transition from the full number line to the zoomed-in segment
        self.play(
            FadeOut(t_equation, label_zero, label_infinity, zoom_box),
            ReplacementTransform(number_line, zoom_line),
            run_time=1.5
        )
        
        # 3. Define generations of points to illustrate "filling the gaps"
        # Sparse dots (Spacing: 0.2)
        dots_step_1 = VGroup(*[
            Dot(zoom_line.n2p(1.0 + i * 0.2), color=BLUE, radius=0.08)
            for i in range(6)
        ])
        
        # Medium-dense dots (Spacing: 0.05)
        dots_step_2 = VGroup(*[
            Dot(zoom_line.n2p(1.0 + i * 0.05), color=BLUE, radius=0.05)
            for i in range(21)
        ])
        
        # Very dense dots (Spacing: 0.01)
        dots_step_3 = VGroup(*[
            Dot(zoom_line.n2p(1.0 + i * 0.01), color=YELLOW, radius=0.03)
            for i in range(101)
        ])
        
        # Solid continuous line representing the infinite packed limit
        solid_line = Line(
            start=zoom_line.n2p(1.0),
            end=zoom_line.n2p(2.0),
            color=YELLOW,
            stroke_width=6
        )
        
        # 4. Animate the points filling up the continuum
        with self.voiceover(text="Every infinitely small number right after another.") as tracker:
            # Show the first set of discrete values
            self.play(Create(dots_step_1), run_time=1.0)
            
            # Animate adding points in between them
            self.play(
                ReplacementTransform(dots_step_1, dots_step_2),
                run_time=0.5
            )
            
            # Pack them extremely closely together
            self.play(
                ReplacementTransform(dots_step_2, dots_step_3),
                run_time=0.5
            )
            
            # Finally, transition into a solid continuous line
            self.play(
                ReplacementTransform(dots_step_3, solid_line),
                run_time=0.5
            )
            
        self.wait(1.5)
        
        # Clean up the screen
        self.play(
            FadeOut(header, zoom_line, solid_line),
            run_time=1.0
        )
